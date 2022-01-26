# Create your views here.
from django.core.management import call_command
from django.urls import reverse
from django.views.generic import *
from django.shortcuts import get_object_or_404

from .models import *
from .forms import SourceForm


class SourceFormView(FormView):
    template_name = 'homepage.html'
    form_class = SourceForm
    success_url = "/"

    def form_valid(self, form):
        link = form.cleaned_data.get('source_link')
        source = Source(link=link)
        source.save()
        call_command('startaggregate')
        return super().form_valid(form)


class NewsPageView(ListView):
    template_name = "news.html"
    model = NewsItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newsItems"] = NewsItem.objects.filter().order_by("-add_date")
        return context


class ViewsPageView(ListView):
    template_name = "views.html"
    model = NewsItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newsItems"] = NewsItem.objects.filter().order_by("-add_date")
        return context


class IncrementViewsRedirectView(RedirectView):
    permanent = False
    pattern_name = 'increment-views'

    def get_redirect_url(self, *args, **kwargs):
        news = get_object_or_404(NewsItem, id=kwargs['news_id'])
        news.increment_views()
        return news.link

