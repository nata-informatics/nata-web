from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomNataUserForm(UserCreationForm):

	username = forms.CharField(
		max_length = 1024, 
		label = 'Username',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
	            'placeholder': 'Azharnanda',
	            'required': 'required',
	            'type': 'text',
			}
			)
		)

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

	email = forms.EmailField(
        label='Email',
        label_suffix='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email@email',
                'required': 'required',
                'type': 'email'
                }
            )
        )

	tanggal_lahir = forms.DateField(
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

	no_telp = forms.DecimalField(max_digits=13,
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

	password1 = forms.CharField(
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
	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'tanggal_lahir','no_telp', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'