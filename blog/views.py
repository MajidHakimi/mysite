from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.published.all()

    # add pagination 
    # 1-we should get all post 
    # 2-create pagination object and split post ( get all objects + split number )
    paginator = Paginator(post_list , 3)
    # 3-get number of page pagination from user(request)
    page_number = request.GET.get('page',1)
    # 4-save new post for each page pagination by get number_page
    posts = paginator.page(page_number)


    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})



def post_detail(request, post , year , month , day  ):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day
                             )
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
