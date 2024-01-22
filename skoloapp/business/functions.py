from django.conf import settings
import requests

def sendWhatAppMessage(phoneNumber, message):
    headers= {"Authourization":settings.WHATSAPP_TOKEN}
    payload= {"messaging_product":"whatsapp",
              "recipient_type":"individual",
              "to":phoneNumber,
              "type":"text",
              "text":{"body":message}
              }
    response = requests.post(settings.WHATSAPP_URL, headers=headers,json=payload)
    ans= response.json()
    return ans
    
    
    
phoneNumber="263781798350"
message= "Hello there, \n This is it the first Link up"
sendWhatAppMessage(phoneNumber, message)