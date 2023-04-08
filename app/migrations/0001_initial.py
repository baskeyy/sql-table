# Generated by Django 4.1.7 on 2023-04-08 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('DEPTNO', models.IntegerField(primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=50)),
                ('DLOC', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('EMPNO', models.IntegerField(primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=50)),
                ('JOB', models.CharField(max_length=50)),
                ('MGR', models.IntegerField()),
                ('HIREDATE', models.DateField()),
                ('SAL', models.IntegerField()),
                ('COMM', models.IntegerField(null=True)),
                ('DEPTNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]