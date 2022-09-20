from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post
from .models import Zone
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'Zone':Zone.objects.all()
    }
    return render(request, 'bucket/bucket.html', context)

def bucketSet(request):
    return render(request, 'bucket/bucket.html', {'title':'Bucket Settings'})

class ZoneListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class ZoneCreateView(LoginRequiredMixin, CreateView):
    model = Zone
    fields = ['_ID', 'description', 'flow', 'area']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
