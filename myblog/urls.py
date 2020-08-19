from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView,AddPostView

urlpatterns = [
    #path('',views.home, name='home'),
    path('',HomeView.as_view(), name="home"), # this is how we use the classbased views
    path('article/<int:pk>',ArticleDetailView.as_view(), name='article-details'),
    path('addArticle', AddPostView.as_view(), name="add_post"),
]
