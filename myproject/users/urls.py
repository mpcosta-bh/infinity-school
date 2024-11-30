from django.urls import path
from .views import UserListView,UserCreateView,UserDetailView

urlpatterns = [

path('',UserListView.as_view(),name='users-list'),
path('create/',UserCreateView.as_view(),name='users-create'),
path('<int:user_id>/',UserDetailView.as_view(),name='users-detail'),
path('<int:user_id>/delete/',UserDetailView.as_view(),name='users-delete'),
path('<int:user_id>/put/',UserDetailView.as_view(),name='users-put')


]
#Não padrão