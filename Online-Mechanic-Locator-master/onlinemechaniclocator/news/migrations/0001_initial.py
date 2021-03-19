# Generated by Django 2.1.7 on 2019-03-10 22:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=280)),
                ('reply', models.BooleanField(default=False, verbose_name='Is a reply?')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ('-timestamp',),
            },
        ),
    ]
