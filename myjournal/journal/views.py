from turtle import title
from django.shortcuts import render
from django.urls import reverse
from .models import Entry
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    posts = Entry.objects.all().order_by('-time')
    return render(request,"journal/index.html",{
        "posts":posts
    })


def entry(request):
    # Handle get request
    if request.method == "GET":
        allEntries = Entry.objects.all()
        return render(request, "journal/index.html",{
            "post":allEntries
        })
        
    else:
        # Get post from user
        content = request.POST["newPost"]
        title = request.POST["title"]
        
        # time of Posting
        
        newPost = Entry(
            title=title,
            content=content,
        )
        newPost.save()
        allPosts = Entry.objects.all()
        return HttpResponseRedirect(reverse("index"))
 
 
def delete(request, id):
    entryData = Entry.objects.get(id=id)
    entryData.delete()
    return HttpResponseRedirect(reverse('index'))
    