

from django.contrib import admin
from django.urls import include, path
from task_app import views

urlpatterns = [
    path('',views.main_home.as_view(),name='home_page'),
    path('login/',views.Login_page.as_view(),name='login_page'),
    path('admin_home/',views.admin_home.as_view(),name='admin_home'),
    path('admin_manage_user/',views.admin_manage_user.as_view(),name='admin_manage_user'),
    path('admin_update_user/<int:id>', views.update_user.as_view(), name='update_user'),
    path('delete_user/<int:id>', views.delete_user.as_view(), name='delete_user'),
    path('delete_task/<int:id>', views.delete_task.as_view(), name='delete_task'),
    path('manage_task/',views.manage_task.as_view(),name='manage_task'),
    path('admin_task_assign/<int:id>', views.assgin_task.as_view(), name='admin_task_assign'),
    path('assign_task_to_user/<int:id>', views.assign_task_to_user.as_view(), name='assign_task_to_user'),
    path('admin_view_assigned_users/<int:id>',views.admin_view_assigned_users.as_view(),name='admin_view_assigned_users'),

    path('user_home/',views.user_home.as_view(),name='user_home'),
    path('user_user_view_assigned_tasks/',views.user_view_assigned_tasks.as_view(),name='user_view_assigned_tasks'),
    path('user_updated_task_status/<int:id>',views.user_updated_task_status.as_view(),name='user_updated_task_status'),


]
