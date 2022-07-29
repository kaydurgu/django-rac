
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from members import views as membersview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('post.urls')),
    path('blog/', include('blog.urls')),
    path('contact/',include('contact.urls')),
    path('password-generator/',include('password_generator.urls')),
    path('register/', membersview.register, name = 'register'),
    path('login/',membersview.login, name = 'login'),
    path('logout/',membersview.logout, name = 'logout'),
    path('members/',include('members.urls')),
    path('contest/',include('contest.urls')),
    path('books/', include('crud.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)