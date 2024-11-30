from django.db import models

class User(models.Model):#colunas do bd users=entidade
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name_name} {self.last_name} {self.enrollment_date}" #não obrigatorio
