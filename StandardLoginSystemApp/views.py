from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from . mytokens import generate_token
from django.core.mail import EmailMessage
from MyShowcase import settings

def SLShome(request):
    return render(request,'sls/sls_home.html')
    #return render(request,'sls/sls_user_home.html')

def Login(request):
    if request.method=='POST':
        uid=request.POST['username']
        pawd=request.POST['password']
        usr=auth.authenticate(username=uid,password=pawd)
        if usr is not None:
            auth.login(request,usr)
            if usr.is_authenticated:
                return render(request,'sls/sls_user_home.html',{'usrname':usr.first_name+' '+usr.last_name})
        else:
            messages.error(request,'Invalid credentials')
            #return redirect('/sls/login')
            return render(request,'sls/sls_login.html')
    else:
        return render(request,'sls/sls_login.html')

def SignUp(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        cnfpwd=request.POST['cnfpassword']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        emailid=request.POST['emailid']
        NewUser=User.objects.create_user(username=uname,password=cnfpwd,first_name=fname,last_name=lname,email=emailid,is_active=False)
        NewUser.save()
        currentSite=get_current_site(request)
        emailSubject='Please verify your email account'
        emailMsg=render_to_string('sls/sls_email_verification.html',{
            'UserName': NewUser.first_name + ' '+ NewUser.last_name,
            'domain': currentSite.domain,
            'uid': urlsafe_base64_encode(force_bytes(NewUser.pk)),
            'token': generate_token.make_token(NewUser)
        })
        email=EmailMessage(emailSubject,emailMsg,settings.EMAIL_HOST_USER,[NewUser.email])
        email.fail_silently=False
        email.send()
        messages.success(request,'Your account has been successfully created. A verification email has been sent to your email id. Please check your email and verify it.')
        return redirect('slshome')
    else:
        return render(request,'sls/sls_signup.html')

def Verify(request,uidb64,token):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        usr=User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        usr=None
    if usr is not None and generate_token.check_token(usr,token):
        usr.is_active=True
        usr.save()
        return render(request,'sls/sls_verification_success.html',{'Uname': usr.first_name})
    else:
        return render(request,'sls/sls_verification_failed.html')

def Logout(request):
    auth.logout(request)
    return redirect('/sls/login')