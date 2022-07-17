# Generated by Django 4.0.1 on 2022-02-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0003_album_cover_image_song_file_alter_album_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='cover_image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Rock', 'Rock'), ('Bollybood', 'BollyBood'), ('Folk', 'Folk'), ('Techno', 'Techno'), ('Country', 'Country'), ('Hip Hop Music', 'Hip Hop Music'), ('Classical', 'Classical'), ('Pop Music', 'Pop Music')], max_length=50),
        ),
    ]
