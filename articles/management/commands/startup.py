from django.core.management.base import BaseCommand
from django_q.tasks import schedule
from articles.utils import datetime_at_12_am


class Command(BaseCommand):
    help = "Create CRON scheduler tasks"

    def handle(self, *args, **options):
        schedule(
            'articles.tasks.daily_task',
            schedule_type='D',
            next_run=datetime_at_12_am()
        )
        self.stdout.write(self.style.SUCCESS("Successfully created CRON task"))