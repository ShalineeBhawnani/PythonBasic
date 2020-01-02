# ******************************************************************************************************************
# @purpose :will save user details after registrations.
# @file  :PrimeQueue.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmailSerializer,LoginSerializer, RegistrationSerializer, UserSerializer
#from django.core.validators import validate_email
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.http import HttpResponse, HttpResponseRedirect , response


def home(request):
   
    return render(request, 'login.html')

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
                return HttpResponse("Your account is active now.")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Failed, Not the Registered username or password")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")



class Registrations(GenericAPIView):

    serializer_class = RegistrationSerializer
    
    def get(self, request):
        return render(request, 'registration.html')
        
    def post(self, request):

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'registration.html', {})

def activate(request, surl):
    
    try:
        tokenobject = ShortURL.objects.get(surl=surl)
        token = tokenobject.lurl
        decode = jwt.decode(token, settings.SECRET_KEY)
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
    
    # except ExpiredSignatureError:
    #     messages.info(request, 'activation link expired')
    #     return redirect('registration')
    
    except Exception:
        messages.info(request, 'activation link expired')
        return redirect('registration')
                    