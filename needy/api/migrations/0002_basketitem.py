# Generated by Django 3.1 on 2020-08-15 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_modelapiview


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basketitems', to='api.offer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_modelapiview.JSONMixin, models.Model),
        ),
    ]