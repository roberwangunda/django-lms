from django.urls import path, include
from .views import send_sms
from .forms import MessageForm


urlpatterns=[
    path('_sms/', send_sms, name='bulksms'),
]