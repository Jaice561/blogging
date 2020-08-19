from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import blogPost
from .forms import ContactForm
from .forms import blogPostModelForm
# Create your views here.

def blog_list_view(request):
    qs = blogPost.objects.all().published()
    template_name = 'blog_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

@login_required(login_url='/login')
@staff_member_required
def blog_create_view(request):
    form = blogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = blogPostModelForm()
    template_name = 'form.html'
    context = {"form": form}
    return render(request, template_name, context)

def blog_detail_view(request, slug):
    obj = get_object_or_404(blogPost, slug=slug)
    template_name = 'blog_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

@login_required(login_url='/login')
@staff_member_required
def blog_update_view(request, slug):
    obj = get_object_or_404(blogPost, slug=slug)
    form = blogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form': form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)

@login_required(login_url='/login')
@staff_member_required
def blog_delete_view(request, slug):
    obj = get_object_or_404(blogPost, slug=slug)
    template_name = 'blog_delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"object": obj}
    return render(request, template_name, context)

def home(request):
    title = "Hello there...."
    qs = blogPost.objects.all()[:5]
    context = {"title": "Welcome to my blog website", "blog_list": qs}
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


