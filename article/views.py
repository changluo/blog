from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
# Create your views here.
#def home(request):
#    return HttpResponse("Hello World,Django")
'''
def detail(request, id):
    try:
        post=Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('post.html', {'post':post})
    
def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})
'''
def home(request):
    return render_to_response('home.html')
def base(request):
    return render_to_response('base.html')
def base1(request):
    return render_to_response('base1.html')
def index(request):
    post_list=Article.objects.all()
    return render_to_response('index.html',{'post_list':post_list})
