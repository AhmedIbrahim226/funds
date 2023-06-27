from .utils import calc_total_article_stats, calc_total_article_funds


def daily_task():
    article_stats = list(calc_total_article_stats())
    calc_total_article_funds(article_stats=article_stats)
