from django.shortcuts import render
from django.views import View
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
        return render(request, 'contact.html')
    
class CollectorsView(View):

    def get(self, request):
        return render(request, 'collectors.html')