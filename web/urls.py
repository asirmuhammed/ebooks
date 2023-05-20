from django.contrib import admin
from django.urls import path
from . import views


app_name="web"

urlpatterns = [
    path('',views.Signup,name="signup"),
    path('',views.Login,name="login"),
    path('',views.Index,name="index"),
    path('books-detail/<int:id>/',views.books_detail,name="books-detail"),
    
]