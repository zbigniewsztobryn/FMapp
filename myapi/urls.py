from django.urls import path
from .views import *
from django.conf.urls import url, include
from django.contrib import admin
from .api import router


#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
#    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('addfile/', AddFileView.as_view()),
    path('', SearchView.as_view()),
    url(r'fmapp/', admin.site.urls),
    url(r'dbapi/', include(router.urls))
    #re_path(r'^handles3downloads/([^/]+)/$', handles3downloads, name='myapi.views.handles3downloads')
]
#, name='myapi.views.handles3downloads'