from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage


from authentication.forms import RegistrationForm, LoginForm
from authentication.models import Account

from .utils import generate_token

def index(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'authentication/index.html', context)


def register_request(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)

            send_activation_email(user, request)

            messages.add_message(request, messages.SUCCESS,
                                 'We sent you an email to verify your account')
            return redirect('login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/register.html', context)

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                if not user.is_email_verified:
                    messages.add_message(request, messages.ERROR,
                                 'Email is not verified, please check your email inbox')
                    return render(request, 'registration/login.html')

                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.add_message(request, messages.ERROR,
                                 'Your account is disabled.')
                    return render(request, 'registration/login.html')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('password_reset/password_reset_mail.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(
        subject=email_subject, 
        body=email_body, 
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )

    email.send()

def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except:
        user = None
    
    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Email Verified')
        return render(request, 'registration/login.html')
    
    return render(request, 'registration/activate-failed.html', {"user": user})