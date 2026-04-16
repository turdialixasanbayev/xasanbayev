from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from .models import ContactUS

class ContactPageView(View):
    def get(self, request):
        return render(request, 'contact-us.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message')

        if name and email and message:
            ContactUS.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message,
            )
            messages.success(request, "Xabaringiz qabul qilindi. Tez orada ko'rib chiqamiz.")
            return redirect('contact-us')
        messages.error(request, "Iltimos, barcha majburiy maydonlarni to'ldiring.")
        return redirect('contact-us')
