from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserArticleStats, Article

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'articles/dashboard.html'

    def get_context_data(self, **kwargs):
        article_stats = UserArticleStats.objects.filter(owner=self.request.user)
        articles = Article.objects.filter(owner=self.request.user)
        ctx = super().get_context_data()
        ctx.update(article_stats=article_stats, articles=articles)
        return ctx
