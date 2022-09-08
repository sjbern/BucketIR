from django.contrib import admin
from django.urls import path, include
from users import views as user_views
admin.site.site_url = 'http://localhost:8000/home/'  # changes the 'View Site' link to homepage, update once hosted
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #these links are for independet folders
    path('admin/', admin.site.urls),
    path('home/', include('bucket.urls')),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('setting/', include('setting.urls')),
    path('register/', include('users.urls')),
    
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
