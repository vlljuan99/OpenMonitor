from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/users/', views.user_list, name='user_list'),
    path('api/projects/<int:project_id>', views.project_detail, name='project_detail'),
    path('api/users/<int:user_id>', views.user_statistics_view, name='user_statistics_view'),
    path('api/projects/', views.projects_view, name='projects'),
    path('api/projects/<int:project_id>/work_packages/', views.project_work_packages_view, name='project_work_packages'),
    path('api/projects/<int:project_id>/statistics/', views.project_statistics_view, name='project_statistics'),
    path('api/users/<int:user_id>/work_packages/', views.user_work_packages_view, name='user_work_packages'),
    path('openmonitor-api/api/users/', views.user_list, name='user_list'),
]

