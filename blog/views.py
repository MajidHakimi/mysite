from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/post/list.html"

def post_share(request , post_id):

    post = get_object_or_404(Post , id=post_id , status=Post.Status.PUBLISHED )
    if request == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid:
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return(request , 'blog/post/share.html',
           {'posts':post,
            'form':form})



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
