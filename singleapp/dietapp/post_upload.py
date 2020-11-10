def post_upload(f): 
	with open('dietapp/static/upload/postpic/'+f.name, 'wb+') as destination:  
		for chunk in f.chunks():
			destination.write(chunk) 