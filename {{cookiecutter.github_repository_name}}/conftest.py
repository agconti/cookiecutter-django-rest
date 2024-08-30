import pytest

# Ensures pytest waits for the database to load
# https://pytest-django.readthedocs.io/en/latest/faq.html#how-can-i-give-database-access-to-all-my-tests-without-the-django-db-marker
@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass
