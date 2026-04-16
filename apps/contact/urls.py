from django.urls import path
from .views import ContactPageView

urlpatterns = [
    path('contact-us/', ContactPageView.as_view(), name='contact-us'),
]
