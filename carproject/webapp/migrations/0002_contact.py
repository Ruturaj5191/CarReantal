# Generated by Django 5.0.8 on 2024-10-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cemail', models.CharField(max_length=100)),
                ('csubject', models.CharField(max_length=100)),
                ('cmessage', models.CharField(max_length=100)),
                ('ctext', models.CharField(max_length=100)),
            ],
        ),
    ]
