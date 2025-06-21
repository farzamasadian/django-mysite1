from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that includes a required email field
    and validates that the email is unique.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # This correctly uses the parent form's default fields ('username', 'password', 'password2')
        # and adds our 'email' field to them.
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # This is optional, it just adds a CSS class to the username input
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        """
        Verify that the email is unique in a case-insensitive way.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("A user with this email address already exists.")
        return email