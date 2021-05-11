from django import forms
from .models import Post,Category,Comments

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','title_tag','header_image','category','content','snippet']
		widgets = {
				'title':forms.TextInput(attrs={'class':'form-control'}),
				'title_tag': forms.TextInput(attrs={'class':'form-control'}),
				'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
				'content':forms.Textarea(attrs={'class':'form-control'}),
				'snippet':forms.Textarea(attrs={'class':'form-control'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','title_tag','header_image','category','content','snippet']
		widgets = {
				'title':forms.TextInput(attrs={'class':'form-control'}),
				'title_tag': forms.TextInput(attrs={'class':'form-control'}),
				'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
				'content':forms.Textarea(attrs={'class':'form-control'}),
				'snippet':forms.Textarea(attrs={'class':'form-control'}),
		}

class CommentsForm(forms.ModelForm):
	class Meta():
		model = Comments
		fields = ['body']
		widgets = {
				'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Your message','rows':'5','cols':'500'}),
		}