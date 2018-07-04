from django import forms
from django.contrib.auth.models import User
from .models import *
class Reg_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    pic=forms.FileField()
    #image=forms.FileField(upload_to='image',null=True)
    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError("the two password fields did not match. ")
            return self.cleaned_data
    class Meta:
        model=User
        fields=['username','email','password','confirm_password','pic']
