import random
from django.shortcuts import render # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.shortcuts import render ,redirect, get_object_or_404 # type: ignore
from django.contrib import messages # type: ignore
from django.conf import settings # type: ignore
from django.core.mail import send_mail # type: ig
from django.contrib.auth import authenticate, login as auth_login

from .models import Course

 
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
   
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Use alias to avoid conflict
            return redirect('home')
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})

    return render(request, 'login.html')
    
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Id = request.POST['ID']
        user = user.objects.create_user(username=username, email=email, password=password, id=Id)
        if user.object.filter(username=username).exit():
            return render(request,register.html,{"error:","user already exists"})
        if user.object.filter(email=email).exit():
            return render(request,register.html,{"error:","email already exists"})
        user.save()
        return render(request,register.html,{"success:","user created successfully"})
    return render(request,"registration.html")

def contact(request):
    return render(request,contact.html)

        
def send_otp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = user.objects.filter(email=email).first()

        if user:
            otp = str(random.randint(100000, 999999))  # Generate OTP
            request.session['otp'] = otp
            request.session['email'] = email

            # Send email
            send_mail(
                'Password Reset OTP',
                f'Your OTP is {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(request, 'OTP sent to your email.')
            return redirect('verify_otp')
        else:
            messages.error(request, 'Email not found')
            return redirect('forgot_password')

    return render(request, 'forgot_password.html')
    
def otp(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        if otp == entered_otp:
            return redirect('change_password.html')
        else:
            messages.error(request, 'Invalid OTP')
            return redirect('verify_otp.html')
        return render(request, 'otp.html')
    return render(request, 'otp.html')
    

def dashboard(request):
    return render(request, 'dashboard.html')
def contact(request):
    return render(request,'contact.html')
def course_detail(request):     
    course = get_object_or_404(Course)
    lessons = course.lesson_set.all()
    return render(request, 'course_detail.html', {
        'course': course,
        'lesson': lessons
    })