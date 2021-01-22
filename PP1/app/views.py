from django.shortcuts import render, HttpResponse
from app.models import Task1
from json import dumps
import hashlib, uuid

# Create your views here.

def sign(request):
    if request.method=='POST':
        objects=Task1.objects.all()
        first=request.POST.get('first_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        last=request.POST.get('last_name')
        print('first',first,'last',last,'password',password,'email',email)
        try:
            hash_password = hashlib.md5(password.encode()).hexdigest()
        except:
            hash_password=''
        if last==first==password==None and email!=None:
            for obj in objects:
                if obj.email==email:
                    return HttpResponse(dumps({'user_id':email,'login_type':'signin'}))
            return  HttpResponse(dumps({'user_id':'Not Registered','login_type':'signup'}))

        if None not in [first,last,email,password]:
            for obj in objects:
                if obj.email==email:
                    return  HttpResponse(dumps({'message':'Create user failed, User already exist'}))
            task1=Task1(first=first,email=email,password=hash_password,last=last)
            task1.save()
            return  HttpResponse(dumps({'message':'New User registered'}))
        if email!=None and password!=None:
            for obj in objects:
                if obj.email==email:
                    if obj.password==hash_password:
                        return  HttpResponse(dumps({'message':'Login Sucessfull'}))
                    else:
                        return  HttpResponse(dumps({'message':'Login Failed'}))
            return  HttpResponse(dumps({'message':'User Not Registered'}))    
    return HttpResponse('This is Sign Page')



def add(request):
    if request.method=='POST':
        email=request.POST.get('email')
        category=request.POST.get('category')
        try:
            obj=Task1.objects.get(email=email)
            category=category.lower()
            if category in obj.favourite:
                return HttpResponse(dumps({'message':'Category Already exist in user favourites'}))
            else:
                if obj.favourite=='':
                    obj.favourite=' '+category
                else:
                    obj.favourite+=', '+category
                obj.save()
                return HttpResponse(dumps({'message':'Category added in user favourites'}))
        except:
            return HttpResponse(dumps({'message':'User does not exist'}))
        
            
           

def delete(request):
    if request.method=='POST':
        email=request.POST.get('email')
        category=request.POST.get('category')
        try:
            obj=Task1.objects.get(email=email)
        except:
            return HttpResponse(dumps({'message':'User dose not exist'}))
        category=' '+category.lower()
        if category not in obj.favourite:
            return HttpResponse(dumps({'message':'Category does not exist in user favourites'}))
        else:
            favourite=obj.favourite.split(',')
            favourite.remove(category)
            obj.favourite=','.join(favourite)
            obj.save()
            return HttpResponse(dumps({'message':'Category deleted from user favourites'}))
        

def show(request):
    if request.method=='POST':
        email=request.POST.get('email')
        try:
            obj=Task1.objects.get(email=email)
            favourite=obj.favourite.split(',')
            return HttpResponse(dumps({'first_name':obj.first,'last_name':obj.last,'email':email,'favourite':[fav[1:] for fav in favourite]}))

        except:
            return HttpResponse(dumps({'message':'User dose not exist'}))
    return HttpResponse(dumps({'message':'incorrect request'}))

        