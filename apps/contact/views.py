from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from .models import Contact


def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            contact = form.save()

            # Gửi email
            send_mail(
                subject="Khách hàng liên hệ từ website",
                message=f"""
Tên: {contact.name}
SĐT: {contact.phone}
Email: {contact.email}

Địa chỉ: {contact.address}

Nội dung:
{contact.message}
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )

            messages.success(request, 'Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi sớm nhất.')

            return redirect('contact:success')

    else:
        form = ContactForm()

    context = {
        'form': form,
        'page_title': 'Liên hệ - Phế Liệu Thiệp Nhung',
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    return render(request, 'contact/success.html')