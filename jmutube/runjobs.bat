cd \mdid\rooibos
SET ROOIBOS_ADDITIONAL_SETTINGS=apps.jmutube.settings_local_jobs
manage.py runjob crass_sorter
manage.py runjob relay_import
