from django.contrib import admin
from .models import Article, ArticleStats, TotalDailyArticleStats, TotalDailyArticleFunds, UserArticleStats, Currency



@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return self.model.objects.count() < 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(ArticleStats)
class ArticleStatsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(TotalDailyArticleStats)
class TotalDailyArticleStatsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(TotalDailyArticleFunds)
class TotalDailyArticleFundsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(UserArticleStats)
class UserArticleStatsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
