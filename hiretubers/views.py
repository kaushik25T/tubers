from django.shortcuts import render , redirect
from  .models import Hiretuber
from django.contrib import messages

def hiretubers(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        tuber_id = request.POST.get('tuber_id')
        tuber_name = request.POST.get('tuber_name')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        state = request.POST.get('state')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')


        hiretuber = Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name,city=city,phone=phone,email=email,state=state,message=message,user_id=user_id)
        hiretuber.save()
        messages.success(request,'Thanks for reaching out!')
        return redirect ('youtubers')