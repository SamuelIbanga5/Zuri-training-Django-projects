from musicapp.models import *
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer, ArtisteSerializer, LyricSerializer

class ArtisteAPIView(generics.ListAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class SongAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailsAPIView(generics.ListAPIView):
    serializer_class = SongSerializer
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            return Http404;

    def get(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LyricAPIView(generics.ListAPIView):
    queryset = Lyric.objects.all()
    serializer_class = SongSerializer


