import time
# host=test
from io import open
from locust import HttpUser, task, between
class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

       
    @task(1)
    def profile(self):
         headers = {
             'Authorization': f'Bearer {self.acces_token}'
         }        
         files = {'profile_image': open('image.png','rb')}

         res = self.client.put(
             "https://lxp-api-prod.azure-api.net/ProdStage/profile/picture", 
             files=files,            
             headers = headers
         )
         print(res.text),
         
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