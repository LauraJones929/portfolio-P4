from django import forms
from .models import Contact

class ContactForm(forms.Form):
    """
    Contact form to collect user queries
    """

    # class Meta:
    #     """ Set fields from Contact model """
    #     model = Contact
    #     fields = ('name', 'email', 'subject', 'message',)
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(widget=forms.EmailInput(), label='Email Address', required=True)
    subject = forms.CharField(label='Subject', max_length=100, required=True)
    message = forms.CharField(label='Message', max_length=300, widget=forms.Textarea(), required=True)