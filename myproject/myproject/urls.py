from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'))#rota padrão para app criado include pega todas subURL's app users
]
