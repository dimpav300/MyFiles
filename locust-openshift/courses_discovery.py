import time
# host=test
from locust import HttpUser, task, between
class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

       
    @task(1)
    def on_start(self):
         res = self.client.get(
             "https://lxp-api-prod.azure-api.net/ProdStage/courses/discovery?language=en", #english (EN) selected as language
         )
