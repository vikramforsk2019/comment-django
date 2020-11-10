from dietapp.post_upload import post_upload
from dietapp.profile_upload import profile_upload  #file upload
from django.shortcuts import render  
from django.template import loader  
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Signup 
from .models import Health_data
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request): 	 
	return render(request, 'dietapp/index.html') 

   
#@login_required(login_url='/login/')
def health_post(request): 
	return render(request, 'dietapp/post-ad.html')
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


  