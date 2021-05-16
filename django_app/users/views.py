from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,ProfilRegistrationForm,UserUpdateForm,ProfilUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		p_reg_form = ProfilRegistrationForm(request.POST)
		if form.is_valid() and p_reg_form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			p_reg_form = ProfilRegistrationForm(request.POST, instance=user.profile)
			p_reg_form.full_clean()
			p_reg_form.save()
			username = form.cleaned_data.get('username')
			return redirect('login')
	else:
		form = UserRegisterForm()
		p_reg_form = ProfilRegistrationForm()

	context = {
		'form': form,
		'p_reg_form': p_reg_form
	}
	return render(request,'users/register.html',context)

@login_required
def profile_view(request):
	u_form = UserUpdateForm(instance = request.user)
	p_form = ProfilUpdateForm(instance = request.user.profile)
	if request.method == "POST":

		u_form = UserUpdateForm(request.POST,instance = request.user)
		p_form = ProfilUpdateForm(request.POST,request.FILES,instance = request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			
			return redirect('profile')

	
	context = {
		'u_form':u_form,
		'p_form':p_form,
	}
	return render(request,'users/profile.html',context)

