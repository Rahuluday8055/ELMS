from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random, string
from users.models import CustomUser

# Function to generate a random password
def generate_password(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

# Admin Dashboard View
@login_required
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

# Add Student View
@login_required
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

    return render(request, "add_student.html")
