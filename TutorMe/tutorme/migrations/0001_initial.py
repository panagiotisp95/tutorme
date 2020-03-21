# Generated by Django 2.1.5 on 2020-03-21 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tutorme.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', tutorme.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(verbose_name='rating')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('location', models.CharField(max_length=30, verbose_name='location')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
                'db_table': 'students',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('location', models.CharField(max_length=30, verbose_name='location')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('active', models.BooleanField(default=True)),
                ('rating', models.IntegerField(default=0, verbose_name='rating')),
                ('categories', models.ManyToManyField(blank=True, related_name='teachers', to='tutorme.Category')),
                ('students', models.ManyToManyField(related_name='teachers', to='tutorme.Student')),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
                'db_table': 'teachers',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tutorme.Teacher'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tutorme.Student'),
        ),
    ]
