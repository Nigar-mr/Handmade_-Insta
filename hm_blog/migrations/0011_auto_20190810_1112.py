# Generated by Django 2.2.4 on 2019-08-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hm_blog', '0010_auto_20190809_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Website', models.CharField(blank=True, max_length=255, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('Twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('Linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('Instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('Googleplus', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='verification',
            name='token',
            field=models.CharField(default='LEa6LhXoPtExFXPQ0fPQkdtHCFf6ksOGAzNCERGRHQLDTQhbDM016aFDzftlydJ9d9gZwYBNEi636M5TDq9ScgFyK6bbHa7mXot1xJgdwKASddCpbMhaMjBo', max_length=120),
        ),
    ]
