from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser

class NataUser(forms.Form):

    first_name = forms.CharField(
        max_length=20,
        label='First Name',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Azhar Difa',
                'required': 'required',
                'type': 'text',
                }
            )
        )

    last_name = forms.CharField(
        max_length=20,
        label='Last Name',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Arnanda',
                'required': 'required',
                'type': 'text',
                }
            )
        )
    
    date_of_birth = forms.DateField(
        label='Date of Birth',
        label_suffix='',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'required': 'required',
                'type': 'date'
                }
            )
        )
    
    phone_number = forms.DecimalField(
        max_digits=13,
        label='Phone Number',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '082115917XXX',
                'required': 'required',
                'type': 'text'
                }
            )
        )
    

    email = forms.EmailField(
        label='Email',
        label_suffix='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email',
                'required': 'required',
                'type': 'email'
                }
            )
        )
    
    password = forms.CharField(
        label='Password',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password',
                'required': 'required',
                'type': 'password'
                }
            )
        )
    
    password2 = forms.CharField(
        label='Confirmation Password',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'confirmation password',
                'required': 'required',
                'type': 'password'
                }
            )
        )

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        
        if len(data) > 20 :
            raise ValidationError(_('Too much character!'))

        return data

# class CustomNataUser(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = '__all__'