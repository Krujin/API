# Generated by Django 3.1 on 2020-08-19 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_modelapiview.JSONMixin


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='users', to='api.Offer'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.offer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_modelapiview.JSONMixin, models.Model),
        ),
    ]
