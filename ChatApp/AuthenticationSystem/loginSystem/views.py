from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmailSerializer,LoginSerializer, RegistrationSerializer
def registration(request):
    
    return render(request,'registration.html',{})


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


class Register(GenericAPIView):

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
                    

                

# class Registration(GenericAPIView):
    
#     serializer_class = ResgistrationSerializer
    
#     def get(self, request):
#         return render(request, 'users/registration.html')
    
#     def post(self, request, *args, **kwargs):        
#         name = request.POST.get('name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')

#         smd = {
#             'success': False,
#             'message': "not registered yet",
#             'data': [],
#         }

#         if username == "" or name == "" or email == "" or password1 == "" or password2 == "":
#             messages.warning(request, "Fields cannot be empty")
#         elif password1 != password2:
#             messages.warning(request, "password fields not matching")

#         try:
#             validate_email(email)
#         except validate_email.ValidationError:
#             messages.error(request, "Email id not valid")
#             smd["success"] = False
#             smd["message"] = "email"
#             return HttpResponse(json.dumps(smd), status=400)
        
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email id already registered")
#             smd["success"] = False
#             smd["message"] = "email exists occured"
#             return HttpResponse(json.dumps(smd), status=400)

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "username already taken")

#         try:
#             user_created = User.objects.create_user(username=username, email=email, 
#                                                     password=password1,
#                                                     is_active=False)
            
#             user_created.save()
#             # send_mail(subject, message, from_mail, to_list, fail_silently=True)
#             sub = 'Thank you for registering with fundoo notes'
#             msg = 'U can do lot many things with fundoo like create notes, set remainders and ../n Have FunDooing'
#             from_mail = 'fundoonotes27@gmail.com'
#             to_list = [user_created.email]
#             send_mail(sub, msg, from_mail, to_list, fail_silently=True)
#             print('welcome mail sent')
#             current_site = get_current_site(request)
#             domain = current_site.domain 
#             print(current_site)
#             print('domain:', domain)                
#             token = activation_token(username, password1)
#             print('return from tokens.py, z:', token)
#             mail_subject = "Activate your account clicking on the link below"
#             message = render_to_string('users/email_validation.html', {
#                     'user': user_created.username,
#                     'domain': domain,
#                     'surl': token
#                 })
#             send_mail(mail_subject, message, from_mail, to_list, fail_silently=True)
#             print('confirmation mail sent')
#             return HttpResponse('Please confirm your email address to complete the registration')

#         except Exception as e:
#             messages.error(request, "user creation failed")
#             smd["success"] = False
#             smd["message"] = "last return"
#             return HttpResponse(json.dumps(smd), status=400)

# def activate(request, surl):
#     try:
#         tokenobject = ShortURL.objects.get(surl=surl)
#         token = tokenobject.lurl
#         decode = jwt.decode(token, SECRET_KEY)
#         username = decode['username']
#         user = User.objects.get(username=username)

#         # if user is not none then user account willed be activated
#         if user is not None:
#             user.is_active = True
#             user.is_staff = True
#             user.save()
#             messages.info(request, "your account is active now")
#             return redirect('/login')
#         else:
#             messages.info(request, 'was not able to sent the email')
#             return redirect('/registration')
#     except KeyError:
#         messages.info(request, 'was not able to sent the email')
#         return redirect('/registration')
#     except ExpiredSignatureError:
#         messages.info(request, 'activation link expired')
#         return redirect('/registration')
#     except Exception:
#         messages.info(request, 'activation link expired')
#         return redirect('/registration')

# class ForgotPassword(GenericAPIView):
    
#     serializer_class = EmailSerializer

#     def get(self, request):
#         return render(request, 'users/forgotpassword.html')

#     def post(self, request):

#         email = request.POST.get('email')
#         global response
#         response = {
#             'success': False,
#             'message': "not a vaild email ",
#             'data': []
#         }

#         if email == "":
#             response['message'] = 'email field cannot be empty'
#             return HttpResponse(json.dumps(response), status=400)
        
#         else:
#             try:
#                 validate_email(email)
#             except Exception:
#                 return HttpResponse(json.dumps(response) ,status=400)
        
#             try:
#                 user = User.objects.filter(email=email)
#                 username = user.values()[0]["username"]
#                 useremail = user.values()[0]["email"]
#                 id = user.values()[0]["id"]

#                 if useremail is not None:
#                     current_site = get_current_site(request)
#                     domain = current_site.domain
#                     print(domain)
#                     from_mail = 'fundoonotes27@gmail.com'
#                     to_list = [useremail]

#                     token = activation_token(username, id)
#                     print('return from tokens.py, z:', token)
                    
#                     mail_subject = "Reset your password clicking on the link below"
#                     message = render_to_string('users/reset_mail.html', {
#                             'user': username,
#                             'domain': domain,
#                             'surl': token
#                         })
#                     send_mail(mail_subject, message, from_mail, to_list, fail_silently=True)
#                     print('Reset password mail sent')
#                     response['message'] = 'reset password link has been sent to your account'
#                     return HttpResponse(json.dumps(response), status=201)
#             except Exception as e:
#                 print(e)
#                 response['message'] = "something went wrong"
#                 return HttpResponse(json.dumps(response), status=400)

# def reset_Password(request, surl):
#     try:
#         tokenObject = ShortURL.objects.get(surl=surl)
#         print(tokenObject)
#         token = tokenObject.lurl
#         decode = jwt.decode(token, SECRET_KEY)
#         username = decode['username']
#         user = User.objects.get(username=username)

#         if user is not None:
#             context = {'userReset': user.username}
#             print(context)
#             return redirect('/resetpassword/'+str(user))

#         else:
#             messages.info(request, "failed to send the email")
#             return redirect('/forgotpassword')
#     except KeyError:
#         messages.info(request, "failed to send the email")
#         return redirect('/forgotpassword')

#     except Exception as e:
#         print(e)
#         messages.info(request, 'actiavtion link expired')
#         return redirect('/forgotpassword')

# class ResetPassword(GenericAPIView):

#     serializer_class = ResetPasswordSerializer

#     def get(self, request, user_reset):
#         return render(request, 'users/reset_password.html')

#     def post(self, request, user_reset):

#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         smd = {
#             'success': False,
#             'message': 'password reset not done',
#             'data': [],
#         }

#         if user_reset is None:
#             smd['message'] = 'not a vaild user'
#             return HttpResponse(json.dumps(smd), status=404)

#         elif password1 == "" or password2 == "":
#             smd['message'] = 'fill in the password field'
#             return HttpResponse(json.dumps(smd), status=400)
        
#         elif password1 != password2:
#             smd['message'] = 'password fields did not match'
#             return HttpResponse(json.dumps(smd), status=400)

#         else:
#             try:
#                 user = User.objects.get(username=user_reset)
#                 user.set_password(password1)
#                 user.is_active = True
#                 user.save()
#                 smd = {
#                     'success': True,
#                     'message': 'password reset done',
#                     'data': [],
#                 }
#                 # return HttpResponse(json.dumps(smd), status=201)
#                 return render(request,'users/login.html')

#             except Exception as e:
#                 print(e)
#                 smd['message'] = 'not a valid user'
#                 return HttpResponse(json.dumps(smd), status=400)