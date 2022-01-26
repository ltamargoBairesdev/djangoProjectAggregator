from django.test import TestCase
from django.utils import timezone
from .models import NewsItem

# Create your tests here.
class NewsItemTests(TestCase):
    def setUp(self):
        self.item = NewsItem.objects.create(
            title="Title of the News",
            description="This is a news",
            add_date=timezone.now(),
            link="https://myawesomeshow.com",
            news_name="My Python News Aggregator",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr",
        )

    def test_newsItem_content(self):
        self.assertEqual(self.item.description, "This is a news")
        self.assertEqual(self.item.link, "https://myawesomeshow.com")
        self.assertEqual(
            self.item.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"
        )

    def test_newsItem_str_representation(self):
        self.assertEqual(
            str(self.item), "My Python News Aggregator: Title of the News"
        )

