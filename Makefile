BACK_PATH = app/back/
FRONT_PATH = app/front/

PYTHON_VENV = $(BACK_PATH)venv/bin/python
DJANGO = $(BACK_PATH)manage.py
LOCAL = --settings=config.django.local

APP ?= api

runbackserver:
	$(PYTHON_VENV) $(DJANGO) runserver $(LOCAL)

makemigrations:
	$(PYTHON_VENV) $(DJANGO) makemigrations $(APP)

migrate:
	$(PYTHON_VENV) $(DJANGO) migrate $(APP)

showmigrations:
	$(PYTHON_VENV) $(DJANGO) showmigrations $(APP)

shell:
	$(PYTHON_VENV) $(DJANGO) shell

test:
	$(PYTHON_VENV) $(DJANGO) test

mkrequirements:
	$(PYTHON_VENV) -m pip freeze > $(BACK_PATH)requirements.txt

runfrontserver:
	cd $(FRONT_PATH) && yarn dev

build:
	cd $(FRONT_PATH) && yarn build

lint:
	cd $(FRONT_PATH) && yarn lint