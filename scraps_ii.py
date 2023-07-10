import requests 
import json 

response = requests.get('https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=pm10,pm2_5')

print(response)
#based on the returned status code printed, the GET API call was successful 


