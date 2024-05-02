from django import forms
from .models import Donor,Donation,Volunteer,DonationArea

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm

from django.contrib.auth import password_validation

class UserForm (UserCreationForm):

    password1 =forms.CharField(label='Password', widget=forms.PasswordInput (attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

    password2= forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput (attrs={'class': 'form-control', 'placeholder': 'Enter Password Again'}))

    class Meta:
        model=User

        fields=['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets={

        'first_name': forms. TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}), 
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),

        'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        'email':forms.EmailInput (attrs={'class': 'form-control', 'placeholder': 'Email ID'})
        }

class DonorSignupForm (forms.ModelForm):
            userpic = forms.ImageField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            class Meta:
                model= Donor
                fields=['contact', 'userpic', 'address']
                widgets={
                    'contact':forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Contact Number'}),
                     'address': forms.Textarea (attrs={'class':'form-control', 'placeholder': 'Full Address'})
                  }

class VolunteerSignupForm(forms.ModelForm):
        userpic = forms.ImageField(),
        idpic= forms.ImageField(),

        class Meta:
            model=Volunteer
            fields=['contact', 'userpic', 'idpic', 'address', 'aboutme']

            widgets={

                    'contact':forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'ContactNumber'}),

                    'address': forms.Textarea(attrs={'class': 'form-control','rows':4, 'placeholder': 'FullAddress'}),

                    'aboutme':forms.Textarea(attrs={ 'class': 'form-control', 'rows':4, 'placeholder': 'AboutMe'}),

                    "userpic": forms.FileInput(attrs= {'class': "form-control"}),

                    'idpic': forms.FileInput(attrs= {'class': 'form-control'}),

            }

            labels={
                "userpic": "User Picture",
                "idpic": "Id Prood Pure"

}


class LoginForm (AuthenticationForm):

        username= UsernameField(required=True, widget=forms.TextInput(attrs={'autofocus ': 'True','class': 'form-control', 'placeholder': 'Username'}))
        password= forms.CharField(required=True, widget= forms.PasswordInput (attrs={'class':'form-control', 'placeholder':'Password'}))



class MyPasswordChangeForm (PasswordChangeForm):

        old_password = forms.CharField(label="Old Password", strip=False, widget=forms.PasswordInput (attrs= {'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control', 'placeholder': 'Old  Password'})) 
        new_password1 =forms.CharField(label="New Password", strip=False, widget=forms.PasswordInput (attrs= {'autocomplete': ' new-password', 'class': 'form-control', 'placeholder': 'New Password'}),
        help_text=password_validation.password_validators_help_text_html())
        new_password2 = forms.CharField(label="Confirm New Password", strip=False, widget=forms.PasswordInput (attrs={'autocomplete':'new-password', 'class': 'form-control', 'placeholder': 'Confirm Password'}))



DONATION_CHOICES=(
    ('Food Donation', 'Food Donation'),
    ('Cloth Donation', 'Cloth Donation'),
    ('Footwear Donation', 'Footwear Donation'),
    ('Books Donation', 'Books Donation'),
    ('Furniture Donation', 'Furniture Donation'),
    ('Vessel Donation', 'Vessel Donation'),
    ('Other','Other'),
)
class DonateNowForm (forms.ModelForm):
             donationpic= forms. ImageField(),

             class Meta:
                model=Donation
                fields=['donationname', 'donationpic', 'collectionloc', 'description']

                widgets={

                    'donationname': forms.Select(choices=DONATION_CHOICES, attrs={'class': 'form-control'}), 'collectionloc': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Donation Collection Address'}),
                    'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (Special Note)'}),
                    'donationpic': forms.FileInput(attrs={'class': 'form-control'}),
                    }

                labels={
                        "donationpic": "Donation Image (Pic of Items u want to donate)",
                        "donationname": "Donation Name",
                        "collectionloc": "Donation Collection Address",
                        "description": "Description (Special Note)",
                }


class DonationAreaForm (forms.ModelForm):
     class Meta:
        model= DonationArea
        fields = ['areaname', 'description']
        widgets={

                'areaname':forms.TextInput(attrs={'class': "form-control", "placeholder": 'Donation Area'}), 
                "description":forms.Textarea(attrs={'class': "form-control", "placeholder": 'Description'})

                }

        labels={

                "areaname":"Donation Area Name",
                "description": "Description",
        }