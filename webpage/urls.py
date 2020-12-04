import webpage.views

from django.urls import path, include

urlpatterns = [
    path("hello_world", webpage.views.hello_world),
    path("detail/<int:productID>", webpage.views.get_detail),
    path("index/", webpage.views.get_index),
    path("test/", webpage.views.test)
]