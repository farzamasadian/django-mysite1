from django.urls import path
from website.views import *


urlpatterns = [
    path('home', index_view),
    path('json-test', json_test)
]
