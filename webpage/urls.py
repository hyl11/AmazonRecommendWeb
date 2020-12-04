import webpage.views

from django.urls import path, include

urlpatterns = [
    path("hello_world", webpage.views.hello_world)
]