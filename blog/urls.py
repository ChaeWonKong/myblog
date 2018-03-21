from django.urls import path
from . import views

urlpatterns = [
		path('', views.post_list, name='post_list'),
		path('<int:pk>/', views.post_detail, name='post_detail'),
		path('post/new/', views.post_new, name='post_new'),
		path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
		path('about', views.about, name='about'),
		path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
		path('<str:category>', views.category_list, name='category_list'),
]