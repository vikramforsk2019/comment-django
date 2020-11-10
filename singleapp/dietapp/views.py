from dietapp.post_upload import post_upload
from dietapp.profile_upload import profile_upload  #file upload
from django.shortcuts import render  
from django.template import loader  
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
from .models import Signup 
from .models import Health_data
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate
@csrf_exempt
def signin(request):
	if request.session.get('semail'):		
		return redirect('/profile/') 	
	else:
		return render(request, 'signin.html')

def signup(request): 
	return render(request, 'signup.html') 
@csrf_exempt	
def signup_insert(request):
	if request.method == 'POST':
		if request.POST.get('Name') and request.POST.get('Email'):
			request.session['semail'] =request.POST.get('Email')
			post=Signup()
			post.name= request.POST.get('Name')
			post.uname= request.POST.get('uname')
			post.email= request.POST.get('Email')
			post.password= request.POST.get('Password')
			post.pic=request.FILES['pic'].name
			profile_upload(request.FILES['pic'])
			print(request.POST.get('Name'))
			post.save()
		return redirect('/profile/') 

def index(request): 	 
	return render(request, 'index.html') 

def profile(request):
	if request.session.get('semail'): 	
		profile_data=Signup.objects.get(email=request.session.get('semail'))
		post_data=Health_data.objects.filter(userid=profile_data.id)
		#print(post_data[0].postfile)
		return render(request, 'profile.html',{'profile_data':profile_data,'post_data':post_data})
	else:
		return render(request, 'signup.html')

def logout(request):
    try:
        del request.session['semail']
    except KeyError:
        pass
    return render(request, 'signin.html')

def login(request):
    if request.method != 'POST':
    	return render(request, 'signin.html')
    else:
    	try:
    		Signup.objects.get(email=request.POST['Email'], password=request.POST['Password'])
    		request.session['semail'] =request.POST.get('Email')
    		return redirect('/profile/')
    	except Signup.DoesNotExist:
    		messages.info(request,"!username or password is wrong!")
    		return render(request, 'signin.html')
   

def health_post(request): 
	return render(request, 'post-ad.html')
@csrf_exempt
def health_data(request):
	if request.method == 'POST':
		user = Signup.objects.get(email=request.session.get('semail'))
		post=Health_data()
		post.userid=user.id		
		post.group= request.POST.get('group')	
		post.age= request.POST.get('Age')
		post.weight= request.POST.get('Weight')	
		post.postfile=request.FILES['postfile'].name
		post.save()
		post_upload(request.FILES['postfile']) 
		return redirect('/profile/') 

def edit(request):
	raw_data=Signup.objects.get(email=request.session.get('semail')) 
	return render(request, 'edit.html',{'raw_data':raw_data})

@csrf_exempt	
def edit_data(request):
	raw_data=Signup.objects.get(email=request.session.get('semail')) 
	raw_data.password=request.POST.get('password')
	raw_data.name= request.POST.get('Name')
	raw_data.uname=request.POST.get('uname')
	try: 
		raw_data.pic=request.FILES['pic'].name
		profile_upload(request.FILES['pic'])
	except Exception as e:
		print('no image update')
	print(raw_data.pic)
	raw_data.save()
	return redirect('/profile/') 
			
@csrf_exempt	
def account_delete(request):
	raw_data=Signup.objects.get(email=request.session.get('semail')) 
	raw_data.delete()
	del request.session['semail']
	return redirect('/') 
					
    		
  