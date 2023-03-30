from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.conf import settings
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail

# Create your views here.
from django.http import HttpResponse

@login_required(login_url='login')
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html")

@login_required(login_url='login')
def about(request):
    return render(request, "about.html")

from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        subject = request.POST['msg_subject']
        message = request.POST['message']
        mymessage = f" Name : {name} \n Email : {email} \n Phonen Number : {phone_number} \n Subject : {subject} \n Message : {message}"
        recipient_list = [request.user.email, ]
        messages.success(request, 'Message Sent Successfully')
        email_from = email
        recipient_list = ['dduprojects12@gmail.com', ]
        send_mail( 'Customer Contact', mymessage, email_from, recipient_list )

        return redirect('contact')
    else:
        return render(request, "contact.html")
    
    
@login_required(login_url='login')
def profile(request):
    return render(request, "profile.html")