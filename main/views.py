from django.shortcuts import render, get_object_or_404
from .models import blogPost
from .forms import ContactForm
# Create your views here.
def blog_list_view(request):
    qs = blogPost.objects.all()
    template_name = 'blog_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def blog_create_view(request):
    template_name = 'blog_create.html'
    context = {"form": ''}
    return render(request, template_name, context)

def blog_detail_view(request, slug):
    obj = get_object_or_404(blogPost, slug=slug)
    template_name = 'blog_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_update_view(request):
    obj = get_object_or_404(blogPost, slug=slug)
    template_name = 'blog_update.html'
    context = {"object": obj, 'form': ''}
    return render(request, template_name, context)

def blog_delete_view(request):
    obj = get_object_or_404(blogPost, slug=slug)
    template_name = 'blog_delete.html'
    context = {"object": obj}
    return render(request, template_name, context)

def home(request):
    title = "Hello there...."
    context = {"title": title}
    if request.user.is_authenticated:
        context = {"title": title, "list": [1,2,3,4,5]}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", {"title": "About"})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Information", 
        "form": form
    }
    return render(request, "form.html", context)


