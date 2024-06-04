from django.urls import path

from . views import HomeView
from . views import AboutView
from . views import SolutionsView
from . views import ContactView
from . views import CollectorsView
from . import views
# my urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('solutions', SolutionsView.as_view(), name='solutions'),
    path('contact', ContactView.as_view(), name='contact'),
    path('collectors', CollectorsView.as_view(), name='collectors'),
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
]