from django.shortcuts import render
from .models import Post
def renderer(request):

    postdata=Post.objects.get(id=1)
   
      
    context={
        'text':"this is a text",
        'postdata':postdata,
    }
    return render(request,'index.html',context)

def check2ndfile(request):
    return render(request,'checkfile.html')
