from django.shortcuts import render , redirect
from .models import CustomSignupForm
from .forms import IssueForm , CustomUser
from .models import IssueModel
import json


def index(request):
	if request.user.is_owner:
		return redirect('owner_index')
		
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

def myRequest(request):
	context = {
	"list" : IssueModel.objects.filter(customer_name=request.user)
	}
	return render(request,'app/my_request.html',context)

def detail_view(request,id):
	instance = IssueModel.objects.get(id=id)
	form = IssueForm(instance=instance)
	context = {
	'detail':IssueModel.objects.get(id=id),
	'owners':CustomUser.objects.filter(is_owner=True,pincode=request.user.pincode),
	'form' : form
	}
	
	if request.method == "POST" :
		data = request.POST
		instance.owner_id=data["owner_id"]
		instance.selected = True
		instance.save()
		print(data["owner_id"])

		# instance.update()

	return render(request,'app/detail_view.html',context)


def owner_index(request):
	context = {
	
	}
	return render(request,'app/owner_index.html',context)

def new_list(request):
	list_data = IssueModel.objects.filter(selected=True,owner_id=request.user.email)
	context = {
	"list_datas" : list_data ,
	}
	return render(request,'app/new_list.html',context)

def old_list(request):

	return render(request,'app/old_list.html',context)