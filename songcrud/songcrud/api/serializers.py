from musicapp.models import *
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'date_released', 'likes', 'artiste_id')

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('id', 'first_name', 'last_name', 'age')

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ('id', 'content', 'song_id')