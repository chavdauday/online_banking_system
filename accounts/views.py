from http import server
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile
from .models import BankAccount
from .models import Transections
from datetime import datetime
import os
from django.contrib.auth.decorators import login_required
import random
from time import gmtime, strftime
# import smtplib
import ssl

# import accounts.models.py

# from django contrib.auth importlogin, authenticate, logout

# Create your views here.
from django.http import HttpResponse


# def error_404(request, exception):
#     return render(request, "error-404.html")

# def error(request):
#     return render(request, "error-404.html")

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST['password']
        
        user = auth.authenticate(username=uname, password=password)
        
        if user is not None:
            auth.login(request, user)
            subject = 'welcome to our Online Banking Syatem'
            message = f'Hi {user.username} you have logged in to your Online Banking System account. If not done by you then change your password and please contact our support team.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user.email, ]
            # send_mail( subject, message, email_from, recipient_list )
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

        if password1 != password2:
            messages.error("Passwords not matching")
    else:
        return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            
            if User.objects.filter(username=uname).exists():
                messages.error(request, "User name has already taken")
                return redirect('signup')


            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email  has already taken")
                return redirect('signup')

            else:
                # user = User.objects.create_user(username=uname, password=password1, email=email,first_name=fname, last_name=lname)
                # user.save()
                # messages.success(request, "User created successfully")
                # subject = 'welcome to our Online Banking Syatem'
                # message = f'Hi {user.username}, thank you for registering in our Online Banking Syatem.'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [user.email, ]
                # send_mail( subject, message, email_from, recipient_list )
                context = {
                    "username": uname,
                    "password": password1,
                    "email": email,
                    "first_name": fname,
                    "last_name": lname,
                }
                # return redirect('/')
                return render(request, 'completeProfile.html', context)
        
        else:
            messages.error(request, "Passwords not matching")
            return redirect('signup')
    else:
        return render(request, "sign-up.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def completeProfile(request):
    if request.method == "POST":
        # user = request.POST['user']
        uname = request.POST['uname']
        password1 = request.POST['password1']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        
        # profileimage = request.POST['profileimage']
        number = request.POST['number']
        dob = request.POST['dob']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        gender = request.POST['gender']
        
        media_root = settings.MEDIA_ROOT
        path = os.path.join(media_root, 'default.jpg')
        # pimage = request.FILES['pimage']
        # if 'profileimage' in request.FILES:
        #     if(os.path.exists(path)):
        #         os.remove(path)
        #     pimage = request.FILES['pimage']
        # else:
        #     pimage = path    


        
        user = User.objects.create_user(username=uname, password=password1, email=email,first_name=fname, last_name=lname)
        user.save()
        profile = Profile(user=user,Image="profile_images/default.jpg",mobile=number,dob=dob,address=address,country=country,city=city,gender=gender)
        profile.save()

        messages.success(request, "User created successfully")
        subject = 'Welcome To Our Online Banking Syatem'
        message = f'Hi {user.username}, thank you for registering in our Online Banking Syatem.'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [user.email, ]

    # # email(request):
    # port = settings.EMAIL_PORT
    # smtp_server = settings.EMAIL_HOST
    # sender_email = settings.EMAIL_HOST_USER
    # password = settings.EMAIL_HOST_PASSWORD
    # receiver_email = user.email
    # subject = 'Website registration'
    # body = 'Activate your account.'
    # message = 'Subject: {}\n\n{}'.format(subject, body)
    # context = ssl.create_default_context()
    # # with smtplib.SMTP(smtp_server, port) as server:
    #  # Can be omitted
    #     server.starttls(context=context)
    #     server.ehlo()  # Can be omitted
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message)
    # # return redirect('index')

        # send_mail( subject, message, email_from, recipient_list )




        return redirect('/')
        
    else:
        return render(request, "sign-up.html")

@login_required(login_url='login')  
def cancelUpdateProfile(request): 
    return redirect('profile')
 
