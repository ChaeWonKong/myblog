from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
		path('keyboard', views.buttons, name='buttons'),
		path('message', views.message, name='message'),
		path('', views.post_list, name='post_list'),
		path('<int:pk>/', views.post_detail, name='post_detail'),
		path('post/new/', views.post_new, name='post_new'),
		path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
		path('about', views.about, name='about'),
		path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
		path('<str:category>', views.category_list, name='category_list'),
		path('post/<int:pk>/like_action/', views.like_action, name='like_action'),
		path('post/upload/', views.upload, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)