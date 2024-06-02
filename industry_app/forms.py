from django import forms

from . models import Contact
from . models import Register
# my forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'col-lg-12'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'col-lg-12'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'col-lg-24'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'text-msg', 'rows': 7}))

class RegisterForm(forms.Form):
    sources_of_choice = (
        ('residential', 'Residential'),
        ('industrial', 'Industrial'),
        ('commercial', 'Commercial'),
        ('institutional', 'Institutional')
    )
    types_of_wastes = (
        ('recyclable', 'Recyclable'),
        ('organic', 'Organic'),
        ('hazardous', 'Hazardous'),
        ('general waste', 'General waste')
    )
    waste_segregation = (
        ('recyclables', 'Recyclables'),
        ('organics', 'Organics'),
        ('non-recyclables', 'Non-recyclables')
    )
    treatment_methods = (
        ('anaerobic digestion', 'Anaerobic digestion'),
        ('pyrolysis', 'Pyrolysis'),
        ('waste-to-enery technologies', 'Waste-to-energy technologies')
    )
    disposal = (
        ('sanitary landfills', 'Sanitary landfills'),
        ('hazardous waste disposal', 'Hazardous waste disposal')
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the company or institution name'}))
    waste_sources = forms.CharField(widget=forms.RadioSelect(attrs={'placeholder': 'choose the source of waste'}, choices=sources_of_choice))
    waste_collection =forms.CharField(widget=forms.Select(attrs={'placeholder': 'select type of waste'}, choices=types_of_wastes))
    transportation = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the mode of transport'}))
    waste_separation = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Choose the method of waste separation'}, choices=waste_segregation))
    waste_treatment = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Choose treatment method'}, choices=treatment_methods))
    waste_disposal = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Choose method of disposal'}, choices=disposal))