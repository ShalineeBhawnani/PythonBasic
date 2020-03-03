"""
 ******************************************************************************
 *  Purpose: Social login app is created where user can login using different
 *           service provider
 *  @file  :view.py
 *  @author :ShalineeBhawnani
 ******************************************************************************
"""

import datetime
import json
import django
import jwt
from django.template.loader import render_to_string
from validate_email import validate_email
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
 # from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.conf import setting
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from rest_framework.views import APIView
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from snippets.token import token_activation,token_validation,account_activation_token
from rest_framework.response import Response
from .serializers import EmailSerializer,LoginSerializer, RegistrationSerializer, UserSerializer
#from django.core.validators import validate_email
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.http import HttpResponse, HttpResponseRedirect , response
from jwt import ExpiredSignatureError
from mysite.settings import SECRET_KEY


class Login(GenericAPIView):

    serializer_class = LoginSerializer

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Failed, Not the Registered username or password")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")


class Logout(GenericAPIView):
    serializer_class = LoginSerializer

    def get(self, request):
        
        smd = {"success": False, "message": "not a vaild user", "data": []}
        try:
            user = request.user
            red.delete(user.username)
            smd = {"success": True, "message": " logged out", "data": []}
            logger.info("%s looged out succesfully ", user)
            return HttpResponse(json.dumps(smd), status=200)
        except Exception:
            logger.error("something went wrong while logging out")
            return HttpResponse(json.dumps(smd), status=400)

class Registrations(GenericAPIView):

    serializer_class = UserSerializer

    def get(self, request):
        return render(request, 'registration.html')
        
    def post(self, request, *args, **kwargs):        
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        smd = {
            'success': False,
            'message': "not registered yet",
            'data': [],
        }

        if username == "" or name == "" or email == "" or password1 == "" or password2 == "":
            messages.warning(request, "Fields cannot be empty")
        elif password1 != password2:
            messages.warning(request, "password fields not matching")

        try:
            validate_email(email)
        except validate_email.ValidationError as e:
            print('validate_email.ValidationError', e)
            messages.error(request, "Email id not valid")
            smd["success"] = False
            smd["message"] = "email"
            return HttpResponse(json.dumps(smd), status=400)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email id already registered")
            smd["success"] = False
            smd["message"] = "email exists occured"
            return HttpResponse(json.dumps(smd), status=400)

        if User.objects.filter(username=username).exists():
            messages.error(request, "username already taken")

        try:
            user_created = User.objects.create_user(username=username, email=email, 
                                                    password=password1,
                                                    is_active=False)
            
            user_created.save()
            # send_mail(subject, message, from_mail, to_list, fail_silently=True)
            sub = 'Thank you for registering'
            msg = 'Welcome to the Family'
            from_mail = "shalineebhawnani80@gmail.com"
            to_list = [user_created.email]
            send_mail(sub, msg, from_mail, to_list, fail_silently=True)
            print('welcome mail sent')
            current_site = get_current_site(request)
            domain = current_site.domain 
            print(current_site)
            print('domain:', domain)                
            token = token_activation(username, password1)
            print('return from tokens.py:', token)
            url = str(token)
            print('url is ',  url)
            surl = get_surl(url)
            print(surl)
            z = surl.split("/")
            print("the z value is", z)
            print("z[2] line printed :", z[2])
            mail_subject = "Activate your account clicking on the link below"
            message = render_to_string('email_validation.html', {
                    'user': user_created.username,
                    'domain': domain,
                    'surl': z[2]
                })
            print(message)
            email = EmailMessage(mail_subject, message, to=[email])
            email.send()

            # send_mail(mail_subject, message, from_mail, to_list, fail_silently=True)
            # message.send()
            print('confirmation mail sent')
            return HttpResponse('Please confirm your email address to complete the registration')

        except Exception as e:
            print('Exception', e)
            messages.error(request, "user creation failed")
            smd["success"] = False
            smd["message"] = "last return"
            return HttpResponse(json.dumps(smd), status=400)

class ForgotPassword(GenericAPIView):
    serializer_class = EmailSerializer
    def post(self, request):
        global response
        email = request.data["email"]
        response = {
            'success': False,
            'message': "not a vaild email ",
            'data': []
        }
      
        if email == "":
            response['message'] = 'email field is empty please provide vaild input'
            return HttpResponse(json.dumps(response), status=400)
        else:

            try:
                validate_email(email)
            except Exception:
                return HttpResponse(json.dumps(response) ,status=400)
            try:
                user = User.objects.filter(email=email)
                useremail = user.values()[0]["email"]
                username = user.values()[0]["username"]
                #id = user.values()[0]["id"]

                #  here user is not none then token is generated
                if useremail is not None:
                    token = token_activation(username, id)
                    url = str(token)
                    surl = get_surl(url)
                    z = surl.split("/")

                    # email is generated  where it is sent the email address entered in the form
                    mail_subject = "Activate your account by clicking below link"
                    mail_message = render_to_string('template/email_validation.html', {
                        'user': username,
                        #'domain': get_current_site(request).domain,
                        'surl': z[2]
                    })

                    recipientemail = email

                    ee.emit('send_email', recipientemail, mail_message)

                    response = {
                        'success': True,
                        'message': "check email for vaildation ",
                        'data': []
                    }
                    # here email is sent to user
                    return HttpResponse(json.dumps(response), status=201)
            except Exception as e:
                print(e)
                response['message'] = "something went wrong"
                return HttpResponse(json.dumps(response), status=400)

def activate(request, surl):
    print("Activate url is ", surl)   
    try:
        tokenobject = ShortURL.objects.get(surl=surl)
        token = tokenobject.lurl
        decode = jwt.decode(token, SECRET_KEY)
        username = decode['username']
        user = User.objects.get(username=username)
        if user is not None:
            user.is_active = True
            user.save()
            messages.info(request, "your account is active now")
            return redirect('login')        
        else:           
            messages.info(request, 'was not able to sent the email')          
            return redirect('registration')
    
    except KeyError:
        messages.info(request, 'was not able to sent the email')
        return redirect('registration')
     