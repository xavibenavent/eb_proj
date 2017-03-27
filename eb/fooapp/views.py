from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from fooapp!")

def template(request):
    context_dict = {'message': "Hello from template.html"}
    return render(request,'fooapp/base.html',context=context_dict)
