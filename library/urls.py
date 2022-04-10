
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.books_form,name='book_insert'),
    path('<int:id>/',views.books_form,name='book_update'),
    path('list/',views.books_list,name='book_list'),
    path('delete/<int:id>/',views.books_delete,name='book_delete')
]
