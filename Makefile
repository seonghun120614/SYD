BACK_PATH = app/back/
FRONT_PATH = app/front/


PYTHON_VENV = $(BACK_PATH)venv/bin/python
DJANGO = $(BACK_PATH)manage.py
LOCAL = --settings=config.django.local

runback:
	$(PYTHON_VENV) $(DJANGO) runserver $(LOCAL)

mkmigrations:
	$(PYTHON_VENV) $(DJANGO) makemigrations $(APP)

migrate:
	$(PYTHON_VENV) $(DJANGO) migrate $(APP)

showmigrations:
	$(PYTHON_VENV) $(DJANGO) showmigrations $(APP)

shell:
	$(PYTHON_VENV) $(DJANGO) shell

test:
	$(PYTHON_VENV) $(DJANGO) test

mkrqms:
	$(PYTHON_VENV) -m pip freeze > $(BACK_PATH)requirements.txt

install:
	$(PYTHON_VENV) -m pip install -r $(BACK_PATH)requirements.txt

reset:
	find $(BACK_PATH)api/migrations/ -not -name '__init__.py' -delete
	find $(BACK_PATH)db.sqlite3

downloadmodule:
	$(PYTHON_VENV) -m pip install $(MODULE)

runfront:
	cd $(FRONT_PATH) && yarn dev

build:
	cd $(FRONT_PATH) && yarn build

lint:
	cd $(FRONT_PATH) && yarn lint

sas:
	sass --update ${FRONT_PATH}src