from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

# Create your views here.

# Function based veiw
def post_list(request):
    posts = models.Post.objects.filter(status='published')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    # return HttpResponse('HelloWorld!')
    return render(request, 'post_list.html', context=context)


def post_details(request, year, month, day, slug):
    # try:

    #     post = models.Post.objects.get(created_date__year=year,
    #                                 created_date__month=month,
    #                                 created_date__day=day,
    #                                 slug=slug,
    #                                 status='published'))
    # except models.Post.DoesNotExist:
    #     raise Http404("This post doesn't exist.")

    post = models.Post.objects.get(created_date__year=year,
                                   created_date__month=month,
                                   created_date__day=day,
                                   slug=slug,
                                   status='published')
    context = {
        'post': post,
    }
    # return HttpResponse(post.title)
    return render(request, 'post_detail.html', context=context)


def contact_us(request):
    return render(request, 'contact_us.html')