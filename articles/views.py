from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse


def index(request):
	return render(request, 'articles/list.html')

def stix(request):
	return render(request, 'articles/stix.html')

def overview(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:5]
	#отображение статей 
	return render(request, 'articles/overview.html', {'latest_articles_list':latest_articles_list})
	
def Detail(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404('Статьи нема')

	latest_comments_list = a.comment_set.order_by('-id')[:10]

	return render(request,'articles/Detail.html', {'article':a, 'latest_comments_list':latest_comments_list }) 

def leave_comment(request, article_id):
	try:
		a = Article.objects.all(id = article_id)
	except:
		raise Http404('Статьи нет')

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('articles:Detail', args = (a.id,)) )