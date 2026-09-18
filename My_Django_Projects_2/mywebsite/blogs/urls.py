from django.urls import path
from . import views

urlpatterns = [
       path("allposts", views.blogposts, name = "allposts")
]