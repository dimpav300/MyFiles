import time
import requests
import string
import random
# host=test
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def openedx(self):
    
        headers = {
            'Authorization': f'Bearer {self.acces_token}'
        }
         
        letters = string.ascii_letters
        slug = ( ''.join(random.choice(letters) for i in range(10)) )
        letters2 = string.ascii_letters        
        badgr_id = ( ''.join(random.choice(letters2) for i in range(10)) )
          
        data = {
            'openedx_slug': f'{slug}',
            'badgr_entity_id': f'{badgr_id}' 
        }
         
        res = self.client.post("https://lxp-api-prod.azure-api.net/ProdStage/openedx_badges", 
         headers = headers,
         data=data
         )   
        print(res.text)
         
         
    def on_start(self):
        access_token_url = "https://sso.lxp.academy.who.int/auth/realms/whoa-lxp/protocol/openid-connect/token"
        payload = {
            'client_id': "openedx-prod-oidc",
            'grant_type': "password",
            'username': "kannanm@who.int",
            'client_secret': "b0b9fa04-f854-43e5-94af-3cce26517fc3",
            'password': "test123",
        }
        res = self.client.post(access_token_url, data=payload)
        self.acces_token = res.json().get("access_token")