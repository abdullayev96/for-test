from django.shortcuts import render, redirect
from twilio.rest import Client



def index(request):
    if request.method == "POST":
        name = request.POST['name']
        text = request.POST['text']
        num = request.POST['num']

        print(f"{name}||{text}||{num}")
        # if text:
        #     account_sid = "ACCOUNT_SID"  # your code
        #     auth_token = "AUTH_TOKEN"   ### your token
        #     client = Client(account_sid, auth_token)
        #     message  = client.messages.create(
        #         body=" sizga " + name +" SMS yuborildi :" + text,
        #         from_="",  #### yuborilgan raqam
        #         to="+998905862236")   #### qabul qiladigan raqam
        #     print(message)
        #     redirect('/')

    else:
        redirect('/')

    return render(request, 'index.html')

