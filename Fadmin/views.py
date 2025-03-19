from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random, string
from users.models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# admin login In view
def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(f"Trying to authenticate: {email} with password: {password}")


        user = authenticate(request, username=email, password=password)  # Use email as username

        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  # Change 'dashboard' to your desired page
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'admin_login1.html')

# admin logout view
@login_required
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


# Function to generate a random password
def generate_password(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

# Admin Dashboard View

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

# Add Student View

def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = generate_password()

        # Create student user
        student = CustomUser.objects.create_user(email=email, name=name, role="student", password=password)

        # Send email with login details
        send_mail(
            subject="Welcome to LMS - Your Login Credentials",
            message=f"Hello {name},\n\nYour account has been created.\n\nEmail: {email}\nPassword: {password}\n\nPlease log in and change your password.\n\nBest,\nLMS Team",
            from_email="your-email@gmail.com",  # Replace with your email
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect("admin_dashboard")

    return render(request, "add_student1.html")
