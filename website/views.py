from django.shortcuts import render
from django.http import HttpResponse
from website.models import Contact
from .forms import NameForm, ContactForm

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
    Renders the 'Contact Us' page.
    """
    return render(request, 'website/contact.html')

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