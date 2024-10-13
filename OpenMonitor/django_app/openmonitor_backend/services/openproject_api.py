# openmonitor_backend/services/openproject_api.py

import os
import requests
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

BASE_URL = 'https://ofiwebsubdir.ugr.es/openproject/api/v3'

# Obtener el token codificado desde la variable de entorno
OPENPROJECT_API_TOKEN_BASE64 = os.getenv('OPENPROJECT_API_TOKEN_BASE64')

# Crear los headers con el token
HEADERS = {
    'Authorization': OPENPROJECT_API_TOKEN_BASE64
}


# Mapa de proyectos
def get_project_map():
    url = f"{BASE_URL}/projects"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        projects = response.json()
        project_map = {project['id']: project['name'] for project in projects['_embedded']['elements']}
        return project_map
    else:
        return {"error": "Error al obtener proyectos", "status_code": response.status_code}

# Obtener todos los proyectos
def get_projects():
    url = f"{BASE_URL}/projects/"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Error al obtener proyectos", "status_code": response.status_code}

# Obtener un proyecto específico
def get_project(project_id):
    url = f"{BASE_URL}/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error al obtener el proyecto {project_id}", "status_code": response.status_code}

# Obtener todos los work packages de un proyecto
def get_work_packages(project_id):
    url = f"{BASE_URL}/projects/{project_id}/work_packages"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error al obtener los work packages del proyecto {project_id}", "status_code": response.status_code}
    
# Obtener todos los subproyectos de un proyecto
def get_subproject(project_id):
    url = f"{BASE_URL}/projects/{project_id}/subprojects"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error al obtener los subproyectos del proyecto {project_id}", "status_code": response.status_code}

#Obtener todos los usuarios
def get_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Error al obtener usuarios", "status_code": response.status_code}

# Obtener detalles de un usuario específico
def get_users(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error al obtener el usuario {user_id}", "status_code": response.status_code}

# funcion que dado un nombre de usuario, devuelve el id de ese usuario
def get_user_id_by_name(user_name):
    url = f"{BASE_URL}/users?filters=[{{\"name\":{{\"operator\":\"=\",\"values\":[\"{user_name}\"]}}}}]"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        user = response.json()
        if user['_embedded']['elements']:
            return user['_embedded']['elements'][0]['id']
        else:
            return {"error": f"No se ha encontrado el usuario {user_name}"}
    else:
        return {"error": f"Error al obtener el usuario {user_name}", "status_code": response.status_code}


# Obtener los work packages asignados a un usuario
def get_work_packages_by_user_id(user_id):
    url = f"{BASE_URL}/work_packages?filters=[{{\"assignee\":{{\"operator\":\"=\",\"values\":[\"{user_id}\"]}}}}]"
    response = requests.get(url, headers=HEADERS)
    return response.json()

# Obtener los work packages asignados a un usuario por su nombre
def get_work_packages_by_user_name(user_name):
    user_id = get_user_id_by_name(user_name)
    return get_work_packages_by_user_id(user_id)


# Obtener todas las entradas de tiempo (time entries) para un proyecto
def get_time_entries_for_project(project_id):
    url = f"{BASE_URL}/time_entries?filters=[{{\"project\":{{\"operator\":\"=\",\"values\":[\"{project_id}\"]}}}}]"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.status_code == 200 else {"error": f"Error al obtener entradas de tiempo para el proyecto {project_id}"}

# Obtener todos los proyectos en los que un usuario específico participa
def get_projects_for_user(user_id):
    url = f"{BASE_URL}/work_packages?filters=[{{\"assignee\":{{\"operator\":\"=\",\"values\":[\"{user_id}\"]}}}}]"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.status_code == 200 else {"error": f"Error al obtener proyectos para el usuario {user_id}"}

# Obtener el número de paquetes retrasados de un proyecto
def get_delayed_work_packages(project_id):
    url = f"{BASE_URL}/projects/{project_id}/work_packages"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        work_packages = response.json()['_embedded']['elements']
        delayed_packages = [wp for wp in work_packages if wp['dueDate'] < wp['updatedAt'] and wp['percentageDone'] < 100]
        return len(delayed_packages)
    return {"error": f"Error al obtener paquetes retrasados para el proyecto {project_id}"}

# Obtener número de paquetes completados en tiempo
def get_completed_on_time_work_packages(project_id):
    url = f"{BASE_URL}/projects/{project_id}/work_packages"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        work_packages = response.json()['_embedded']['elements']
        completed_on_time = [wp for wp in work_packages if wp['dueDate'] >= wp['updatedAt'] and wp['percentageDone'] == 100]
        return len(completed_on_time)
    return {"error": f"Error al obtener paquetes completados en tiempo para el proyecto {project_id}"}



