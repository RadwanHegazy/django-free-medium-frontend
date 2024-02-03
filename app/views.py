from django.shortcuts import render, redirect
import requests
from django.contrib.messages import success, error

def index (request) : 
    if request.method == "POST" : 
        
        data = {
            'link' : request.POST.get('link'),
            'email' : request.POST.get('email'),
            'lang' : request.POST.get('lang')
        }

        url = "http://127.0.0.1:4444/"
        req = requests.post(
            url = url,
            data = data,
        )

        if req.status_code == 200 : 
            success(request,"جاري بدأ العملية")
        else:
            error(request,"توجد مشكلة في بدأ العملية")
        print(req.json())
        return redirect('index')
    
    return render(request,'index.html')