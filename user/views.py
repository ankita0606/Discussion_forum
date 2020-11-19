from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Account created!')
			url=reverse('base')
			return HttpResponseRedirect(url)
	else:
		form=UserRegisterForm()
	return render(request,'user/register.html',{'form': form})
@login_required
def updateprofile(request):
	if request.method=='POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Update Done!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context={'u_form':u_form, 'p_form':p_form}
	return render(request,'user/updateprofile.html',context)

@login_required
def profile(request):
	return render(request,'user/profile.html')

@login_required
def all_question(request):
	questions=Question.objects.all()
	context={'questions':questions}
	return render(request,'user/allques.html',context)
@login_required
def question_detail(request,id):
	instance = get_object_or_404(Question, id=id)
	instance.save()
	context={'instance':instance}
	return render(request,'user/ques_detail.html',context)
@login_required
def question_create(request):
	if request.method == 'POST':
		form=QuestionCreateForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Question asked!')
			url = reverse('allques')
			return HttpResponseRedirect(url)
	else:
		form = QuestionCreateForm(instance=request.user)
	context={'form':form}
	return render(request,'user/ask_question.html',context)

@login_required
def question_update(request):
	pass
@login_required
def question_del(request):
	pass
@login_required
def vote_up_ques(request):
	pass
@login_required
def vote_up_ans(request):
	pass


