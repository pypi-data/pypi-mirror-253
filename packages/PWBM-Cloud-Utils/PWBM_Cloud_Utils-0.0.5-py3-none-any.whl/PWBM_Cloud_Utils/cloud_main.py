from .api_functions import RunListAPI, PolicyAPI, PolicyFilesAPI
import urllib.parse
import json
import requests

class Cloud_Main:

    _input_config: dict
    _runtime_option: dict

    _policy_files: any

    def __init__(self, run_id:int, policy_id: int, local: bool = True, merge_baseline: bool = True):
        run_list = RunListAPI()
        config = run_list.get_run_list(run_id)  #BatchId and JobId
        self._input_config = json.loads(config["runtime_configuration"])
        stacking_order = self._input_config['stacking_order'][0]
        print(self._input_config['stacking_order'])
        policy_api = PolicyAPI().get_policy(policy_id)
        policy_files = PolicyFilesAPI().get_all_files_by_policy(policy_id)
        self._policy_files = policy_files
        print('end')

    def convert_response_to_parameter(json_response):
        policy_parameter = {}
        for item in json_response:
            policy_parameter[str(item["name"])] = json.loads(item["data"])

        return policy_parameter

    @property
    def Input_Config(self):
        return self._input_config
    
    @property
    def Policy_Files(self):
        return self._policy_files
    
    def save_output(policy_id, policy_name):
        """get runtime options from the policyrun id

        Args:
            policy_id . policy_name

        Returns:
            _type_: json format of runtime options
        """
        policy_name_url = urllib.parse.quote(policy_name)
        url = "https://wits.pwbm-api.net/run_list/output_details/?id={}&path={}".format(
            str(policy_id), policy_name_url
        )
        return requests.post(url).json()
