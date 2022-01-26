from django.db import models

# Create your models here.


class Source(models.Model):
    link = models.URLField()


class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    add_date = models.DateTimeField()
    link = models.URLField()
    guid = models.CharField(max_length=50)
    views = models.IntegerField()
    image = models.URLField(null=True)
    news_name = models.CharField(max_length=100)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}: {self.link}"

    def increment_views(self):
        self.views += 1
        self.save()


