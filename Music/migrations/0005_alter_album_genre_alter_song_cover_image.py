# Generated by Django 4.0.1 on 2022-02-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0004_song_cover_image_alter_album_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Rock', 'Rock'), ('Country', 'Country'), ('Pop Music', 'Pop Music'), ('Classical', 'Classical'), ('Hip Hop Music', 'Hip Hop Music'), ('Folk', 'Folk'), ('Bollybood', 'BollyBood'), ('Techno', 'Techno')], max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='cover_image',
            field=models.ImageField(default='\\static\\img\\diwali-india.jpg', null=True, upload_to=''),
        ),
    ]
