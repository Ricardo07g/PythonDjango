from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
]
'''
urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
    re_path(r'^weblog/', include('blog.urls')),
    ...

         path('index/', views.index, name='index'),
    path('page2/', views.page2, name='Page2'),
]
'''