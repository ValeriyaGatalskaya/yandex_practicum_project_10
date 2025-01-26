import configuration
import data
import requests

# Создаем нового пользователя
def post_new_user(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # Формируем полный URL
        json=body,  # Тело запроса
        headers=data.headers  # Заголовки
    )
    if response.status_code != 200:
        print(f"Error creating user: {response.status_code} - {response.text}")
    return response

# Получаем токен авторизации
def get_auth_token():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        headers=data.headers
    )
    if response.status_code != 200:
        print(f"Error getting auth token: {response.status_code} - {response.text}")
        return None  # Возвращаем None в случае ошибки
    return response.json().get('token')  # Возвращаем токен

# Создаем новый набор
def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
        json=kit_body,
        headers=headers
    )
    if response.status_code != 200:
        print(f"Error creating client kit: {response.status_code} - {response.text}")
    return response
