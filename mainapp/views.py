from django.shortcuts import render

# Create your views here.
def baseactivate(request):
	return render(request,'mainapp/base.html')

def home(request):
	return render(request,'mainapp/home.html')
