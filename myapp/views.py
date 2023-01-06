from django.shortcuts import render
from django.http import HttpResponse
import datetime
from myapp.models import Blog, Comment
from myapp.forms import BlogForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

 

# Create your views here.

def indexHandler(request):
    return render(request, 'utility/index.html')
'''
def showAllBlogs(request):
    all_blogs_variable = Blog.objects.all()
    return render(request, 'all_blogs.html', {'blogs': all_blogs_variable})

def delete(request):
    id1 = int(request.GET['id'])
    Blog.objects.get(id=id1).delete()
    return render(request, 'all_blogs.html', {'success':'deleted successfully'})


def addBlog(request):
    print(request)
    if request.POST != None:
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        tags = request.POST.get('tags')
        no_lines = request.POST.get('no_lines')
        publisher = request.POST.get('publisher')

    else:
        pass

    obj = Blog.objects.create(title=title, description= description, 
    tags= tags, no_lines= no_lines, publisher= publisher)
    return render(request, 'all_blogs.html', {'success': "USER ADDED SUCCESSFULLY"})

'''
def handle404Error(request, exception):
    return render(request, 'utility/404.html')
#@login_required(login_url='/admin')
def formAddBlog(request):
    b_form = BlogForm()
    return render(request, "pages/form-add-blog.html", {'form': b_form})

@login_required
def formSave(request):
    success = ''
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get('description')
            tags = form.cleaned_data.get('tags')
            publisher = form.cleaned_data.get('publisher')
            no_lines = form.cleaned_data.get('no_lines')
            img = form.cleaned_data.get('img')
            author = request.user

            obj = Blog.objects.create(author = author,title=title, 
                                        description=description,
                                        tags = tags,
                                        publisher = publisher,
                                        no_lines = no_lines,
                                        img = img
                                    )
            obj.save()
            success = " Blog Added Successfully"

    return render(request, "pages/form-add-blog.html", {"success":success})

def viewOnlyBlogs(request):
    obj = Blog.objects.all()
    return render(request, 'pages/all_blogs_view.html', {'blogs':obj})

@login_required
def aDelete(request, id):
    success = ''
    obj = Blog.objects.get(id=id)
    if obj.author == request.user:
        Blog.objects.get(id = id).delete()
        success = 'Blog deleted successfully'
    else:
        success = ' You are not allow to delete this blog '
    return render(request, "pages/all_blogs_view.html", {'success': success})

@login_required
def updateForm(request, id):
    blog_data = Blog.objects.get(id = id)
    return render(request, 'pages/update-form.html', {'blog_data': blog_data})

@login_required
def updateData(request):
    print(request.POST)
    comm_id = request.POST.get('i-d')
    title = request.POST.get('title')
    description = request.POST.get('description')
    tags = request.POST.get('tags')
    publisher = request.POST.get('publisher')
    no_lines = request.POST.get('no_lines')
    print(id, title, '...............')
    obj = get_object_or_404(Blog, id = comm_id)
    obj.title = title
    obj.description = description
    obj.tags = tags
    obj.publisher = publisher
    obj.no_lines = no_lines
    obj.save()

    return render(request, 'pages/all_blogs_view.html', {'success': "Blog updated..."})

def viewBlog(request, id):
    get_blog = Blog.objects.get(id = id)
    comments = Comment.objects.filter(blog = get_blog)
    return render(request, 'pages/view-blog.html', {'blog_data': get_blog, 'comments_data': comments})

def addComment(request):
    g_comment = request.GET.get('msg')
    g_blog = Blog.objects.get(id = request.GET.get('id'))
    print('........'+str(request.user))
    g_user = request.user
    if str(request.user) != 'AnonymousUser':
        obj = Comment.objects.create(comment = g_comment, user = request.user, blog = g_blog)
        obj.save()
    else:
        obj = Comment.objects.create(comment = g_comment, blog = g_blog, user = get_object_or_404(User, pk = 2))
        obj.save()
    comments = Comment.objects.filter(blog = g_blog)
    return render(request, 'pages/view-blog.html', {'blog_data': g_blog, 'comments_data': comments})