from django.contrib import admin
from django.urls import path
from customer.views import UserView, PostView, UserDetailView, PostDetailView, CommentView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/<str:pk>/', UserDetailView.as_view(), name='user-detail'),
    # TODO - nested urls
    path('post/', PostView.as_view()),
    path('post/<str:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:pk>/comment/', CommentView.as_view(), name='post-comment'),
]