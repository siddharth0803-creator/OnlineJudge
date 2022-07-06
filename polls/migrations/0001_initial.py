# Generated by Django 4.0.5 on 2022-07-02 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=2000)),
                ('Name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=2000)),
                ('difficulty', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=200)),
                ('output', models.CharField(max_length=200)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.problems')),
            ],
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verdict', models.CharField(max_length=20)),
                ('time', models.DateTimeField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.problems')),
            ],
        ),
    ]
