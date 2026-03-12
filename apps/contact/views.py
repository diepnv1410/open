from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
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