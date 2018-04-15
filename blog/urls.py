from django.urls import path
from . import views


urlpatterns = [
		path('', views.post_list, name='post_list'),
		path('<int:id>/', views.post_detail, name='post_detail'),
		path('post/new/', views.post_new, name='post_new'),
		path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
		path('about', views.about, name='about'),
		path('post/<int:id>/remove/', views.post_remove, name='post_remove'),
		path('<str:category>', views.category_list, name='category_list'),
		path('<int:id>/like_action/', views.like_action, name='like_action'),
]