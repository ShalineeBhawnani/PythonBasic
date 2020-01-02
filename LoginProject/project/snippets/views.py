from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmailSerializer,LoginSerializer, RegistrationSerializer, UserSerializer
from django.core.validators import validate_email


class Login(GenericAPIView):

    serializer_class = LoginSerializer

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse("Your account was active.")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Failed, Not the Registered username or password")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")

class Registrations(GenericAPIView):
   
    serializer_class = UserSerializer

    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):

        # pdb.set_trace()
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']


        smd = {
            'success': False,
            'message': "not registered yet",
            'data': [],
        }

        try:
            validate_email(email)
        except Exception as e:
            smd['message'] = "please enter vaild email address"
            logger.error("error: %s while as email entered was not a vaild email address", str(e))
            return HttpResponse(json.dumps(smd), status=400)

        # user input is checked
        if username == "" or email == "" or password == "":
            smd['message'] = "one of the details missing"
            logger.error("one of the details missing logging in")
            return HttpResponse(json.dumps(smd), status=400)

        # if email exists it will show error message
        elif User.objects.filter(email=email).exists():
            smd['message'] = "email address is already registered "
            logger.error("email address is already registered  while logging in")
            return HttpResponse(json.dumps(smd), status=400)

        else:
            try:
                user_created = User.objects.create_user(username=username, email=email, password=password,is_active=True)
                user_created.save()

                # user is unique then we will send token to his/her email for validation
                if user_created is not None:
                    token = token_activation(username, password)
                    url = str(token)
                    surl = get_surl(url)
                    z = surl.split("/")

                    mail_subject = "Activate your account by clicking below link"
                    mail_message = render_to_string('user/email_validation.html', {
                        'user': user_created.username,
                        'domain': get_current_site(request).domain,
                        'surl': z[2]
                    })
                    recipient_email = user_created.email
                    email = EmailMessage(mail_subject, mail_message, to=[recipient_email])
                    email.send()
                    smd = {
                        'success': True,
                        'message': 'please check the mail and click on the link  for validation',
                        'data': [token],
                    }
                    logger.info("email was sent to %s email address ", username)
                    return HttpResponse(json.dumps(smd), status=201)
            except Exception as e:
                smd["success"] = False
                smd["message"] = "username already taken"
                logger.error("error: %s while loging in ", str(e))
                return HttpResponse(json.dumps(smd), status=400)



# class Register(GenericAPIView):

#     serializer_class = RegistrationSerializer
    
#     def get(self, request):
#         return render(request, 'registration.html')
        
#     def post(self, request):
#         if request.method == 'POST':
#             form = UserCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 username = form.cleaned_data.get('username')
#                 raw_password = form.cleaned_data.get('password')
#                 user = authenticate(username=username, password=raw_password)
#                 login(request, user)
#                 return redirect('home')
#         else:
#             form = UserCreationForm()
#         return render(request, 'registration.html', {})
                    

