from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('completeProfile', views.completeProfile, name='completeProfile'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('removePic', views.removePic, name='removePic'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('cancelUpdateProfile', views.cancelUpdateProfile, name='cancelUpdateProfile'),
    path('createBankAccount', views.createBankAccount, name='createBankAccount'),
    path('deleteBankAccount/<int:id>', views.deleteBankAccount, name='deleteBankAccount'),
    path('myAccount', views.myAccount, name='myAccount'),
    path('fundTransfer', views.fundTransfer, name='fundTransfer'),
    path('transfer', views.transfer, name='transfer'),
    path('myTransections', views.myTransections, name='myTransections'),
    path('clearTransections', views.clearTransections, name='clearTransections'),
    path('deleteUserAccount', views.deleteUserAccount, name='deleteUserAccount'),

    # path('forgot-password', views.forgotpassword, name='forgot-password'),
    # path('reset-password', views.reset_password, name='forgot-password'),
    # path('error', views.error, name='error')
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    #  auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
    auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
]