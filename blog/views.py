# -*- coding: utf-8 -*-
import json

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .forms import PostForm, ImageForm
from .models import Post, PostImage


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


def like_action(request, pk):
	"""Like action: add +1 to post.like_button"""

	post = get_object_or_404(Post, pk=pk)
	post.like_button = post.like_button + 1
	post.save()

	return redirect('post_detail', pk=post.pk)


def upload(request):
	imgform = ImageForm(request.POST, request.FILES)

	if request.method == 'POST':
		if imgform.is_valid():
			image = imgform.save(commit=False)
			image.save()
			src = get_object_or_404(PostImage, pk=image.pk).img.url
			return render(request, "blog/upload.html", {'imgform': imgform, 'src': src})
	else:
		imgform = ImageForm()
	return render(request, "blog/upload.html", {'imgform': imgform})

