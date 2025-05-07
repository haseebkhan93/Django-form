from django import forms 
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'email', 'age', 'gender', 'country']
        

def clean_email(self):
    
    email = self.cleaned_data.get("email")
    if  Info.objects.filter(email = email).exists():
        raise forms.ValidationError("This email already have submitted the form!")  
        
    return email 