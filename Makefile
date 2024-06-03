BACK_PATH = app/back/
FRONT_PATH = app/front/
APP = api

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
	$(PYTHON_VENV) $(DJANGO) test $(BACK_PATH)tests
	rm migrate mkmigrations

mkrqms:
	$(PYTHON_VENV) -m pip freeze > $(BACK_PATH)requirements.txt

install:
	$(PYTHON_VENV) -m pip install -r $(BACK_PATH)requirements.txt

pipinstall:
	$(PYTHON_VENV) -m pip install $(ARG)

reset:
	find $(BACK_PATH)api/migrations/ -not -name '__init__.py' -delete
	rm $(BACK_PATH)db.sqlite3 $(BACK_PATH)media/*.*

downloadmodule:
	$(PYTHON_VENV) -m pip install $(MODULE)

runfront:
	cd $(FRONT_PATH) && yarn dev

build:
	cd $(FRONT_PATH) && yarn build

lint:
	cd $(FRONT_PATH) && yarn lint

.PHONY: watch-sass

watch-sass:
	@echo "Starting SASS watch..."
	@bash -c 'while true; do sass --update app/front/src; sleep 1; done'
