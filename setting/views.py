from django.shortcuts import render

def setting(request):
    return render(request, 'setting/setting.html', {'title':'Settings'})

