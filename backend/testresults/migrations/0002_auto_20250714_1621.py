# Generated by Django 5.2.4 on 2025-07-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("DROP TABLE IF EXISTS testresults_testresult;"),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('executed_at', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField(blank=True)),
            ],
        ),
    ]
