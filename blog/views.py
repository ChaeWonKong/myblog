import requests
import json
from bs4 import BeautifulSoup

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .forms import PostForm
from .models import Post


def case_scraper(request):
	"""Search request in casenote.kr and return outcome"""

	link = "https://casenote.kr/search/?q="+request
	req = requests.get(link)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	issue = soup.find('div', {'class': 'issue'}).get_text()
	summary = soup.find('div', {'class': 'summary'}).get_text()

	return [issue, summary, link]


def buttons(request):
	return JsonResponse({
		"type": "buttons",
		"buttons": ['판례검색', ]
		})


@csrf_exempt
def message(request):
	json_str = (request.body).decode('utf-8')
	json_data = json.loads(json_str)
	request = json_data['content']

	if request =='판례검색':
		return JsonResponse({
			"message": {"text": "판례번호를 띄어쓰기 없이 입력해주세요"}
			})
	else:
		try:
			case = case_scraper(request)
		except:
			return JsonResponse({
				"message": {
				"text": "해당 판례를 찾을 수 없습니다.\n띄어쓰기에 유의해 다시 검색해주세요.\n\n 예) 98다22543"
				}
			})
		else:
			return JsonResponse({
				"message": {
					"text": request + "\n\n판시사항\n\n" + case[0] +
							"\n\n판결요지\n\n" + case[1] +
							"\n\n케이스노트에서 자세히 보기\n\n" + case[2]
					},
			})


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
	return render(request, 'blog/post_detail.html', {'posts': post})


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
