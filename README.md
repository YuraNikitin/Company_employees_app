# Company_employees_app
1) Необходимо клонировать проект:
  git clone https://github.com/YuraNikitin/Company_employees_app.git
2) Создать и запустить виртуальную среду:
   * virtualenv venv
   * source venv/bin/activate
3) Установить зависимости:
   * pip install -r requirements.txt
4) Создать postgres db и добавить учетные данные в settings.py:
  ```python
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'worker_db',
      'USER': 'postgres',
      'PASSWORD': 'postgres',
      'HOST': 'localhost',
      'PORT': '5432',
      }
   }
  ```
5) Необходимо создать миграции:
   * cd workersenjine
   * python manage.py migrate
6) Создать учетную запись администратора:
   * python manage.py createsuperuser
7) Для запуска необходимо:
   * python manage.py runserver
   
