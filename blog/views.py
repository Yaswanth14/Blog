import email
from django.shortcuts import render, HttpResponse, redirect
from blog.models import Blog, Contact
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    messages.success(request, "Welcome to SnoozeWrites")
    return render(request, 'index.html')

def blog(request):
    no_of_posts = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    # print(page)

    '''
    0-3, 3-6, 6-9

    (pageno-1)*no_of_posts to (pageno)*no_of_posts
    '''
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts : page*no_of_posts]
    if page>1:
        prev = page-1
    else:
        prev = None

    if page<ceil(length/no_of_posts):
        nxt = page+1
    else:
        nxt = None


    context = {'blogs': blogs, 'prev': prev, 'nxt':nxt}
    return render(request, 'bloghome.html', context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug = slug).first()
    context = {'blog': blog}

    return render(request, 'blogpost.html', context)

def search(request):
    # allPosts = Blog.objects.all()
    query = request.GET['query']
    if(len(query)>78):
        allPosts = Blog.objects.none()
    else:
        allPostsTitle = Blog.objects.filter(title__icontains=query)
        allPostsContent = Blog.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, "Please search with correct keyword")
    
    params = { 'allPosts': allPosts, 'query':query}
    return render(request, 'search.html', params)

def contact(request):
    messages.success(request, "Welcome to contact")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")

        if len(name)<2 or len(email)<3 or len(desc)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            instance = Contact(name=name, email=email, desc=desc)
            instance.save()
            messages.success(request, "Your message has been recieved :)")


    return render(request, 'contact.html')


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been created successfully")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")