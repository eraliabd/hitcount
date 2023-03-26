from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import HitCount, Article
from django.core.cache import cache


def update_hit_count(article_id):
    key = f'article_{article_id}_hitcount'
    hitcount = cache.get(key)
    print("test-1: ", hitcount, "key: ", key)
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

    context = {
        'article': article,
    }

    return render(request, 'article_detail.html', context)


def article(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'index.html', context)


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(created__gte='2023-03-26 06:00:00')
    template_name = 'index.html'
