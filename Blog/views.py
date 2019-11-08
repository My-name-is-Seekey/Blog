from django.http import HttpResponse
from django.shortcuts import render
from Article.models import *
from django.core.paginator import Paginator


def about(request):
    return render(request, 'about.html')


def index(request):
    article_index = Article.objects.all()[:6]
    recommend = Article.objects.filter(recommend='1')[:7]
    content_click = Article.objects.all().order_by('-click')[:12]
    return render(request, 'index.html', locals())
def listpic(request):
    return render(request, 'listpic.html')


def newslistpic(request, page):
    article = Article.objects.all()
    paginator = Paginator(article, 6)

    if not page:
        page = 1

    pag_obj = paginator.page(page)

    if pag_obj.has_next():
        pag_next = pag_obj.next_page_number()
    else:
        pag_next = paginator.num_pages

    if pag_obj.has_previous():
        pag_previous = pag_obj.previous_page_number()

    # 实现制定页码跳转
    page = int(page)
    if 3 <= page <= 15:
        page_list = [i for i in range(page - 2, page + 3)]
    else:
        page_list = [1, 2, 3, 4, 5] if page < 3 else [12, 14, 15, 16, 17]
    return render(request, 'newslistpic.html', locals())


def base(request):
    return render(request, 'base.html')


def articlecontent(request, id):
    article = Article.objects.get(id=id)
    article.click += 1
    article.save()
    return render(request, 'articlecontent.html', locals())
