from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)
# этот файл позволяет администратору управлять моделью Post через интерфейс администратора Django
# после регистрации модели Post в админке, вы сможете добавлять, редактировать и удалять записи этой модели через интерфейс администратора Django
# чтобы увидеть изменения, нужно запустить сервер разработки Django и перейти в админку по адресу http://127.0.0.1:8000/admin/