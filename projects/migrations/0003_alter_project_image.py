# Generated by Django 5.1.1 on 2024-09-07 20:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_alter_project_image_alter_project_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FilePathField(path="/projects/img"),
        ),
    ]
