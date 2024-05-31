from django.urls import path

from . views import HomeView
from . views import AboutView
from . views import SolutionsView
from . views import ContactView
# my urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('solutions', SolutionsView.as_view(), name='solutions'),
    path('contact', ContactView.as_view(), name='contact'),
]