from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import HitCount, Article
from django.core.cache import cache


def update_hit_count(article_id):
    key = f'article_{article_id}_hitcount'
    hitcount = cache.get(key)
    print("test-1: ", hitcount)
    if hitcount is None:
        hitcount, created = HitCount.objects.get_or_create(article_id=article_id)
        cache.set(key, hitcount.hits)
        print("test-2: ", hitcount, created)
    else:
        hitcount = HitCount.objects.filter(article_id=article_id).update(hits=F('hits') + 1)
        cache.incr(key)
        print("test-3: ", hitcount)
    return hitcount


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    hitcount = update_hit_count(article.pk)

    return render(request, 'article_detail.html', {'article': article, 'hitcount': hitcount})


def article(request):
    articles = Article.objects.all()

    return render(request, 'index.html', {"articles": articles})


class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'
