# openmonitor_backend/views.py

from django.http import JsonResponse
from .services.openproject_api import *
from .utils.statistics_utils import *

def user_statistics_view(request, user_id):
    work_packages_data = get_work_packages_by_user_id(user_id)
    total_work_packages = count_work_packages_by_user(user_id, work_packages_data)
    status_distribution = count_work_packages_by_status(work_packages_data)

    return JsonResponse({
        'total_work_packages': total_work_packages,
        'status_distribution': status_distribution,
        # 'average_work_package_duration': average_work_package_duration(work_packages_data)
    })

def project_list(request):
    # obtenemos el mapa de proyectos y lo mostramos por consola
    project_map = get_project_map()
    print(project_map)

    return JsonResponse(get_projects(), safe=False)

def user_list(request):
    # id = get_user_id_by_name("Vanesa Gámiz")
    # users = get_work_packages_by_user_id(id)
    users = get_work_packages_by_user_name("Vanesa Gámiz")
    return JsonResponse(users, safe=False)

def project_detail(request, project_id):
    subproject = get_project(project_id)
    return JsonResponse(subproject, safe=False)

# Vista para obtener proyectos
def projects_view(request):
    projects = get_projects()
    return JsonResponse(projects, safe=False)

# Vista para obtener paquetes de trabajo de un proyecto
def project_work_packages_view(request, project_id):
    work_packages = get_work_packages(project_id)
    return JsonResponse(work_packages, safe=False)

# Vista para obtener estadísticas de un proyecto
def project_statistics_view(request, project_id):
    completion_percentage = calculate_completion_percentage(project_id)
    delayed_percentage = calculate_delayed_percentage(project_id)
    
    stats = {
        "completion_percentage": completion_percentage,
        "delayed_percentage": delayed_percentage
    }
    
    return JsonResponse(stats)

# Vista para obtener los work packages asignados a un usuario
def user_work_packages_view(request, user_id):
    work_packages = get_work_packages_by_user_id(user_id)
    return JsonResponse(work_packages, safe=False)



