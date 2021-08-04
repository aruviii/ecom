from django.shortcuts import render
from .models import CustomSignupForm
from .forms import IssueForm , CustomUser
import json
def index(request):
	form = IssueForm()
	user_info ={
	'user':request.user.email
	}
	dataJSON = json.dumps(user_info)
	context = {
	'title' : "Submit Issue",
	'form' : form,
	'user_email' : request.user.email,
	'user_address': request.user.address,
	'user_state': request.user.state,
	'user_district': request.user.district,
	'user_pincode': request.user.pincode
	}
	print(request.user.address)
	if request.method == "POST":
		form = IssueForm(request.POST)
		if form.is_valid :
			form.save()
			print(request.POST)
	return render(request,'app/index.html',context)