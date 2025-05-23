from django import forms
from captcha.fields import CaptchaField
from website.models import Contact, Newsletter

class NameForm(forms.Form):
    """
    A simple form not connected to any database model.
    Used for collecting contact information through plain form fields.
    """

    # The name of the person submitting the form
    name = forms.CharField(max_length=255)

    # The email address of the sender
    email = forms.EmailField()

    # The subject of the message
    subject = forms.CharField(max_length=255)

    # The message content itself, displayed as a larger text area
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    """
    A Django ModelForm based on the Contact model.
    Automatically creates fields based on the model definition.
    Useful for rendering forms tied directly to the database.
    """
    captcha = CaptchaField()

    class Meta:
        model = Contact  # The model associated with this form
        fields = '__all__'  # Include all fields from the model

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        if Newsletter.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already subscribed.")
        return email