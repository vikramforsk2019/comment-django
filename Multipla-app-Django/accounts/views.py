from dietapp.post_upload import post_upload
from dietapp.profile_upload import profile_upload  #file upload
from django.shortcuts import render  
from django.template import loader  
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
from .models import Signup 
from dietapp.models import Health_data
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
@csrf_exempt
def signin(request):
	if request.session.get('semail'):		
		return redirect('/profile/') 	
	else:
		return render(request, 'accounts/signin.html')

def signup(request): 
	return render(request, 'accounts/signup.html') 
@csrf_exempt	
def signup_insert(request):
	if request.method == 'POST':
		user =User.objects.create_user(request.POST.get('uname'),request.POST.get('Email'),request.POST.get('Password'))
		if request.POST.get('Name') and request.POST.get('Email'):
			request.session['semail'] =request.POST.get('Email')
			post=Signup()
			myfile = request.FILES['pic']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			post.name= request.POST.get('Name')
			post.uname= request.POST.get('uname')
			post.email= request.POST.get('Email')
			post.password= request.POST.get('Password')
			post.pic=request.FILES['pic'].name
			profile_upload(request.FILES['pic'])
			print(request.POST.get('Name'))
			post.save()
		return redirect('/profile/')

def logout(request):
    try:
        del request.session['semail']
    except KeyError:
        pass
    return render(request, 'accounts/signin.html')

def login(request):
    if request.method != 'POST':
    	return render(request, 'accounts/signin.html')
    else:
    	try:
    		Signup.objects.get(email=request.POST['Email'], password=request.POST['Password'])
    		request.session['semail'] =request.POST.get('Email')
    		return redirect('/profile/')
    	except Signup.DoesNotExist:
    		messages.info(request,"!username or password is wrong!")
    		return render(request, 'accounts/signin.html')
  
			
@csrf_exempt	
def account_delete(request):
	raw_data=Signup.objects.get(email=request.session.get('semail')) 
	ob=User.objects.get(email=request.session.get('semail')) 
	raw_data.delete()
	ob.delete()
	del request.session['semail']
	return redirect('/') 
					
    		
  