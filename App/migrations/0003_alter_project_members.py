# Generated by Django 3.2 on 2022-02-06 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_project_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='Les_membres', through='App.MemberShipInProject', to='App.Etudiant'),
        ),
    ]