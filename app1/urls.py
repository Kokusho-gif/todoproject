from django.contrib import admin
from django.urls import path
from . import views
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('create/', TodoCreate.as_view(), name='create'),
    path('admin/', admin.site.urls),
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update')
]
