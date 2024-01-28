import requests, json, time

class HQData:
    def __init__(self, apikey: str, autofetch=True, debug_messages=True):
        self.apikey = apikey
        self.autofetch = autofetch
        self.debug = debug_messages
        try:
            import requests
            import json
            import time
            import timeit
            self.requests = requests
            self.json = json
            self.time = time
            self.timeit = timeit
        except ImportError as e:
            raise ImportError("Error: Missing required dependencies. Please install them using 'pip install requests json time timeit'") from e

        self.dbg("successfully initialized")

    def modules(self):
        """
        Fetches module data from the HQData API.
        :return: Available module data
        """
        response = requests.get("https://api.hqdata.com/modules", headers={"HQD-Authentification-Key": self.apikey}).json()
        modules = response["modules"]
        if response["status"] == "success":
            return modules
        else:
            raise Exception(response["status_message"])

    def subscription(self):
        """
        Fetches subscription data from the HQData API.
        :return: Subscription data
        """
        subscription = requests.get("https://api.hqdata.com/subscription", headers={"HQD-Authentification-Key": self.apikey}).json()
        if subscription["status"] == "success":
            return subscription
        else:
            raise Exception(subscription["status_message"])
  
    def fetch(self, id=None, fetch=None, chunks=None, chunk=None, page=None, status=None):
        """
        Fetches job/result data from the HQData API.

        :param id: Fetch a specific jobid (optional)
        :param fetch: Fetch html, screenshot or patterns data (optional)
        :param chunks: Define a specific chunks amount incase data is too large (optional)
        :param chunk: Fetch a specific chunk (optional)
        :param page: Job list pagination (optional)
        :param status: Filter jobs by status (optional)
        :return: Job/result data
        """
        params = {
            "id": id,
            "fetch": fetch,
            "chunks": chunks,
            "chunk": chunk,
            "page": page,
            "status": status
        }
        params = {key: value for key, value in params.items() if value is not None}
        result = requests.get("https://api.hqdata.com/list/", headers={"HQD-Authentification-Key": self.apikey}, params=params).json()
        try:
            status = result["status"]
        except:
            status = "success"

        if status == "error":
            raise Exception(result["status_message"])
        else:
            return result
    
    def run(self, module: str, payload: dict):
        """
        Runs a HQData module.
        :param module: HQData module
        :param payload: Post payload dictionary for specific module
        :return: Job/result data
        """
        payload["module"] = module
        response = requests.post("https://api.hqdata.com/run/", headers={"HQD-Authentification-Key": self.apikey}, data=json.dumps(payload)).json()
        if response["status"] == "error":
            raise Exception(response["status_message"])
        else:
            start_time = time.time()
            job_id = response["job_id"]
            if self.autofetch:
                checks = 0
                while True:
                    end_time = time.time()
                    time.sleep(2)
                    result = self.fetch(id=job_id)
                    execution_time = str(round(end_time - start_time, 2)) + " seconds"
                    if result[0]["status"] == "success":
                        self.dbg("job successfully executed - "+str(execution_time))
                        return result
                    elif result[0]["status"] == "pending":
                        self.dbg("job execution pending - "+str(execution_time))
                    elif result[0]["status"] == "running":
                        self.dbg("job still running - "+str(execution_time))
                    elif result[0]["status"] == "failed":
                        raise Exception("Job execution failed")
                    checks += 1
                    if checks > 30:
                        raise Exception("Waiting for job completion timed out")
            else:
                return job_id
        
    def dbg(self, msg):
        if self.debug:
            print("[hqdata] "+str(msg))