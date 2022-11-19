from django.urls import path
from api.views import article_list, index
urlpatterns = [
    path('articles/', article_list),
    path('', index)
]
