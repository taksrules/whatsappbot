import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .functions import *

# Create your views here.
def home(request):
    return render(request, 'business/index.html',{})

@csrf_exempt
def whatsAppWebhook(request):
    if request.method== 'GET':
        VERIFY_TOKEN='070ac4a2-76fe-4014-b31b-998e393f0264'
        mode= request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge= request.GET['hub.challenge']
        
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge,status=200)
        else:
            return HttpResponse('error', status=403)
    if request.method=='POST':
        data= json.loads(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                try:
                    for entry in data['entry']:
                        phoneNumber=entry['changes'][0]['value']['metadata']['display_phone_number']
                        phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                        profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        whatsAppId=entry['changes'][0]['value']['contacts'][0]['wa_id']
                        fromId= entry['changes'][0]['value']['messages'][0]['from']
                        messageId= entry['changes'][0]['value']['messages'][0]['id']
                        timestamp= entry['changes'][0]['value']['message'][0]['timestamp']
                        text= entry['changes'][0]['value']['message'][0]['text']['body']
                        
                        phoneNumber="263781798350"
                        message= 'RE: {} received'.format(text)
                        sendWhatAppMessage(phoneNumber, data)
                except:
                    pass
        
        return HttpResponse('success', status=200) 