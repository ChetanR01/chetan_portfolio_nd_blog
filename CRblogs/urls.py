from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index" ),
    path('about',views.about, name="about" ),
    path('blog',views.blog, name="blog" ),
    path('search',views.search, name="search" ),
    path('category/<int:id>',views.category, name="category" ),
    path('tag/<int:id>',views.tag, name="tag" ),
    path('post/<int:id>/<str:post_url>',views.post, name="post" ),
    path('contact',views.contact, name="contact" ),
    path('profile',views.profile, name="profile" ),
    path('profile/signup',views.signup, name="signup" ),
    path('profile/login',views.login, name="login" ),
    path('profile/logout',views.logout, name="logout" ),
]