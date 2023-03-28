up:
	docker-compose -f docker-compose.dev.yml up
down:
	docker-compose -f docker-compose.dev.yml down
mg:
	docker exec -it temir-backend python3 manage.py migrate
mkmg:
	docker exec -it temir-backend python3 manage.py makemigrations
user:
	docker exec -it temir-backend python3 manage.py createsuperuser
app:
	docker exec -it temir-backend python3 manage.py startapp $(NAME)