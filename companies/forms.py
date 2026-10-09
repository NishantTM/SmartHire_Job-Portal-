from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            
            "name",
            "logo",
            "description",
            "industry",
            "company_size",
            "founded_year",
            "website",
            "location",
            "contact_email",
            "contact_phone",
        ]
        
        
    widets = {
    "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Company Name"}),
    
    "logo":forms.ClearableFileInput(attrs={"class":"form-control"}),
    
    "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe your company...",
                }
            ),
     "industry": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Information Technology",
                }
            ),
    "company_size": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. 11-50 employees",
                }
            ),
  "founded_year": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. 2020",
                }
            ),

    "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),

    "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Kathmandu, Nepal",
                }
            ),
    

    "contact_email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "company@example.com",
                }
            ),

    "contact_phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+977 98XXXXXXXX",
                }
            ),


    
    }

