from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm


def contact(request):
    """
    A function to allow the user to submit an email
    """

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Your email has been sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, 'Failed to send email. Please ensure you have filled out the form correctly.')
    else:
        form = ContactForm()

    template = 'contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
