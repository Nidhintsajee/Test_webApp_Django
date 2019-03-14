from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
	if request.session["profile_image"]:
		request.session["profile_image"] = request.session.get("profile_image")
	else:
		request.session["profile_image"] =''

	request.session.modified = True
	return render(request,'home.html')

def sign_up(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		phone_number = request.POST.get('phone_number')
		email = request.POST.get('email')
		dob = request.POST.get('dob')
		profile_image = request.FILES['profile_image']
		password = request.POST.get('password')
		print(first_name,last_name,phone_number,email,dob,profile_image,password)


		user = User.objects.create_user(
			first_name=first_name,last_name=last_name,
			username=phone_number,email=email,password=password
			)
		user=User_profile.objects.create(
			user=user,phone_number=phone_number,profile_image=profile_image,DOB=dob
			)
		return render(request,'login.html')
	else:
		return render(request,'signup.html')


def log_in(request):
	if request.method == 'POST':
		phone_number = request.POST.get('phone_number')
		password = request.POST.get('password')
		user= authenticate(username=phone_number,password=password)

		request.session["profile_image"] = User_profile.objects.get(user=user).profile_image.url
		request.session.modified = True

		if user:
			login(request,user)
			return render(request,'home.html')
		else:
			return render(request,'login.html')

	else:
		return render(request,'login.html')


def log_out(request):
	logout(request)
	return render(request,'home.html')


def about(request):
	return render(request,'about.html')