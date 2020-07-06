from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        sender_email = request.POST.get('sender-email', False)
        message = request.POST.get('message', False)
        # send mail

        response = send_mail(
            'from project site',  # subject
            message,  # message
            'gouthambolt@gamil.com',  # my mail
            [sender_email],  # to email
            fail_silently=False
        )
        messages.success(request, f"""You have successfully 
                        sent the message to {sender_email}.""")
        context = {'sender_email': sender_email, 'message': message}
        return render(request, 'intern/contact.html', context)
    else:
        return render(request, 'intern/contact.html')
