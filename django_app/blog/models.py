from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog-home')

class Post(models.Model):
	title = models.CharField(max_length=200)
	title_tag = models.CharField(max_length=255)	
	header_image = models.ImageField(blank=True,default='header.jpg',upload_to='header_pictures')
	content = RichTextField(blank=True,null=True)
	date_posted = models.DateTimeField(default=timezone.now)
	category = models.CharField(max_length=255,default='uncategorized')
	snippet = models.TextField(max_length=255)
	likes = models.ManyToManyField(User,related_name='blog_posts')
	# one to many relationships      if user is deleted post will be deleted
	author = models.ForeignKey(User,on_delete=models.CASCADE)
		
	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'pk': self.pk})

class Comments(models.Model):
	post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	name = models.ForeignKey(User,on_delete=models.CASCADE)
	body = models.TextField()
	likes = models.ManyToManyField(User,related_name='comment_posts')
	parent = models.ForeignKey('self',blank=True,null=True,related_name="+",on_delete=models.CASCADE)
	date_added = models.DateField(auto_now_add=True)

	@property
	def children(self):
		return Comments.objects.filter(parent=self).order_by('-date_added').all()

	@property
	def is_parent(self):
		if self.parent is None: 
			return True
		return False

	def __str__(self):
		return '%s-%s'%(self.post.title,self.name)

	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'pk': self.pk})	
		