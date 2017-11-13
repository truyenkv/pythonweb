from django.shortcuts import render
from blog.models import Post

def list(request):
	Data = {
		'Posts':Post.objects.all().order_by("-date")[:10],
	}
	return render(request,'blog/blog.html', Data)
	