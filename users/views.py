from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# def userlogin(request):
#     if(request.method=="POST"):
#         form= LoginForm(request.POST)
#         if form.is_valid():
#             data= form.cleaned_data
#             user= authenticate(request,username= data['username'], password= data['password'])

#             if user is not None:
#                 return HttpResponse('User Authenticated and logged in:')
#             else:
#                 return HttpResponse('Invalid credentials')
        
#     else:
#         form= LoginForm()
#     return render(request,'users/login.html',{'form': form })

@login_required
def index(request):
    return render(request,'users/index.html')