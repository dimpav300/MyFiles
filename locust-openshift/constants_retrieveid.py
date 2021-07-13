import time
# host=test
from locust import HttpUser, task, between
class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def on_start(self):
        res = self.client.post("https://lxp-api-prod.azure-api.net/ProdStage/constants/retrieve?id=1&action=country")
    
