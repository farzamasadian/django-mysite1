from django.urls import path
from website.views import *

# Define the namespace for this app's URLs
app_name = 'website'

# URL patterns for the website app
urlpatterns = [
    path('', index_view, name='index'),       # Home page
    path('about/', about_view, name='about'), # About page
    path('contact/', contact_view, name='contact'), # Contact page
    path('test/', test_view, name='test'),
    path('newsletter/', newsletter_view, name='newsletter')
]
