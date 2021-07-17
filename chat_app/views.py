from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'basic.html',{})

def chat(request):
    return render(request,"chat.html",{})