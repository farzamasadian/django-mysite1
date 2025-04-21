from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from website.models import Contact
from .forms import NameForm, ContactForm, NewsletterForm

# View for the home page (index.html)
def index_view(request):
    """
    Renders the main homepage of the website.
    """
    return render(request, 'website/index.html')

# View for the About page (about.html)
def about_view(request):
    """
    Renders the 'About Us' page.
    """
    return render(request, 'website/about.html')

# View for the Contact page (contact.html)
def contact_view(request):
    """
    Handle GET and POST requests for the contact page.
    - Displays a form for users to contact.
    - If submitted and valid, saves the data and redirects to the same page.
    """
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "Unknown"
            contact.save()
            messages.add_message(request=request, level=messages.SUCCESS, extra_tags='contact',message='Your ticket submitted successfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.add_message(request=request, level=messages.ERROR,extra_tags='contact', message='Your ticket didn\'t submit successfully')
            return render(request, 'website/contact.html', {'form':form})

    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

from django.shortcuts import redirect
from django.contrib import messages

def newsletter_view(request):
    """
    Handle newsletter form submissions from any page.
    - Keeps the user on the same page.
    """
    if request.method == 'POST':
        form = NewsletterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You subscribed successfully!', extra_tags='newsletter')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            error_message = "There was a problem with your subscription:"
            for field, errors in form.errors.items():
                for error in errors:
                    error_message += f" {field.capitalize()}: {error}"
            messages.error(request, error_message, extra_tags='newsletter-error')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect(request.META.get('HTTP_REFERER', '/'))

# View for the test page (test.html)
def test_view(request):
    """
    Renders a test template (used for development/testing purposes).

    Template:
        test.html
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = ContactForm()
            
    return render(request, 'test.html', {'form':form})


    