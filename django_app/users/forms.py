from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


SEX_OPTIONS = (
		('U', 'Unsure'),
        ('F', 'Female'),
        ('M', 'Male')
    )

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))


	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		
class ProfilRegistrationForm(forms.ModelForm):
	birth_day = forms.DateField(label='BirthDay',widget=forms.DateInput(attrs={'type':'date'}))
	sex = forms.ChoiceField(choices=SEX_OPTIONS)

	class Meta:
		model = Profile
		fields = ['birth_day','sex']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
	

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']


	def __init__(self,*args,**kwargs):
		super(UserUpdateForm, self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'class':'form-control'})

class ProfilUpdateForm(forms.ModelForm):
	birth_day = forms.DateField(label='BirthDay',widget=forms.DateInput(attrs={'type':'date'}))
	image = forms.ImageField()
	class Meta:
		model = Profile
		fields = ['birth_day','image']

	def __init__(self,*args,**kwargs):
		super(ProfilUpdateForm, self).__init__(*args,**kwargs)
		self.fields['birth_day'].widget.attrs.update({'class':'form-control'})