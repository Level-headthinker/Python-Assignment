# views.py
from django.shortcuts import render, redirect,get_object_or_404
# from .models import Blog
blogs=[]
def blogpage(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        image = request.FILES.get("image")
        # Blog.objects.create(title=title, desc=desc, image=image)
        blog_data={'id':len(blogs)+1,'title':title,'desc':desc,'image':image}
        blogs.append(blog_data)
        return redirect("Listpage")
    return render(request, 'blogpage/blogpage.html')

def Listpage(request):
    # blogs = Blogs.objects.all()
    return render(request, 'blogpage/Listpage.html', {'blogs': blogs})

def detailpage(request, blog_id):
    # blog = get_object_or_404(Blog, id=blog_id)
    blog = next((blog for blog in blogs if blog['id'] == blog_id), None)
    if not blog:
        return redirect("Listpage")  # Redirect to list if blog not found
    
    return render(request, 'blogpage/detailpage.html', {'blog': blog})
