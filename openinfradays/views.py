from django.contrib.auth import login as user_login, logout as user_logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.utils.translation import ugettext as _
from .email import send_auth_email
from .models import ProgramCategory, AuthToken
from .forms import EmailLoginForm



def index(request):
    return render(request, 'index.html')


def schedule_page(request):
    return render(request, 'schedule.html')


class ProgramList(ListView):
    model = ProgramCategory
    template_name = "program.html"


def login(request):
    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Delete existed token
            AuthToken.objects.filter(email=email).delete()

            token = AuthToken(email=email)
            token.save()

            if send_auth_email(request, token):
                return render(request, 'login_sendmail.html')
            else:
                return render(request, 'login_sendmail_fail.html')
    return render(request, 'login.html', {
        'form': EmailLoginForm(),
        'title': _('Login'),
    })


def process_login(request, token):
    # Create user automatically by email as id, token as password
    email = 'asdf@naver.com'
    try:
        user = User.objects.get(email=email)
    except ObjectDoesNotExist:
        user = User.objects.create_user(email, email, 'testpassword')
        user.save()

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user_login(request, user)
    return redirect(reverse('index'))
