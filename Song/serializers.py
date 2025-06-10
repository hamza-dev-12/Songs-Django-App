from .models import Genre, Song, Collection
from rest_framework import serializers
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ["id", ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        extra_kwargs = {"password": {"write_only": True},
                        "username" : {"required": True},
                        "email" : {"required": True},
                        "password" : {"required": True}
                        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


class CollectionSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(
        queryset = Song.objects.all(),
        many = True,
        required = True
    )
    class Meta:
        model = Collection
        fields = ["id", "user", "collection_name", "songs"]
        extra_kwargs = {
            "user" : {"required": True},
            "collection_name" : {"required": True},
            "songs" : {"required": True},
        }

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "type"]
        extra_kwargs = {"type" : {"required": True}}

class SongSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        required=True
    )

    class Meta:
        model = Song
        fields = ["id",
                "song_name",
                "singer_name" ,
                "published_date",
                "genres"
                ]
        
        extra_kwargs = {
            "song_name": {"required" : True},
            "singer_name": {"required" : True},
            "published_date": {"required" : True},
            "genres": {"required" : True},
            }