import numpy as np  # O alguna librería de análisis de datos si la necesitas
# importamos los modulos que tenemos en services
from openmonitor_backend.services.openproject_api import *

# Calcular la cantidad total de proyectos
def count_total_projects(projects_data):
    return len(projects_data['_embedded']['elements'])

# Calcular la cantidad total de work packages asignados a un usuario
def count_work_packages_by_user(user_id, work_packages_data):
    return sum(1 for wp in work_packages_data['_embedded']['elements'] if wp['_links']['assignee']['href'].endswith(f"/{user_id}"))

# Calcular la duración promedio de los work packages
def average_work_package_duration(work_packages_data):
    durations = []
    for wp in work_packages_data['_embedded']['elements']:
        duration = wp.get('duration', None)
        if duration:
            durations.append(duration)
    if durations:
        return np.mean(durations)
    else:
        return 0

# Estadísticas de tareas por estado
def count_work_packages_by_status(work_packages_data):
    status_count = {}
    for wp in work_packages_data['_embedded']['elements']:
        status = wp['_links']['status']['title']
        status_count[status] = status_count.get(status, 0) + 1
    return status_count

# Calcular el porcentaje de paquetes completados en un proyecto
def calculate_completion_percentage(project_id):
    work_packages = get_work_packages(project_id)['_embedded']['elements']
    completed = len([wp for wp in work_packages if wp['percentageDone'] == 100])
    total = len(work_packages)
    return (completed / total) * 100 if total > 0 else 0

# Calcular el porcentaje de paquetes retrasados en un proyecto
def calculate_delayed_percentage(project_id):
    total_packages = get_work_packages(project_id)['_embedded']['elements']
    delayed = get_delayed_work_packages(project_id)
    total = len(total_packages)
    return (delayed / total) * 100 if total > 0 else 0
