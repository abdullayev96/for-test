from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from random import randint
from django.contrib import messages
from .models import User


def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            user.confirm = randint(10000, 99999)
            user.save()
            # user ga sms yuborish
            messages.warning(request, "Success")
            return redirect('confirm', user.id)

        else:
            messages.warning(request, "Wrong details, please try again !!!")
            return redirect('/login')

    return render(request, 'login.html')



def confirm(request, id):
    if not request.user.is_authenticated:
        user = User.objects.get(id=id)
        if user and user.confirm != 0:
            if request.method == 'POST':
                confirm = request.POST['confirm']
                if user.confirm == int(confirm):
                    login(request, user)
                    user.confirm = 0
                    user.save()
                else:
                    messages.warning(request, "Wrong")
        else:
            return redirect('/')

    else:
        return redirect('/')
    return render(request, 'confirm.html', {"user": user})


