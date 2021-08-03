from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.forms import SignupForm
from django import forms

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,blank=False,null=False)
    address = models.TextField(max_length=300,blank=False,null=False)
    state = models.CharField(max_length=100,blank=False , null = False)
    district = models.CharField(max_length=200, blank=False , null = False)
    pincode = models.CharField(max_length=200,blank = True , null = True)
    is_owner = models.BooleanField(blank = True , null = True)

class CustomSignupForm(SignupForm):
    phone = forms.CharField()
    company_name = forms.CharField(required=False)
    address = forms.CharField(widget=forms.Textarea)
    state = forms.CharField()
    district = forms.CharField()
    pincode = forms.CharField()
    is_owner = forms.BooleanField(initial=False,required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.state = self.cleaned_data['state']
        user.district = self.cleaned_data['district']
        user.pincode = self.cleaned_data['pincode']
        user.is_owner = self.cleaned_data['is_owner']
        user.company_name = self.cleaned_data['company_name']
        user.save()
        return user
