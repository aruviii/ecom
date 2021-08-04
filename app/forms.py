from django import forms 
from .models import CustomUser,IssueModel

# class SecSignupForm(forms.ModelForm):
# 	class Meta:
# 		model = CustomUser
# 		fields = ['email','username','phone','address','password1','password2']
class IssueForm(forms.ModelForm):
	class Meta:
		model = IssueModel
		fields = ['issue','customer_name','address','state','district','pincode']