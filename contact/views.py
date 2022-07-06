from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm


# Credit -> https://learndjango.com/tutorials/django-email-contact-form
def contact(request):
    """View to render contact page"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = [settings.EMAIL_HOST_USER,]
            try:
                send_mail(subject, message, email, ['lauraljones19@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, 'There was a problem sending your message. \
                    Please try again.')
    return render(request, "contact.html", {'form': form})

