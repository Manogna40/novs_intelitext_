from django.http import FileResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import requests as req
import os
from pathlib import Path

env='prod'
url_dict={
    'General Text Suggestions':"http://10.185.56.168:8053/intellitext_general",
    'Clinical Text Suggestions':"http://10.185.56.168:8053/intellitext_abstracts"
}

suggestions=['suggestion1','suggestion2','''suggestion3  
    suggestion3 suggestion3 
    suggestion3 suggestion3
    suggestion3 suggestion3 suggestion3 suggestion3  
    suggestion3 suggestion3 
    suggestion3 suggestion3
    suggestion3 suggestion3 suggestion3 suggestion3  
    suggestion3 suggestion3 
    suggestion3 suggestion3
    suggestion3 suggestion3 suggestion3 suggestion3  
    suggestion3 suggestion3 
    suggestion3 suggestion3
    suggestion3 suggestion3 suggestion3''','suggestion4','suggestion5','suggestion6','suggestion7']

def render_home(request):
    return render(request, 'ui_preview_page.html', {})

@api_view(['GET','POST'])
def get_suggestions(request):
    model_name=request.POST['model_name']
    current_data=request.POST['current_data']
    if env=='prod':
        op_dict={'input_text':current_data}
        url = url_dict[model_name]
        resp = req.post(url,json=op_dict)
        resp_json = resp.json()
        # print('resp_json',resp_json)
        suggestions=[]
        for suggestion in resp_json:
            if suggestion['text'] not in suggestions and suggestion['text'].strip() !='':
                suggestions.append(suggestion['text'])

    return JsonResponse( {'data':suggestions})
    
    
