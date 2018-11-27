from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == "POST":
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    company = request.POST['company']
    message = request.POST['message']
    user_id = request.POST['user_id']
    
    contact = Contact(name=name, email=email, phone=phone, message=message, user_id=user_id)

    contact.save()

    # Send mail
    send_mail(
      'Potential Client Inquiry!',
      'There has been an inquiry from: ' + name + ' of Company: ' + company,
      'filioarturo@gmail.com',
      ['filioarturo@gmail.com'],
      fail_silently = False
    )

    messages.success(request, 'Your request has been submitted, we will get back to you shortly')
    return redirect('/contact')