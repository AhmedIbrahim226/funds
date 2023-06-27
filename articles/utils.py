from datetime import timedelta
from django.db.models import F
from .models import Article, TotalDailyArticleStats, TotalDailyArticleFunds, UserArticleStats, Currency
from django.utils import timezone


def datetime_at_12_am():
    next_day = timezone.now() + timedelta(days=1)
    at_12_am = next_day.replace(hour=0, minute=0, second=0, microsecond=0)
    return at_12_am

def check_can_repeat_link_on_range_time(link, user):
    from .models import Article
    articles = Article.objects.filter(link=link, owner=user)
    if articles.exists():
        article = articles.last()
        return article.created_at == timezone.now().date(), article
    return None, None


"""
1st calculating TotalDailyArticleStats,
2st calculating TotalDailyArticleFunds
"""



def calc_total_article_stats():
    for article in Article.objects.all():
        article_stats = article.article_stats.all()
        time__decimal = article_stats.values('time', 'received_decimal')

        t_time = (x['time'] for x in time__decimal)
        t_time = sum(t_time)

        t_percentage = (x['received_decimal'] for x in time__decimal)
        t_percentage = (sum(t_percentage) / len(time__decimal)) * 100

        try:
            TotalDailyArticleStats.objects.create(article=article, total_time=t_time, total_percentage=t_percentage)
            yield article, t_time, t_percentage
        except:
            pass


def calc_total_article_funds(article_stats):
    for article_stats in article_stats:
        article, t_time, t_percentage = article_stats

        currency_amount = Currency.objects.first().const_amount
        t_funds = t_time * t_percentage * currency_amount
        TotalDailyArticleFunds.objects.create(article=article, daily_funds=t_funds)

        user_article_stats, created = UserArticleStats.objects.get_or_create(owner=article.owner)
        user_article_stats.total_num_articles_read = F('total_num_articles_read') + 1
        user_article_stats.total_time_articles_read = F('total_time_articles_read') + t_time
        user_article_stats.total_articles_funds = F('total_articles_funds') + t_funds
        user_article_stats.save()
