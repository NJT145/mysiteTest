from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse

from tags.models import Tag
from .models import BlogEntries
from .forms import BlogForm

def show_blog(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_entry = form.save(commit=False)
            blog_entry.owner = request.user
            blog_entry.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "blog_entries.html", {"blog_entries": BlogEntries.objects.filter(owner=request.user.id),
                                                 "tags": Tag.objects.all(),
                                                 "form": form})

def get_blog_entry(request, entry_id):
    try:
        blog_entry = BlogEntries.objects.get(id=entry_id)
        if request.user.id != blog_entry.owner.id:
            return render(request, "no_user.html")
            #raise PermissionDenied
        return render(request, "one_blog_entry.html", {"blog_entry": blog_entry, "entry_id": entry_id})

    except BlogEntries.DoesNotExist:
        raise Http404("We don't have any.")

@permission_required('is_superuser')
def show_all_blog(request):
    return render(request, "blog_entries.html", {"userType": "super",
                                                 "blog_entries": BlogEntries.objects.all()})

@permission_required('is_superuser')
def show_all_blog_from_user(request, userId):
    return render(request, "blog_entries.html", {"userType": "super",
                                                 "blog_entries": BlogEntries.objects.filter(owner=userId)})
