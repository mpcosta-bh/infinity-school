from django.shortcuts import get_object_or_404 #metodo manipulação bsase dados
from django.views import View
from django.http import JsonResponse
from .models import User #classe users
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class UserListView(View): #Listar todos users
    def get(self,request):
        users = list(User.objects.values())
        return JsonResponse(users,safe=False)



@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(View): #Criar novo usuário
    def post(self,request):
        data = json.loads(request.body)

        #criar o usuário

        user = User.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            date_of_birth = data['date_of_birth'],
            enrollment_date = data['enrollment_date']
            
        )
        return JsonResponse({'id':user.id},status = 201)
        
@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(View): # Listar especific user
    def get(self,request,user_id):
        user = get_object_or_404(User,id=user_id)
        data = {
            'id':user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_of_birth': user.date_of_birth,
            'enrollment_date': user.enrollment_date
            
        }

        return JsonResponse(data,safe=False)


    def put(self,request,user_id):
        user = get_object_or_404(User,id=user_id)
        data = json.loads(request.body)
        user.first_name=data.get('first_name',user.first_name)
        user.last_name_name=data.get('last_name',user.last_name)
        user.date_of_birth=data.get('date_of_birth',user.date_of_birth)
        user.enrollment_date=data.get('enrollment_date',user.enrollment_date)
        user.save()
        return JsonResponse({'id':user.id},status=200)

    def delete(self,request,user_id):
        user = get_object_or_404(User,id=user_id)
        user.delete()
        return JsonResponse({'message':'User deleted'},status=204)