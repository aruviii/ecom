from django.urls import path
from .views import (
	index ,
	myRequest,
	detail_view,
	owner_index,
	new_list,
	old_list,
	home
)
urlpatterns = [
	path('index/',index, name="index"),
	path('myreq/',myRequest, name="my_request"),
	path('dt_view/<int:id>/',detail_view,name='detail_view'),
	path('owner_index',owner_index , name ="owner_index"),
	path('new_list/',new_list, name="new_list"),
	path('old_list/',old_list, name="old_list"),
	# path('peoplesignup/',peopleSignup, name="people_signup")
]