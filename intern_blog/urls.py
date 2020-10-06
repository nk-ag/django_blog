from django.urls import path
from . import views

urlpatterns=[
    path('',views.PostListView.as_view(),name="BlogHome"),
    path('category/<str:category>', views.categoryview, name="Category"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="PostDetail"),
    path('post/newpost/', views.PostCreateView.as_view(), name="PostCreate"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="PostDelete"),
    path('about/', views.about, name="BlogAbout")
]
