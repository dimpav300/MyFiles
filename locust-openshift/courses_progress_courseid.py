import time
# host=test
from locust import HttpUser, task, between
class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

       
    @task(1)
    def profile(self):
         headers = {
             'Authorization': f'Bearer {self.acces_token}'
         }
         res = self.client.get(
             "https://lxp-api-prod.azure-api.net/ProdStage/courses/progress/course-v1:WHOAcademy+CS101+2021",
             headers = headers
         )
    def on_start(self):
        access_token_url = "https://sso.lxp.academy.who.int/auth/realms/whoa-lxp/protocol/openid-connect/token"
        payload = {
            'client_id': "openedx-prod-oidc",
            'grant_type': "password",
            'username': "pavlidisd@who.int",
            'client_secret': "b0b9fa04-f854-43e5-94af-3cce26517fc3",
            'password': "Test123!",
        }
        res = self.client.post(access_token_url, data=payload)
        self.acces_token = res.json().get("access_token")