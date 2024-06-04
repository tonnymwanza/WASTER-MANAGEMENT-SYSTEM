from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages

from . forms import RegisterForm
from . forms import ContactForm
from . models import Contact
from . models import Register
# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, 'index.html')
    
class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')
    
class SolutionsView(View):

    def get(self, request):
        return render(request, 'solutions.html')
    
class ContactView(View):

    def get(self, request):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_object = Contact.objects.create(
                name= form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                subject = form.cleaned_data['subject'],
                message = form.cleaned_data['message']
            )
            form = ContactForm()
            messages.info(request, 'Info send successfully')
        else:
            messages.error(request, 'problem sending info')
        return redirect('contact')
    
class CollectorsView(LoginRequiredMixin, View):

    def get(self, request):
        form = RegisterForm()
        context= {
            'form': form
        }
        return render(request, 'collectors.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST or None)
        register_object = None
        if form.is_valid():
            register_object = Register.objects.create(
                name = form.cleaned_data['name'],
                waste_sources = form.cleaned_data['waste_sources'],
                waste_collection = form.cleaned_data['waste_collection'],
                transportation = form.cleaned_data['transportation'],
                waste_separation = form.cleaned_data['waste_separation'],
                waste_treatment = form.cleaned_data['waste_treatement'],
                waste_disposal = form.cleaned_data['waste_disposal']
            )
            form = RegisterForm()
            messages.info(request, 'Information submitted successfully')
        else:
            messages.error(request, 'Error sending information')
        print(request.POST)
        context = {
            'form': form
        }
        context
        return redirect('collectors')
    
def register(request): # user registration
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'the username is in user. try another one')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'the email is in use. find another one')
                return redirect('user_register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                return redirect('signin')
        else:
            messages.error(request, 'ensure the passwords are matching')
            return redirect('register')
    return render(request, 'register.html')

def signin(request): # user login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('home')
        else:
            messages.error(request, 'invalid details provided. make sure the password or username is correct')
            return redirect('signin')
    return render(request, 'login.html')