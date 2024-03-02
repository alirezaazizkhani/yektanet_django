from celery import shared_task
from datetime import datetime, timedelta
from .models import Click , Saver  , View

@shared_task
def calculate_clicks_past_hour():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)
    clicks_past_hour = Click.objects.filter(click_time__gte=start_time, click_time__lt=end_time).count()
    from .models import Saver
    Saver.objects.create(count=clicks_past_hour)


@shared_task
def calculate_clicks_hour():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)
    click_past_hour = Click.objects.filter(click_time__gte=start_time, click_time__lt=end_time).count()
    from .models import Saver
    Saver.objects.create(count=click_past_hour)


@shared_task
def calculate_views_hour():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)
    view_past_hour = View.objects.filter(view_time__gte=start_time, view_time__lt=end_time).count()
    from .models import Saver
    Saver.objects.create(count=view_past_hour)


@shared_task
def calculate_clicks_days():
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    click_count = Click.objects.filter(click_time__range=(start_time, end_time)).count()
    Saver.objects.create(count=click_count)


@shared_task
def calculate_views_days():
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    view_count = Click.objects.filter(view_time__range=(start_time, end_time)).count()    
    Saver.objects.create(count=view_count)


