from django.shortcuts import render
from .models import CustomSignupForm

def index(request):
	context = {
	'name' : "Aruviii",
	}
	return render(request,'app/index.html',context)

# def peopleSignup(request):
# 	form = CustomSignupForm()
# 	context = {
# 	'form':form,
# 	}
# 	if request.method == "POST":
# 		form = CustomSignupForm(request.POST)
# 		data = request.POST._mutable
# 		data = True 
# 		request.POST["is_owner"] = False
# 		print(request.POST)
# 		if form.is_valid():
# 			form.save(request)
# 	return render(request,'app/people_signup.html',context)