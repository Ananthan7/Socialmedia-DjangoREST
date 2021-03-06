from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="admin",
                          email="admin1234@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="121212",
                          gender="Male"
                          )
        user.set_password("admin1234")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
