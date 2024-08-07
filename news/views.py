from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Article, Comment
from  customize.models import Links, Address
from  gallery.models import ImageNews

class homeListView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        myset = {
            "urgent1" : Article.objects.filter(is_urgent=True).filter(is_active=True).order_by('-id')[:1],
            "urgent2" : Article.objects.filter(is_urgent=True).filter(is_active=True).order_by('-id')[1:2],
            "urgent3" : Article.objects.filter(is_urgent=True).filter(is_active=True).order_by('-id')[2:3],
            "urgent4" : Article.objects.filter(is_urgent=True).filter(is_active=True).order_by('-id')[3:4],
            "world" : Article.objects.filter(category__url_title="world").filter(is_active=True).order_by('-id')[:4],
            "politics" : Article.objects.filter(category__url_title="politics").filter(is_active=True).order_by('-id')[:4],
            "economy" : Article.objects.filter(category__url_title="economy").filter(is_active=True).order_by('-id')[:4],
            "sport" : Article.objects.filter(category__url_title="sport").filter(is_active=True).order_by('-id')[:4],
            "local" : Article.objects.filter(category__url_title="local").filter(is_active=True).order_by('-id')[:4],
            "science" : Article.objects.filter(category__url_title="science").filter(is_active=True).order_by('-id')[:4],
            "travel" : Article.objects.filter(category__url_title="travel").filter(is_active=True).order_by('-id')[:4],
            "health" : Article.objects.filter(category__url_title="health").filter(is_active=True).order_by('-id')[:4],
            "style" : Article.objects.filter(category__url_title="style").filter(is_active=True).order_by('-id')[:4],
            "weather" : Article.objects.filter(category__url_title="weather").filter(is_active=True).order_by('-id')[:4],
            "gallery" : Article.objects.filter(category__url_title="gallery").filter(is_active=True).order_by('-id')[:4],
            "links" : Links.objects.all().first(),
            "address" : Address.objects.all().first(),
            "imagenews" : ImageNews.objects.all().first(),
        }
        return myset
    

class WorldListView(ListView):
    template_name = 'news/world.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    
    def get_queryset(self):
        return Article.objects.filter(category__url_title="world").filter(is_active=True).order_by('-id')

class PoliticsListView(ListView):
    template_name = 'news/politics.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="politics").filter(is_active=True).order_by('-id')

class EconomyListView(ListView):
    template_name = 'news/economy.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="economy").filter(is_active=True).order_by('-id')

class SportListView(ListView):
    template_name = 'news/sport.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="sport").filter(is_active=True).order_by('-id')

class LocalListView(ListView):
    template_name = 'news/local.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="local").filter(is_active=True).order_by('-id')

class ScienceListView(ListView):
    template_name = 'news/science.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="science").filter(is_active=True).order_by('-id')

class TravelListView(ListView):
    template_name = 'news/travel.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="travel").filter(is_active=True).order_by('-id')

class HealthListView(ListView):
    template_name = 'news/health.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="health").filter(is_active=True).order_by('-id')

class StyleListView(ListView):
    template_name = 'news/style.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="style").filter(is_active=True).order_by('-id')

class WeatherListView(ListView):
    template_name = 'news/weather.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        return Article.objects.filter(category__url_title="weather").filter(is_active=True).order_by('-id')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article.html'
    context_object_name = 'news'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = Comment.objects.filter(article_id=article.id).order_by('-create_date')
        return context


def add_article_comment(request: HttpRequest, **kwargs):
    if request.user.is_authenticated:
        article_comment = request.GET.get('article_comment')
        article_id = request.GET.get('article_id')
        # print(article_id, article_comment)
        new_comment = Comment(article_id=article_id, text=article_comment, user=request.user)
        if article_comment is not None:
            new_comment.save()

    return HttpResponse('response')
