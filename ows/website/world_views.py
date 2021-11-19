from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import worldsForm
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import worlds 


def create(request):
    context ={}
    form = worldsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(
        request,
        'website/world/create.html', context
    )

