from django.shortcuts import render
from .models import Article, Job
from django.core.paginator import Paginator

# Create your views here.



def intro(request):
    return render(request, 'schedules/intro.html')

def index(request):
    articles = Article.objects.all()
    article_paginator = Paginator(articles,5)
    article_page = request.GET.get('page')
    article_obj = article_paginator.get_page(article_page)

    alltime_jobs = Job.objects.filter(end_date='상시채용')
    normal_jobs = Job.objects.exclude(end_date='상시채용')
    job_paginator = Paginator(normal_jobs, 10)
    job_page = request.GET.get('page')
    job_obj = job_paginator.get_page(job_page)
    context = { 'alltime_jobs':alltime_jobs, 'article_obj': article_obj, 'job_obj': job_obj}
    return render(request, 'schedules/index.html',context)