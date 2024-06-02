from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages

from . forms import RegisterForm
from . forms import ContactForm
from . models import Contact
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
    
class CollectorsView(View):

    def get(self, request):
        form = RegisterForm()
        context= {
            'form': form
        }
        return render(request, 'collectors.html', context)