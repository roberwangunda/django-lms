from django.shortcuts import render
from .models import *
from .forms import MessageForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.decorators import method_decorator

from accounts.decorators import lecturer_required, student_required

User = settings.AUTH_USER_MODEL
def send_sms(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Message sent successfuly.')
        else:
            messages.error(request, f'Somthing is not correct, please write the message correctly.')
    else:
        form = MessageForm(request.POST)
    return render(request, "send_sms.html", {'form': form})

@login_required
def send_sms(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        title = request.POST.get('title')
        if form.is_valid():
            form.save()

            messages.success(request, (title + ' has been uploaded.'))
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = MessageForm()
    return render(request, 'send_sms.html', {
        'title': 'Add Post | DjangoSMS',
        'form': form,
    })