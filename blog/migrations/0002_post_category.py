# Generated by Django 2.0.3 on 2018-03-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('cs', 'Computer Science'), ('pj', 'Projects'), ('es', 'Essays')], default='cs', max_length=5),
            preserve_default=False,
        ),
    ]