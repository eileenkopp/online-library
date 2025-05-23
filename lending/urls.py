from django.urls import path

from . import views
from .views import profile_view, profile_update


app_name = "lending"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('add/', views.add_book, name='add_book'),
    path('login/', views.login, name='login'),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('collection/create/', views.create_collection, name='create_collection'),
    path('collection/<int:pk>/', views.CollectionDetailView.as_view(), name='collection_detail'),
    path('collection/<int:pk>/delete/', views.CollectionDeleteView.as_view(), name='collection_delete'),
    path('collection/<int:pk>/edit/', views.edit_collection, name='edit_collection'),
    path('collection/<int:pk>/search', views.collection_search_view, name='collection_search'),
    path('collection/', views.collection_list_view, name="collections_list"),
    path('collection/request', views.request_collection_access, name='request_collection_access'),
    path('search/', views.search_view, name='search'),
    path('my-requests/', views.my_book_requests, name='my_book_requests'),
    path('manage-requests/', views.manage_requests, name='manage_requests'),
    path('librarian/add', views.add_librarian, name='add_librarian'),
    path("return/<int:pk>/", views.return_book, name="return_book"),
    path("my-books/", views.my_books, name="my_books"),
    path('book/<int:pk>/review/', views.add_review, name='add_review'),
    path('requests/<int:pk>/cancel/', views.cancel_request, name='cancel_request'),
    path('requests/<int:pk>/delete/', views.delete_request, name="delete_request"),
]
