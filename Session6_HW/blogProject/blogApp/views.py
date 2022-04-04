from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method =='POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            
        )
        return redirect('list')
    return render(request, 'new.html')

def count(category_name):
    result=0;
    for article in Article.objects.all():
        if article.category == category_name:
            result +=1
    return result
def list(request):
    return render(request, 'list.html',{'articles':Article.objects.all(), 'article_nums':{
        'hobby': count('Hobby'),
        'study': count('Study'),
        'book' : count('Book'),
    }})

def detail(request, article_id):
    return render(request, 'detail.html',{'article': Article.objects.get(pk = article_id)})

def category(request, category_name):
    articles = Article.objects.filter(category = category_name)
    return render(request, 'category.html', {'articles': articles})