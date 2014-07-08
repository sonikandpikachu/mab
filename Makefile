#aplication
APPLICATION = mab_django
# settings:
CONFIG = settings.custom
TEST_CONFIG = settings.test
BB_CONFIG = settings.buildbot

# python path:
PYPATH=$(PWD%%/)$(APPLICATION)

# execute scrips:
MAINSCRIPT = django-admin.py
MANAGESCRIPT = PYTHONPATH=$(PYPATH) DJANGO_SETTINGS_MODULE=$(CONFIG) python $(APPLICATION)/manage.py

SCRIPT = PYTHONPATH=$(PYPATH) DJANGO_SETTINGS_MODULE=$(CONFIG) $(MAINSCRIPT)
TEST_SCRIPT = PYTHONPATH=$(PYPATH) DJANGO_SETTINGS_MODULE=$(TEST_CONFIG) $(MAINSCRIPT)
BB_SCRIPT = PYTHONPATH=$(PYPATH) DJANGO_SETTINGS_MODULE=$(BB_CONFIG) $(MAINSCRIPT)


# commands:

test:
	$(TEST_SCRIPT) test $(APP)

run:
	$(SCRIPT) runserver $(PORT)

syncdb:
	$(SCRIPT) syncdb --noinput
	$(SCRIPT) migrate

migrate:
	$(SCRIPT) migrate

manage:
	$(MANAGESCRIPT) $(CMD)

shell:
	$(MANAGESCRIPT) shell

collectstatic:
	$(SCRIPT) collectstatic --noinput

validate:
	$(SCRIPT) validate



