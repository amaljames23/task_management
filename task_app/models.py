from django.db import models

# Create your models here.


from django.db import models

# Create your models here.




class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)
    def __str__(self):
        return self.username
    
    
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    district=models.CharField(max_length=200)   
    pincode=models.CharField(max_length=200)
    house_no=models.CharField(max_length=200)
    phone_no=models.CharField(max_length=200)
    def __str__(self):
        return self.first_name
    

class task(models.Model):
    task_id=models.AutoField(primary_key=True)
    user_id=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    due_date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)   
    report=models.CharField(max_length=200)
    worked_hr=models.CharField(max_length=200)
    def __str__(self):
        return self.title