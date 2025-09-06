from django.shortcuts import render, redirect
from .models import Post, BlogComment
from django.contrib import messages
from .templatetags import extras

# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()

    return render(request, 'blog/blogHome.html', {'allPost' : allPost})

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post = post, parent=None)
    replies = BlogComment.objects.filter(post = post).exclude(parent=None)
    user = request.user
    
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    print(replyDict)
        
    return render(request, 'blog/blogPost.html', {'post' : post, 'comments' : comments, 'user' : user, 'replyDict' : replyDict})

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        postID = request.POST.get('postSno')
        commentID = request.POST.get('commentSno')
        post = Post.objects.get(sno = postID)
        parent = BlogComment.objects.get(sno = commentID)

        if commentID == "":
            comment = BlogComment(
                comment = comment,
                user = request.user,
                post = post,
            )

            comment.save()

            messages.success(request, 'Comment posted successfully!')
        
        else:
            comment = BlogComment(
                comment = comment,
                user = request.user,
                post = post,
                parent = parent,
            )

            comment.save()

            messages.success(request, 'Reply posted successfully!')
            
    return redirect(f"/blog/{post.slug}")