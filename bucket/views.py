from django.shortcuts import render
from django.http import HttpResponse
from .models import Create

def home(request):
    context = {
        'Create':Create.objects.all()
    }
    return render(request, 'bucket/bucket.html', context)

def bucketSet(request):
    return render(request, 'bucket/bucket.html', {'title':'Bucket Settings'})
