from django.shortcuts import render  # type: ignore
from django.http import HttpResponse # type: ignore
from .forms import *
from .models import *
from django.core.mail import * # type: ignore
from django.shortcuts import render, redirect
from .models import Registration
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,"home.html")
def courses(request):
    return render(request,"courses.html")
def register(request):
    return render(request,"register.html")
def about(request):
    return render(request,"about.html")
def faq(request):
    return render(request,"faq.html")
def contact(request):
    return render(request,"contact.html")
def register_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        reg_email = request.POST.get('reg_email')
        reg_password=request.POST.get('reg_password')
        mobile = request.POST.get('mobile')
        course = request.POST.get('course')
        qualification = request.POST.get('qualification')
        college = request.POST.get('college')
        year = request.POST.get('year')
        location = request.POST.get('location')
        dob = request.POST.get('dob')

        reg_training_mode = request.POST.get('reg_training_mode')
        reg_training_location = request.POST.get('reg_training_location')
        reg_preferred_timings = ', '.join(request.POST.getlist('reg_preferred_timings'))
        
        reg_guardian_name = request.POST.get('reg_guardian_name')
        reg_guardian_occupation = request.POST.get('reg_guardian_occupation')
        reg_guardians_mobile = request.POST.get('reg_guardians_mobile')

        reg_address = request.POST.get('reg_address')
        reg_country = request.POST.get('reg_country')
        reg_state = request.POST.get('reg_state')
        reg_city = request.POST.get('reg_city')
        reg_zip = request.POST.get('reg_zip')

        message = request.POST.get('message')

        # Save registration data
        Registration.objects.create(
            name=name,
            reg_email=reg_email,
            reg_password=reg_password,
            mobile=mobile,
            course=course,
            qualification=qualification,
            college=college,
            year=year,
            location=location,
            dob=dob,
            reg_training_mode=reg_training_mode,
            reg_training_location=reg_training_location,
            reg_preferred_timings=reg_preferred_timings,
            reg_guardian_name=reg_guardian_name,
            reg_guardian_occupation=reg_guardian_occupation,
            reg_guardians_mobile=reg_guardians_mobile,
            reg_address=reg_address,
            reg_country=reg_country,
            reg_state=reg_state,
            reg_city=reg_city,
            reg_zip=reg_zip,
            message=message
        )

        # Optional: Send confirmation email
        
        
        
        try:
            send_mail(
                subject='Registration Confirmation',
                message=f"Hi {name},\n\nThank you for registering for the {course} course. We’ll contact you soon!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[reg_email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

        # Redirect to thank you page
        return redirect('thankyou')

    return render(request, 'register.html')

def thankyou(request):
    return render(request, 'thankyou.html')
def login(request):
    return render(request,'login.html')
#login
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Registration.objects.get(reg_email=email, reg_password=password)
            request.session['user_id'] = user.id  # Store session for profile
            return redirect('profile')
        except Registration.DoesNotExist:
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'login.html')
#profile

def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Not logged in

    user = get_object_or_404(Registration, id=user_id)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.reg_email = request.POST.get('reg_email')
        user.reg_password = request.POST.get('reg_password')  # Consider hashing in future
        user.mobile = request.POST.get('mobile')
        user.course = request.POST.get('course')
        user.qualification = request.POST.get('qualification')
        user.college = request.POST.get('college')
        user.year = request.POST.get('year')
        user.location = request.POST.get('location')
        user.dob = request.POST.get('dob')
        user.reg_training_mode = request.POST.get('reg_training_mode')
        user.reg_training_location = request.POST.get('reg_training_location')
        user.reg_preferred_timings = ', '.join(request.POST.getlist('reg_preferred_timings'))
        user.reg_guardian_name = request.POST.get('reg_guardian_name')
        user.reg_guardian_occupation = request.POST.get('reg_guardian_occupation')
        user.reg_guardians_mobile = request.POST.get('reg_guardians_mobile')
        user.reg_address = request.POST.get('reg_address')
        user.reg_country = request.POST.get('reg_country')
        user.reg_state = request.POST.get('reg_state')
        user.reg_city = request.POST.get('reg_city')
        user.reg_zip = request.POST.get('reg_zip')
        user.message = request.POST.get('message')

        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect('profile')

    return render(request, 'profile.html', {'user': user})

#delete
def delete_profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        Registration.objects.get(id=user_id).delete()
        request.session.flush()  # clear session
    return redirect('login')

#logout
def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    messages.success(request, "You have been logged out.")
    return redirect('login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

