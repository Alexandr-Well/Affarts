import os


import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_factory.settings")
django.setup()

from app_factory.models import Auto
from django.db import connection

a = Auto.objects.filter(name='Nissan').first()
print(a.get_total_price())

print(len(connection.queries), 'db connections')
for sql in connection.queries:
    print(sql)