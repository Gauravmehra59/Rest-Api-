from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo-view-set',views.todoviewset,basename='todo')
urlpatterns = [
    path("",views.index,name="index"),
    path("post_todo/",views.postt_todo,name="post_todo"),
    path("get_todo/",views.get_todo,name="get_todo"),
    path("patch_todo/",views.patch_data,name="patch_todo"),

]
urlpatterns += router.urls