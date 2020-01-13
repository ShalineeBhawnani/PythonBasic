import datetime
import json
import django
import jwt
from django.template.loader import render_to_string
from pyee import BaseEventEmitter 
from pymitter import EventEmitter
from lib.emitter import ee
from validate_email import validate_email
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
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
from project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from snippets.token import token_activation
from rest_framework.response import Response
from .serializers import EmailSerializer,LoginSerializer, RegistrationSerializer, UserSerializer,ResetPasswordSerializer
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.http import HttpResponse, HttpResponseRedirect , response
from jwt import ExpiredSignatureError
from project.settings import SECRET_KEY

# def home(request):
   
#     return render(request, 'login.html')

class Login(GenericAPIView):

    serializer_class = LoginSerializer

    def get(self, request):
        return render(request, 'user/index.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('chats')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Failed, Not the Registered username or password")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")



class Registrations(GenericAPIView):

    serializer_class = UserSerializer

    def get(self, request):
        return render(request, 'user/registration.html')
        
    def post(self, request):        
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        smd = {
            'success': False,
            'message': "not registered yet",
            'data': [],
        }

        if username == "" or name == "" or email == "" or password == "" or password2 == "":
            messages.warning(request, "Fields cannot be empty")
        elif password != password2:
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
                                                    password=password,
                                                    is_active=False)
            
            user_created.save()

            sub = 'Thank you for registering'
            msg = 'Welcome to the Family'
            from_mail = "kour.gursheesh281@gmail.com"
            to_list = [user_created.email]
            send_mail(sub, msg, from_mail, to_list, fail_silently=True)
            print('welcome mail sent')
            current_site = get_current_site(request)
            domain = current_site.domain 
            print(current_site)
            print('domain:', domain)                
            token = token_activation(username, password)
            print('return from tokens.py:', token)
            url = str(token)
            print('url is ',  url)
            surl = get_surl(url)
            print(surl)
            z = surl.split("/")
            print("the z value is", z)
            print("z[2] line printed :", z[2])
            mail_subject = "Activate your account clicking on the link below"
            message = render_to_string('user/email_validation.html', {
                    'user': user_created.username,
                    'domain': domain,
                    'surl': z[2]
                })
            print(message)
            email = EmailMessage(mail_subject, message, to=[email])
            email.send()


            print('confirmation mail sent')
            return HttpResponse('Please confirm your email address to complete the registration')

        except Exception as e:
            print('Exception', e)
            messages.error(request, "user creation failed")
            smd["success"] = False
            smd["message"] = "last return"
            return HttpResponse(json.dumps(smd), status=400)

# class Logout(GenericAPIView):
#     serializer_class = LoginSerializer

#     def get(self, request):
     
#         smd = {
#             "success": False,            
#             "message": "not a vaild user", 
#             "data": []
#             }

#         try:
#             user = request.user
#             red.delete(user.username)
#             smd = {"success": True, "message": " logged out", "data": []}
#             return HttpResponse(json.dumps(smd), status=200)
#         except Exception:
#             return HttpResponse(json.dumps(smd), status=400)

class ForgotPassword(GenericAPIView):
 
    serializer_class = EmailSerializer

    def get(self, request):
        return render(request,'user/forgot_password.html')

    def post(self, request):

        global response
        email = request.data["email"]
        smd = {
            'success': False,
            'message': "not a vaild email ",
            'data': []
        }
        try:
            if email == "":
                response = 'email field is empty please provide vaild input'
            else:

                try:
                    validate_email(email)
                except Exception:
                    return HttpResponse(json.dumps(smd))
                try:
                    print(email)
                    user = User.objects.filter(email=email)
                    useremail = user.values()[0]["email"]
                    username = user.values()[0]["username"]
                    id = user.values()[0]["id"]

                    if useremail is not None:
                        token = token_activation(username, id)
                        url = str(token)
                        surl = get_surl(url)
                        z = surl.split("/")

                        mail_subject = "Activate your account by clicking below link"
                        mail_message = render_to_string('user/reset_password_token.html', {
                            'user': username,
                            'domain': get_current_site(request).domain,
                            'surl': z[2]
                        })
                        recipientemail = email
                        
                        email = EmailMessage(mail_subject, mail_message, to=[recipientemail])
                        email.send()
                        response = {
                            'success': True,
                            'message': "check email for vaildation ",
                            'data': []
                        }

                except Exception as e:
                    response = smd['message'] = "not a registered user",
        except Exception:
            smd['message'] = "not a registered user",

        return HttpResponse(json.dumps(response))


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
            return redirect('index')        
        else:           
            messages.info(request, 'was not able to sent the email')          
            return redirect('user/registration')
    

    except KeyError:
        messages.info(request, 'was not able to sent the email')
        return redirect('user/registration')
     
    
def reset_password(request, surl):
    
    try:

        tokenobject = ShortURL.objects.get(surl=surl)
        token = tokenobject.lurl
        decode = jwt.decode(token, settings.SECRET_KEY)
        username = decode['username']
        user = User.objects.get(username=username)

        if user is not None:
            context = {'reset_password': user.username}
            print(context)
            return redirect('user/reset_password' + str(user))
        else:
            messages.info(request, 'was not able to sent the email')
            return redirect('user/forgot_password')
    except KeyError:
        messages.info(request, 'was not able to sent the email')
        return redirect('user/forgot_password')
    except Exception as e:
        print(e)
        messages.info(request, 'activation link expired')
        return redirect('user/forgot_password')


class ResetPassword(GenericAPIView):
    
    serializer_class = ResetPasswordSerializer


    def post(self, request, user_reset):
        password = request.data['password']


        smd = {
            'success': False,
            'message': 'password reset not done',
            'data': [],
        }
        if user_reset is None:
            smd['message'] = 'not a vaild user'
            return HttpResponse(json.dumps(smd), status=404)

        elif password == "":
            smd['message'] = 'one of the fields are empty'
            return HttpResponse(json.dumps(smd), status=400)

        elif len(password) <= 4:
            smd['message'] = 'password should be 4 or  more than 4 character'
            return HttpResponse(json.dumps(smd), status=400)

        else:
            try:

                user = User.objects.get(username=user_reset)
                user.set_password(password)
                user.save()

                smd = {
                    'success': True,
                    'message': 'password reset done',
                    'data': [],
                }
                return HttpResponse(json.dumps(smd), status=201)
            except User.DoesNotExist:
                smd['message'] = 'not a vaild user '
                return HttpResponse(json.dumps(smd), status=400)


def session(request):
  
    return render(request, 'user/session.html')