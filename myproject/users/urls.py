from django.urls import path
from .views import UserListView,UserCreateView,UserDetailView

urlpatterns = [

path('/',UserListView.as_view(),name='user-list'),
path('create/',UserCreateView.as_view(),name='user-create'),
path('<int:user_id>',UserDetailView.as_view(),name='user-detail')

]