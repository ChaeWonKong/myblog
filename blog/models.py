from django.db import models
from django.utils import timezone


class Post(models.Model):
	CATEGORY = (
			('cs', 'Computer Science'),
			('pj', 'Projects'),
			('es', 'Essays')
		)

	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	category = models.CharField(max_length=5, choices=CATEGORY)
	created_date = models.DateTimeField(blank=True, null=True)
	like_button = models.IntegerField(default=0)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title


class PostImage(models.Model):
	title = models.CharField(max_length=100)
	img = models.IMageField(null=True)

	def __str__(self):
		return self.title