@login_required(login_url='login')  
def updateProfile(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pNumber = request.POST['number']
        dob = request.POST['dob']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        gender = request.POST['gender']
        
        current_user = request.user
        user = User.objects.get(username=current_user)
        profile = Profile.objects.get(user_id=user.id)
        
        is_error = False
        if username != current_user.username:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User name has already taken")
                # is_error = True
                return redirect('profile')
            else:
                user.username = username
                

        if email != current_user.email:
            if User.objects.filter(email=email).exists():
                print("work")
                messages.error(request, "Email  has already taken")
                # is_error = True
                return redirect('profile')
            else:
                user.email = email
        
        # user.username = username
        # user.email = email
        user.first_name = fname
        user.last_name = lname
        user.save()

        media_root = settings.MEDIA_ROOT
        path = os.path.join(media_root, profile.Image.name)
        print(profile.Image.name)
        if 'pimage' in request.FILES:
            if profile.Image.name != "profile_images/default.jpg":
                if(os.path.exists(path)):
                    os.remove(path)
            profile.Image = request.FILES['pimage']
                    
        profile.user = user
        profile.mobile = pNumber
        profile.dob = dob
        profile.address = address
        profile.country = country
        profile.city = city
        profile.gender = gender
        profile.save() 
        
        messages.success(request, "Profile Updated successfully")
        return redirect('profile')
    else:
        return redirect('/')

@login_required(login_url='login')
def removePic(request):
    if(request.method == "GET"):
        
        current_user = request.user
        user = User.objects.get(username=current_user.username)
        profile = Profile.objects.get(user_id=user.id)
        
        media_root = settings.MEDIA_ROOT
        path = os.path.join(media_root,profile.Image.name)
        
        if profile.Image.name != "profile_images/default.jpg":
            if(os.path.exists(path)):
                os.remove(path)
                profile.Image = "profile_images/default.jpg"

        user.save()
        profile.save()
        
        messages.success(request, "Profile Image Removed Successfuly")
        return redirect('profile')
    
    else:
        return redirect('/')
    
    
@login_required(login_url='login')    
def createAccount(request):
    return render(request, "createAccount.html")

@login_required(login_url='login')
def createBankAccount(request):
    if request.method == "POST":
        balance = int(request.POST['ibalance'])
        acc_type = request.POST['acc_type']
        
        acc_number = random.randint(999999999,9999999999)
        num = random.randint(9999,99999)
        ifsc = "LUVIN" + str(num)
        # created_on = strftime("%Y-%m-%d", gmtime())
        current_user = request.user
        bank_account = BankAccount(user=current_user,account_type=acc_type,account_no=acc_number,IFSC_Code=ifsc,balance=balance,created_on=datetime.now())
        bank_account.save()
        messages.success(request, "Bank account created successfully")
        return render(request, "createAccount.html")
        # return redirect('myAccount')
    else:
        return redirect('/')
 
@login_required(login_url='login')   
def myAccount(request):
    current_user = request.user
    user = User.objects.get(username=current_user)
    bankAccounts = BankAccount.objects.filter(user_id=user.id)
    context = {'bankAccounts': bankAccounts}
    return render(request, "myAccount.html", context)

@login_required(login_url='login')
def fundTransfer(request):
    return render(request, "fundTransfer.html")

@login_required(login_url='login')
def transfer(request):
    if request.method == "POST":
        u_acc_no = request.POST['u_acc_no']
        amount = request.POST['amount']
        r_acc_no = request.POST['r_acc_no']
        ifsc = request.POST['ifsc']
        
        if u_acc_no == r_acc_no:
            messages.error(request, "You can't transfer to same account")
            return redirect('fundTransfer')
        
        if BankAccount.objects.filter(account_no=u_acc_no).exists():
            uaccount = BankAccount.objects.get(account_no=u_acc_no)
            if uaccount.user_id == request.user.id:
                if BankAccount.objects.filter(account_no=r_acc_no).exists():
                    raccount = BankAccount.objects.get(account_no=r_acc_no)
                    if raccount.IFSC_Code == ifsc:
                        if int(uaccount.balance) - int(amount) >= int(uaccount.Minimum_Balance):
                            uaccount.balance = int(uaccount.balance) - int(amount)
                            raccount.balance = int(raccount.balance) + int(amount)
                            uaccount.save()
                            raccount.save()
                            messages.success(request, "Fund transfered successfuly")
                            user = request.user
                            ruser = User.objects.get(id=raccount.user_id)
                            utransections = Transections(user=user,account_no=uaccount.account_no,amount=amount,balance_after_transaction=uaccount.balance,timestamp=datetime.now(),status="Debited")
                            utransections.save()
                            rtransections = Transections(user=ruser,account_no=raccount.account_no,amount=amount,balance_after_transaction=raccount.balance,timestamp=datetime.now(),status="Credited")
                            rtransections.save()
                            # user = request.user
                            subject = f'Debited {amount} Ruppess from your account'
                            message = f'Hi {user.username}, you have transfered {amount} Ruppess from your account having account number {uaccount.account_no}. Your current balance is {uaccount.balance} ruppess'
                            # email_from = settings.EMAIL_HOST_USER
                            # recipient_list = [user.email, ]
                            # send_mail( subject, message, email_from, recipient_list )
                            
                            # ruser = User.objects.get(id=raccount.user_id)
                            subject = f'Credited {amount} Ruppess to your account'
                            message = f'Hi {ruser.username}, you have recieved {amount} Ruppess to your account having account number {raccount.account_no}. Your current balance is {raccount.balance} ruppess'
                            # email_from = settings.EMAIL_HOST_USER
                            # recipient_list = [ruser.email, ]
                            # send_mail( subject, message, email_from, recipient_list )
                            
                            return redirect('fundTransfer')
                        else:
                            messages.error(request, "Insufficient Balance")
                            return redirect('fundTransfer')
                    else:
                        messages.error(request, "IFSC code is wrong")
                        return redirect('fundTransfer')
                else:
                    messages.error(request, "Recipients Account doesnt exist with this account number")
                    return redirect('fundTransfer')   
            else:
                messages.error(request, "This is not your account")
                return redirect('fundTransfer') 
        else:
            messages.error(request, "User Account doesnt exist with this account number")
            return redirect('fundTransfer')
    else:    
        return redirect('/')  

@login_required(login_url='login')
def myTransections(request):
    current_user = request.user
    transections = Transections.objects.filter(user_id=current_user.id,show_to_user=True)
    
    if not transections:
        messages.error(request, "No transections found")
        print("transections is null")
    context = {'transections': transections}
    return render(request, "myTransections.html", context)

@login_required(login_url='login')
def clearTransections(request):
    current_user = request.user
    transections = Transections.objects.filter(user_id=current_user.id)
    
    for transection in transections.iterator():
        transection.show_to_user = False
        transection.save()
    return redirect('myTransections')  

@login_required(login_url='login')
def deleteBankAccount(request, id):
    # if request.method == "POST":
    #     acc_id = request.POST['acc_id']
        bankAccount = BankAccount.objects.get(id=id)
        print(bankAccount.account_no)
        bankAccount.delete()
        messages.success(request, "Bank account deleted successfully")
        return redirect('myAccount')  
 
def deleteUserAccount(request):
    user = request.user
    user.delete()
    return redirect('/')  
# def forgotpassword(request):
#     if request.method == "POST":
#         uname = request.POST['uname']
        
#         if User.objects.filter(username=uname).exists():
#                 messages.success(request, "User name has already taken")
#                 # subject = 'Changing password'
#                 # message = f'Hi {user.username}, As we have recieved your request for changing the account password This is the link for changing the password.'
#                 # email_from = settings.EMAIL_HOST_USER
#                 # recipient_list = [user.email, ]
#                 # send_mail( subject, message, email_from, recipient_list )
#                 return redirect('forgot-password')
#         elif User.objects.filter(email=uname).exists(): 
#                 messages.success(request, "Email has already taken")
#                 return redirect('forgot-password')
#         else:
#                messages.error(request, "Username or Email not found")  
#                return redirect('forgot-password')  

#     else:    
#         return render(request, 'forgot-password.html') 

# def reset_password(request):
#     if request.method == "POST":
#         uname = request.POST['uname']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
        
#         if password1 == password2:
#             user = User.objects.get(username=uname)
#             user.set_password(password1)
#             user.save()
#             messages.success(request, "Password changed successfully")
#             return redirect('/')
#         else:
#             messages.error(request, "Passwords not matching")
#             return redirect('reset-password')
#     else:
#         return render(request, 'reset-password.html')



