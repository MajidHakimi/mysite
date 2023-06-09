from django.shortcuts import render, get_object_or_404
from .models import Post,Comments
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST



class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/post/list.html"

def post_share(request , post_id):

    sent = False
    post = get_object_or_404(Post , id=post_id , status=Post.Status.PUBLISHED )
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommend you to read {post.title}"
            message = f"read {post.title} in {post_url} that comments"\
                    f" {cd['comments']} "
            send_mail(subject , message , 'kalkele58@gmail.com' , [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request ,
                  'blog/post/share.html',
                  {'posts':post,
                   'form':form,
                   'sent':sent})



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


@require_POST
def post_comment(request , post_id):

    # retive post by id for connect to comment 
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    
    # define blank comment object to save comment 
    comment = None

    # make a form object instatnce to comment form 
    form = CommentForm(data=request.POST)

    # validate form 
    if form.is_valid():

        # put the form data in comment but don't save it 
        comment = form.save(commit=False)

        # assign specific post that retrived to post of comment object 
        comment.post = post

        # save comment 
        comment.save()

    # render requset and make "comments" tag to use in template 
    return render(request ,
                   "/blog/post/comment/html",
                   {"post":post,
                    "form":form,
                    "comment":comment})



    
    


