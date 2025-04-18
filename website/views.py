from django.shortcuts import render
from django.http import HttpResponse

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
