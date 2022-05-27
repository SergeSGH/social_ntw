# from django.db.models import Avg

from posts.models import News
from social_ntw.celery import app


@app.task
def do_something():
    # news_list = News.objects.all().annotate(avg_score=Avg('scores__score'))
    # for news in news_list:
    #     news.rating = news.avg_score
    #     news.save()
    # print('ratings updated')
    return 'Success'
