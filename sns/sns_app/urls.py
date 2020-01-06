from django.contrib import admin
from django.urls import path
from . import views

app_name = "sns_app"

urlpatterns = [
    path('index/', views.thread_index_view, name="index"),
    path("<int:thread_id>/", views.thread_view, name="thread"),
    path("<int:pk>/create_post/", views.CreateResPost.as_view(), name="create_post"),
    path("create_thread/", views.CreateThreadView.as_view(), name="create_thread"),
]
