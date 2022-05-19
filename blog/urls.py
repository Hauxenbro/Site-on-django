from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', cache_page(15)(Home_blog.as_view()), name='home'),
    path('cats/<int:category_id>/', cache_page(15)(Category_view.as_view()),name='category'),
    path('article/<int:pk>/', Art_view.as_view(), name='article_view'),
    path('add_article/', AddArticle.as_view(), name='add_art'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('email/', contact_us, name='email'),
    path('author/', about_auth, name='author'),
]