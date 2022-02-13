from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
import datetime
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from scandata.models import Data
from scandata.forms import DataCreationForm
# from request.forms import CommentForm

def dashboard(request):
	
	'''
	Summary of all apps - display here with charts etc.
	eg.lEAVE - PENDING|APPROVED|RECENT|REJECTED - TOTAL THIS MONTH or NEXT MONTH
	EMPLOYEE - TOTAL | GENDER 
	CHART - AVERAGE EMPLOYEE AGES
	'''
	dataset = dict()
	user = request.user

	if not request.user.is_authenticated:
		return redirect('accounts:login')
	staff_requests = Data.objects.filter(user = user)

	dataset['staff_requests'] = staff_requests

	return render(request,'dashboard/dashboard_index.html',dataset)

def data_creation(request):
	if not request.user.is_authenticated:
		return redirect('accounts:login')
	if request.method == 'POST':
		form = DataCreationForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			user = request.user
			instance.user = user
			instance.save()


			# print(instance.defaultdays)
			messages.success(request,'DATA SAVED!',extra_tags = 'alert alert-success alert-dismissible show')
			return redirect('dashboard:createdata')

		messages.error(request,'UNABLE TO SAVE DATA!!!',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('dashboard:createdata')


	dataset = dict()
	form = DataCreationForm()
	dataset['form'] = form
	dataset['title'] = 'Scan Data'
	return render(request,'dashboard/create_data.html',dataset)

def view_my_data_table(request):
	# work on the logics
	if request.user.is_authenticated:
		user = request.user
		datas = Data.objects.filter(user = user)
	#	employee = Employee.objects.filter(user = user).first()
		print(datas)
		dataset = dict()
		dataset['data_list'] = datas
	#	dataset['employee'] = employee
		dataset['title'] = 'Datas List'
	else:
		return redirect('accounts:login')
	return render(request,'dashboard/staff_datas_table.html',dataset)

