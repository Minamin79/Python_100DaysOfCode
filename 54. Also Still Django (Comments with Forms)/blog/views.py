from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from . import forms

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
    return render(request, 'post_list.html', context=context)


def post_details(request, year, month, day, slug):
    post = models.Post.objects.get(created_date__year=year,
                                   created_date__month=month,
                                   created_date__day=day,
                                   slug=slug,
                                   status='published')
    
    comment_form = forms.CommentForm()
    new_comment = None
    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    context = {
        'post': post,
        'comment_form': comment_form,
        'new_comment': new_comment,
    }
    
    return render(request, 'post_detail.html', context=context)


def contact_us(request):
    return render(request, 'contact_us.html')