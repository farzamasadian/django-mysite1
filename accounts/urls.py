from django.urls import path, include
from accounts.views import *


# Define the namespace for this app's URLs
app_name = 'accounts'

# URL patterns for the website app
urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup')
]
