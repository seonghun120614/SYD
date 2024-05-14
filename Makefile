DJANGO = python src/backend/manage.py
LOCAL = --settings=config.settings.local_settings

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