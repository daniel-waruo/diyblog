# Generated by Django 3.1.6 on 2021-02-06 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(help_text='Some information about you would be great... ', max_length=1000)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(help_text='Type something amazing...', max_length=3000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogger')),
            ],
            options={
                'ordering': ['post_date'],
                'permissions': (('can_edit_blog_post', 'Edit blog post'),),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the category of your blog post (e.g Business, self help...)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.CharField(max_length=200)),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
            ],
            options={
                'ordering': ['comment_date'],
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tag',
            field=models.ManyToManyField(help_text='Select a genre for this blog post', to='blog.Tag'),
        ),
    ]