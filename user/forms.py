from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']

class QuestionCreateForm(forms.ModelForm):
	#Sdescription=forms.CharField(label='Question',widget=forms.Textarea())
	class Meta:
		model=Question
		fields=['time_post','question_text','user_posted']