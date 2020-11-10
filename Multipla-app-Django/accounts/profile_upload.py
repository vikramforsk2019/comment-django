def profile_upload(f):  
    with open('dietplan/static/upload/profilepic/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  