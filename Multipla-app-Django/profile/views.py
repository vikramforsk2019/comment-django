from dietapp.post_upload import post_upload
from dietapp.profile_upload import profile_upload  #file upload
from django.shortcuts import render  
from django.template import loader  
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Signup 
from dietapp.models import Health_data
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@csrf_exempt
def profile(request):
	if request.session.get('semail'): 	
		profile_data=Signup.objects.get(email=request.session.get('semail'))
		post_data=Health_data.objects.filter(userid=profile_data.id)
		#print(post_data[0].postfile)
		return render(request, 'profile/profile.html',{'profile_data':profile_data,'post_data':post_data})
	else:
		return render(request, 'accounts/signup.html')


def edit(request):
	raw_data=Signup.objects.get(email=request.session.get('semail')) 
	return render(request, 'profile/edit.html',{'raw_data':raw_data})

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
			

					
    		
  