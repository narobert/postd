from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
	
class UserForm(forms.Form):
    image = forms.ImageField()
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput, max_length=40)
	
    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(u'Username taken.')
