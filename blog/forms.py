from django import forms
from .models import Post, PostImage


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('category', 'title', 'text')


class ImageForm(forms.ModelForm):
	class Meta:
		model = PostImage
		fields = ('title', 'img')

	def __init__(self, *args, **kwargs):
		super(ImageForm, self).__init__(*args, **kwargs)
		self.fields['img'].required = False
