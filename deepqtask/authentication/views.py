from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages,auth

# Create your views here.

class UsernameValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'},status=400)
        if User.objects.filter(username = username).exists():
            return JsonResponse({'username_error':'this username already exists'},status=409)
        return JsonResponse({'username_valid': True})

class EmailValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'Invalid email'},status=400)
        if User.objects.filter(email = email).exists():
            return JsonResponse({'email_error':'this email already exists'},status=409)
        return JsonResponse({'email_valid': True})

class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username = username).exists() and not User.objects.filter(email = email).exists():
            if len(password)<6:
                messages.warning(request,"Password should be at least of 6 letters")
                return render(request,'authentication/register.html',context)
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            messages.success(request, "Account successfully created, now you can login")
            return render(request,'authentication/register.html')
            

        return render(request,'authentication/register.html')
    
class LoginView(View):
    def get(self, request):
        return render(request,'authentication/login.html')
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Welcome, ' + user.username + ' log in successful!')
                return redirect('services')

            messages.warning(request, 'Incorrect username/password, try again' )
            return render(request, 'authentication/login.html',context)
        
        messages.warning(request, 'Username does not exist, please create account' )
        return render(request, 'authentication/login.html')
    
class LogoutView(View):

    def post(self,request):
        auth.logout(request)
        messages.success(request,'Logout successful')
        return redirect('login')