from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PostForm
from .models import Post


def post_list(request):
	page_list = \
		Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	page = request.GET.get('page', 1)
	
	paginator = Paginator(page_list, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	return render(request, 'blog/post_list.html', { 'posts': posts })


def post_detail(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, 'blog/post_detail.html', {'posts': post})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now()
			post.save()

			return redirect('post_detail', id=post.id)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, id):
	post = get_object_or_404(Post, id=id)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now()
			post.save()

			return redirect('post_detail', id=post.id)

	else:
		form = PostForm(instance=post)

	return	render(request, 'blog/post_edit.html', {'form': form})


def post_remove(request, id):
	post = get_object_or_404(Post, id=id)
	post.delete()

	return redirect('post_list')


def about(request):
	return render(request, 'blog/about.html')


def category_list(request, category):

	page_list = \
		Post.objects.filter(category=category, \
				created_date__lte=timezone.now()).order_by('-created_date')
	page = request.GET.get('page', 1)
	
	paginator = Paginator(page_list, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	return render(request, 'blog/category_list.html', { 'posts': posts })


def like_action(request, id):
	"""Like action: add +1 to post.like_button"""

	post = get_object_or_404(Post, id=id)
	post.like_button = post.like_button + 1
	post.save()

	return redirect('post_detail', id=post.id)
