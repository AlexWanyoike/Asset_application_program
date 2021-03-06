# Generated by Django 3.2.9 on 2021-11-28 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='asset_id',
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_model',
            field=models.IntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Application_request',
        ),
        migrations.AddField(
            model_name='applicationrequest',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.asset'),
        ),
    ]
