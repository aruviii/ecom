from django.shortcuts import render


def index(request):
	context = {
	'name' : "Aruviii",
	}
	return render(request,'app/index.html',context)
