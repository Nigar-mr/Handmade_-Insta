# Generated by Django 2.2.4 on 2019-08-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hm_blog', '0029_auto_20190814_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('job', models.CharField(blank=True, max_length=100, null=True)),
                ('person_story', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='about',
            name='job',
        ),
        migrations.RemoveField(
            model_name='about',
            name='name',
        ),
        migrations.RemoveField(
            model_name='about',
            name='person_story',
        ),
        migrations.AlterField(
            model_name='verification',
            name='token',
            field=models.CharField(default='fZmadsxvsPfWZNQ1XIrNzWzdUonh9EXmgUNXFk3sRWPLTjIUsxM3w9zBw0hyUgRkCCbYqtiAPS3kxC2waCKEqLAVDMU52Bu16ywNlfLOJ2vzzsg6eGwZDJ5H', max_length=120),
        ),
    ]
