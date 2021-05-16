from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category,Comments
from .forms import PostForm,EditForm,CommentsForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)

def home(request):
	context = {
			'posts' : Post.objects.all()
	}
	return render(request,'blog/home.html',context)

def LikeView(request,pk):
	post = get_object_or_404(Post,id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return redirect('post_detail', post.pk) 

def CommentView(request,pk):
	post = Post.objects.get(id=pk)
	comments = request.POST.get('id')
	if request.method == 'POST':
		comment_form = CommentsForm(request.POST)
		if comment_form.is_valid():
			body = request.POST.get('body')
			reply_id = request.POST.get('comments_id')
			comment_qs = None
			print(comments)
			if reply_id:
				comment_qs = Comments.objects.get(id=reply_id)
			comment = Comments.objects.create(post = post,name = request.user, body = body,parent = comment_qs)
			comment.save()
	else:
		comment_form = CommentsForm()
	return redirect('post_detail', post.pk) 

def CategoryView(request,cats):
	category_post = Post.objects.filter(category=cats.replace('-',' '))
	return render(request,'blog/categories.html',
		{'cats':cats.title().replace('-',' '),'category_post':category_post})

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 6


	def get_context_data(self,*args,**kwargs):
		cat_menu = Category.objects.all()
		context = super(PostListView,self).get_context_data(*args,**kwargs)
		context["cat_menu"] = cat_menu
		return context


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

	def get_context_data(self,*args,**kwargs):
		context = super(PostDetailView,self).get_context_data(*args,**kwargs)
		stuff = get_object_or_404(Post,id=self.kwargs.get('pk'))
		comments = Comments.objects.filter(post=stuff).order_by('-id')
		total_likes = stuff.total_likes()
		context["total_likes"] = total_likes
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True
			
		if self.request.method == 'POST':
			comment_form = CommentsForm(self.request.POST)
		else:
			comment_form = CommentsForm()

		context["liked"] = liked
		context["comments"] = comments
		context["comment_form"] = comment_form
		return context
# it prevents enter post creat view before log in

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	#fields = ('__all__')
	form_class = PostForm
	# Define who is writing post 

	def form_valid(self,form):
		print(self.request.POST)
		print(self.request.FILES)
		form.instance.author = self.request.user
		return super().form_valid(form)
									  # this checks if post.author is user or not


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	form_class = EditForm
	
	def form_valid(self,form):
		form.instance.author = self.request.user	
		return super().form_valid(form)
		# check if post is own author 
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class AddCommentLike(LoginRequiredMixin,View):
	def post(self,request,pk,*args,**kwargs):
		comment = Comments.objects.get(pk=pk)
		is_like = False 

		for like in comment.likes.all():
			if like == request.user:
				is_like = True
				break

		if not is_like:
			comment.likes.add(request.user)

		if is_like:
			comment.likes.remove(request.user)
		next = request.POST.get('next', '/')
		return HttpResponseRedirect(next)


class CommentReplyView(LoginRequiredMixin,View):
	def post(self,request,post_pk,pk,*args,**kwargs):
		post = Post.objects.get(pk=post_pk)
		parent_comment = Comments.objects.get(pk=pk)
		form = CommentsForm(request.POST)

		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.name = request.user
			new_comment.post = post 
			new_comment.parent = parent_comment
			new_comment.save()	

		return redirect('post_detail',post_pk)


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	
	def get_success_url(self):
		return reverse('blog-home')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



def about(request):
	return render(request, 'blog/about.html',{'title':'About'})
