from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, LoginForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import login, authenticate, logout
from home.views import home
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, smart_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(login_view)
        
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Sucessfull")
                return redirect(home)
            
            else:
                messages.error(request, "Authentication failed")
                return redirect(login_view)
            
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, "user/logout.html")

def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('user/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        form = CustomUserCreationForm()  
    return render(request, 'user/register.html', {'form': form})  

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        # Decode the user ID
        uid = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if user.is_active:
            return HttpResponse('User is already active.')
        user.is_active = True
        user.save()
        return HttpResponse("Thank you for confirmation. Now you cann login your account")
    else:
        return HttpResponse("Activation link is invalid")




def profile(request):
    return render (request, "user/profile.html")

def profile_update(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,  request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user_profile')

    else:
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()
        
    return render(request, "user/profile_update.html", {'u_form':u_form, 'p_form': p_form})

