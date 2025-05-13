from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from task_app.forms import LoginForm
from .models import *

# Create your views here.



class main_home(View):
    def get(self,request):
        return render(request,'home.html')


class Login_page(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'login.html',{'forms':form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username,password,"//////////")
            try:
                lg=login.objects.get(username=username,password=password)
                request.session['login_id']=lg.pk
                if lg.usertype == 'admin':
                    return HttpResponse("<script>alert('welcome admin');window.location='/admin_home';</script>")
                elif lg.usertype == 'user':
                    users=user.objects.get(login_id=request.session['login_id'])
                    request.session['user']=users.pk
                    return HttpResponse("<script>alert('welcome user');window.location='/user_home';</script>")
            except:
                return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/login';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/login';</script>")
        return render(request,'home.html')


                                                  ## ADMIN SECTION ##


class admin_home(View):
    def get(self,request):
        return render(request,'admin_home.html')

    

class admin_manage_user(View):
    def get(self, request):
        c = user.objects.all()
        return render(request, 'admin_manage_user.html', {'users': c})
    
    def post(self, request):
        uname = request.POST.get('uname')
        psw = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        houseno = request.POST.get('houseno')
        phone = request.POST.get('phone')

        a = login(username=uname, password=psw, usertype='user')
        a.save()
        b = user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            place=place,
            district=district,
            pincode=pincode,
            house_no=houseno,
            phone_no=phone,
            login_id=a.pk
        )
        b.save()

        return HttpResponse("<script>alert('REGISTRATION COMPLETED');window.location='/admin_manage_user'</script>")
    


class update_user(View):
    def get(self,request,id):
        c=user.objects.get(user_id=id)
        print(c,"***************")
        return render(request,'update_user.html',{'a':c})
    
    def post(self,request,id):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        houseno = request.POST.get('houseno')
        phone = request.POST.get('phone')

        c=user.objects.filter(user_id=id).update(first_name=first_name,last_name=last_name,email=email,place=place,district=district,pincode=pincode,house_no=houseno,phone_no=phone)
        
        return HttpResponse("<script>alert('USER UPDATED');window.location='/admin_manage_user'</script>")

class delete_user(View):
    def get(self,request,id):
        c=login.objects.get(login_id=id)
        c.delete()
        return HttpResponse("<script>alert('USER DELETED');window.location='/admin_manage_user'</script>")


class manage_task(View):
    def get(self,request):
        c=task.objects.all()
        return render(request,'manage_task.html',{'tasks':c})
    
    def post(self,request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('date')

        a=task(user_id="0",title=title,description=description,due_date=due_date,status="pending",report="pending",worked_hr="pending")
        a.save()

        return HttpResponse("<script>alert('TASK ADDED');window.location='/manage_task'</script>")
    
class delete_task(View):
    def get(self,request,id):
        c=task.objects.get(task_id=id)
        c.delete()
        return HttpResponse("<script>alert('TASK DELETED');window.location='/manage_task'</script>")


class assgin_task(View):
    def get(self,request,id):
        users=user.objects.all()
        request.session['task']=id
        return render(request,'assign_task.html',{'users':users})
    

class assign_task_to_user(View):
    def get(self,request,id):
        taskid=request.session['task']
        a=task.objects.get(task_id=taskid)
        a.user_id=id
        a.status="Assigned"
        a.save()
        return HttpResponse("<script>alert('TASK ADDED');window.location='/manage_task'</script>")
    

class admin_view_assigned_users(View):
    def get(self,request,id):
        users=user.objects.filter(user_id=id)
        return render(request,'admin_view_assigned_users.html',{'users':users})
    


class user_home(View):
    def get(self,request):
        return render(request,'user_home.html')


class user_view_assigned_tasks(View):
    def get(self,request):
        tasks=task.objects.filter(user_id=request.session['user'])
        return render(request,'user_view_assigned_tasks.html',{'tasks':tasks})


class user_updated_task_status(View):
    def post(self,request,id):
        c=task.objects.get(task_id=id)
        print(c,"***************")
        report = request.POST.get('report')
        hrs = request.POST.get('hrs')
        c.report = report
        c.worked_hr = hrs
        c.status="Completed"
        c.save()
        return HttpResponse("<script>alert('TASK UPDATED');window.location='/user_home'</script>")
    def get(self,request,id):
        return render(request,'user_updated_task_status.html')