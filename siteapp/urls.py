from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index),
    path("error", error),
    re_path(r"^user/(?P<name>\D+)/(?P<folder>\D+)/(?P<folder_num>\d+)", user),
    re_path(r"^user/(?P<name>\D+)/(?P<folder>\D+)", user),
    re_path(r"^user/(?P<name>\D+)", user),
    re_path(r"^user", user),
]
