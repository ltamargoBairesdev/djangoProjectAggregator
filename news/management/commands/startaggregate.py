# news/management/commands/startaggregate.py

from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser
from news.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        for src in Source.objects.all():
            feed = feedparser.parse(src.link)
            news_title = feed.channel.title
            if 'image' in feed.channel:
                news_image = feed.channel.image.url
            else:
                news_image = ""

            for item in feed.entries:
                if not NewsItem.objects.filter(link=item.link).exists():
                    news = NewsItem(
                        title=item.title,
                        description=item.description,
                        add_date=parser.parse(item.published),
                        link=item.link,
                        guid=item.guid,
                        views=0,
                        image=news_image,
                        news_name=news_title,
                        source=src
                    )
                    news.save()
