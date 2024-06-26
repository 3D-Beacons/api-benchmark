from locust import FastHttpUser
from omegaconf import OmegaConf
from utils import CSVReader

conf = OmegaConf.load("conf/api_conf.yaml")
DATA_FOLDER = "data"

class User(FastHttpUser):
    
    def on_start(self):
        for api in conf.apis:
            csv_reader = CSVReader(f"{DATA_FOLDER}/{api.params}")
            self.tasks.append(create_task(self, api.path, api.name, csv_reader, method=api.method))

def create_task(user_object: User, url: str, url_group, csv_reader: CSVReader, method="GET"):
    def api_task(*args):
        param = next(csv_reader)

        if method == "POST":
            with user_object.client.post(url, data=param, name=url_group, catch_response=True) as response:
                if response.status_code == 404:
                    response.success()
        else:
            parts = []
            for part in url.split("/"):
                if part.startswith(":"):
                    parts.append(param.pop(0))
                else:
                    parts.append(part)
            final_url = "/".join(parts)
            with user_object.client.get(final_url, name=url_group, catch_response=True) as response:
                if response.status_code == 404:
                    response.success()

    return api_task
