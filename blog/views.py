from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PostForm
from .models import Post


def post_list(request):
	page_list = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	page = request.GET.get('page', 1)
	
	paginator = Paginator(page_list, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	return render(request, 'blog/post_list.html', { 'posts': posts })


"""def post_list(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'blog/post_list.html', {'posts': posts})"""


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now()
			post.save()

			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now()
			post.save()

			return redirect('post_detail', pk=post.pk)

	else:
		form = PostForm(instance=post)

	return	render(request, 'blog/post_edit.html', {'form': form})


def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()

	return redirect('post_list')


def about(request):
	return render(request, 'blog/about.html')


def category_list(request, category):

	page_list = Post.objects.filter(category=category, created_date__lte=timezone.now()).order_by('-created_date')
	page = request.GET.get('page', 1)
	
	paginator = Paginator(page_list, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	return render(request, 'blog/category_list.html', { 'posts': posts })
