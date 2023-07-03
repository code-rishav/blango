from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.views import PostList,PostDetail
from rest_framework.authtoken import views

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token)
]
urlpatterns = format_suffix_patterns(urlpatterns)