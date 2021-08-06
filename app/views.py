from django.shortcuts import render , redirect
from .models import CustomSignupForm
from .forms import IssueForm , CustomUser
from .models import IssueModel
import json
from django.db import transaction
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'app/home.html')

@login_required(login_url='/accounts/login/')
def index(request):
	if request.user.is_owner:
		return redirect('owner_index')

	form = IssueForm(initial={'customer_name':request.user.id})
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
	'user_pincode': request.user.pincode,
	'is_owner':request.user.is_owner,
	}
	print(request.user.address)
	if request.method == "POST":
		form = IssueForm(request.POST)
		if form.is_valid :
			form.save()
			print(request.POST)
	return render(request,'app/index.html',context)

@login_required(login_url='/accounts/login/')
def myRequest(request):
	context = {
	'title' : "My Requests",
	"list" : IssueModel.objects.filter(customer_name=request.user)
	}
	return render(request,'app/my_request.html',context)

@login_required(login_url='/accounts/login/')
def detail_view(request,id):
	instance = IssueModel.objects.get(id=id)

	if instance.selected == False :
		selected_owner = ""
	else :
		selected_owner = CustomUser.objects.get(email=instance.owner_id)


	instance = IssueModel.objects.get(id=id)
	form = IssueForm(instance=instance)
	context = {
	'title' : "Detailed Issue",
	'detail':IssueModel.objects.get(id=id),
	'owners':CustomUser.objects.filter(is_owner=True,pincode=request.user.pincode),
	'form' : form,
	'selected_owner': selected_owner
	}

	if request.method == "POST":
		if request.POST.get("form_type") == 'formOne':
			instance.owner_id = ""
			instance.selected = False
			instance.save()
			return redirect('detail_view',id=id)
		elif request.POST.get("form_type") == 'formTwo':
			data = request.POST
			instance.owner_id=data["owner_id"]
			instance.selected = True
			instance.save()
			return redirect('detail_view',id=id)
	return render(request,'app/detail_view.html',context)

@login_required(login_url='/accounts/login/')
def owner_index(request):
	instance = IssueModel.objects.filter(selected=True,owner_id=request.user.email,picked=True)
	context = {
	'title' : "Working Orders",
	'picked_lists' : instance
	}
	if request.method == "POST":
		data = request.POST
		new_instance = IssueModel.objects.get(id=data['data_id'])
		new_instance.picked = False
		new_instance.save()
		return redirect('owner_index')

	return render(request,'app/owner_index.html',context)

@login_required(login_url='/accounts/login/')
def new_list(request):
	list_data = IssueModel.objects.filter(selected=True,owner_id=request.user.email,picked=False)
	context = {
	'title' : "New Orders",
	"list_datas" : list_data ,
	}

	if request.method == "POST":
		target_val = IssueModel.objects.get(id=request.POST['id'])
		target_val.picked = True
		target_val.save()
		return redirect('new_list')
	return render(request,'app/new_list.html',context)

@login_required(login_url='/accounts/login/')
def old_list(request):
	return render(request,'app/old_list.html',context)
