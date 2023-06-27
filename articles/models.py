from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property


class Currency(models.Model):
    currency_type = models.IntegerField(_('currency type'), choices=[(1, 'EGP'), (2, 'USD')], default=1)
    const_amount = models.IntegerField(_('const amount'), default=5)

    def __str__(self):
        return self.get_currency_type_display()

    class Meta:
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')


class Article(models.Model):
    link = models.URLField(_('link'))
    owner = models.ForeignKey(verbose_name=_('owner'), to='users.UserAuth', on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateField(_('created at'), auto_now_add=True)

    @cached_property
    def get_stats(self):
        return self.total_daily_article_stats if hasattr(self, 'total_daily_article_stats') else '_'

    @cached_property
    def get_funds(self):
        return self.total_daily_article_funds if hasattr(self, 'total_daily_article_funds') else '_'

    @cached_property
    def get_reading_time_for_article(self):
        times_list = self.article_stats.all().values_list('time', flat=True)
        t_time = sum(times_list)
        if t_time < 60:
            return f"{round(t_time, 3)} s"
        elif t_time < 360:
            return f"{round(t_time / 60, 3)} m"
        return f"{round(t_time / 360, 3)} h"

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')


class ArticleStats(models.Model):
    article = models.ForeignKey(verbose_name=_('article'), to=Article, on_delete=models.CASCADE, related_name='article_stats')
    time = models.IntegerField(_('time'), default=10)
    received_decimal = models.FloatField(_('received decimal'))

    class Meta:
        verbose_name = _('article statistic')
        verbose_name_plural = _('article stats')

class TotalDailyArticleStats(models.Model):
    article = models.OneToOneField(verbose_name=_('article'), to=Article, on_delete=models.CASCADE, related_name='total_daily_article_stats')
    total_time = models.IntegerField(_('total time')) # total visit time for one article to user / 24 h
    total_percentage = models.FloatField(_('total percentage')) # total percentage for one article to user / 24 h

    class Meta:
        verbose_name = _('total daily article statistic')
        verbose_name_plural = _('total daily article stats')

class TotalDailyArticleFunds(models.Model):
    article = models.OneToOneField(verbose_name=_('article'), to=Article, on_delete=models.CASCADE, related_name='total_daily_article_funds')
    daily_funds = models.FloatField(_('daily funds')) # total funds for one article to user / 24 h

    class Meta:
        verbose_name = _('total daily article funds')
        verbose_name_plural = _('total daily article funds')


class UserArticleStats(models.Model):
    owner = models.OneToOneField(verbose_name=_('user'), to='users.UserAuth', on_delete=models.CASCADE, related_name='all_articles_stats')
    # total_articles_stats = models.ManyToManyField(to=TotalDailyArticleStats, verbose_name=_('total articles stats'), related_name='total_articles_stats')
    # total_article_funds = models.ManyToManyField(to=TotalDailyArticleFunds, verbose_name=_('total articles funds'))
    total_num_articles_read = models.IntegerField(_('total num articles read'), default=0)
    total_time_articles_read = models.FloatField(_('total time articles read'), default=0)
    total_articles_funds = models.FloatField(_('total articles funds'), default=0)

    @cached_property
    def ret_total_time_read_in_hour(self):
        return f"{round(self.total_time_articles_read / 60 / 60, 5)} h"

    class Meta:
        verbose_name = _('user article stats')
        verbose_name_plural = _('user article stats')
