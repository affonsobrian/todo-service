run:
	python todo_service/manage.py runserver

makemigrations:
	python todo_service/manage.py makemigrations

migrate:
	python todo_service/manage.py migrate
