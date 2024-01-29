from django.urls import path

from online_shop.categories.views import CategoryCreateView, CategoryListView

urlpatterns = [
    path("list/", CategoryListView.as_view()),
    path("create/", CategoryCreateView.as_view()),
]
