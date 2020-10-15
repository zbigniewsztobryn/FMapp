from django.urls import include, path, re_path
from rest_framework import routers
from . import views
from .views import *

#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
#    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('addfile/', AddFileView.as_view()),
    path('', SearchView.as_view()),
    #re_path(r'^handles3downloads/([^/]+)/$', handles3downloads, name='myapi.views.handles3downloads')
]
#, name='myapi.views.handles3downloads'