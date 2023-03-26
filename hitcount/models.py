from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HitCount(models.Model):
    article = models.OneToOneField(Article, null=True, blank=True, on_delete=models.CASCADE, related_name='articles')
    hits = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['hits']

    def __str__(self):
        return f"{self.article} - {self.hits}"
