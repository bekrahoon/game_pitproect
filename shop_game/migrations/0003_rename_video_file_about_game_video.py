# Generated by Django 5.0.7 on 2024-07-31 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_game', '0002_remove_game_ditaly_category_about_game_delete_game_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about_game',
            old_name='video_file',
            new_name='video',
        ),
    ]
