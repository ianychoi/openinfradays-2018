# Generated by Django 2.0.5 on 2018-05-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0003_programcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='openinfradays.ProgramCategory'),
        ),
    ]
