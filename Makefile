DJANGO = python src/backend/manage.py
LOCAL = --settings=config.django.local

runbackserver:
	$(DJANGO) runserver $(LOCAL)

makemigrations:
	$(DJANGO) makemigrations $(LOCAL)

migrate:
	$(DJANGO) migrate $(LOCAL)

startapp:
	$(DJANGO) startapp $(app) $(LOCAL)

test:
	$(DJANGO) test $(LOCAL)