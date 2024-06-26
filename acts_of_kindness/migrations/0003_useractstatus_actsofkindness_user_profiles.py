# Generated by Django 4.2.11 on 2024-03-22 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('acts_of_kindness', '0002_actsofkindness_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('act_of_kindness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acts_of_kindness.actsofkindness')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
            options={
                'unique_together': {('profile', 'act_of_kindness')},
            },
        ),
        migrations.AddField(
            model_name='actsofkindness',
            name='user_profiles',
            field=models.ManyToManyField(related_name='acts_of_kindness', through='acts_of_kindness.UserActStatus', to='profiles.userprofile'),
        ),
    ]
