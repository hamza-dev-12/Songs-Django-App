from .models import Genre, Song, Collection
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.contrib.auth import authenticate


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Replace username field with email field
        self.fields.pop("username", None)
        self.fields["email"] = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("No account found with this email.")

            # Check if password is correct
            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect password.")

            if not user.is_active:
                raise serializers.ValidationError("User account is disabled.")

            # Set username for token generation
            attrs["username"] = user.username

            # Remove email from attrs since parent expects username
            attrs.pop("email")

        return super().validate(attrs)


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
            "username": {"required": True},
            "email": {"required": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"email": {"required": True}, "password": {"required": True}}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class CollectionSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(), many=True, required=True
    )

    class Meta:
        model = Collection
        fields = ["id", "user", "collection_name", "songs"]
        extra_kwargs = {
            "user": {"required": True},
            "collection_name": {"required": True},
            "songs": {"required": True},
        }


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "type"]
        extra_kwargs = {"type": {"required": True}}


class SongSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), required=True
    )

    class Meta:
        model = Song
        fields = ["id", "song_name", "singer_name", "published_date", "genres"]

        extra_kwargs = {
            "song_name": {"required": True},
            "singer_name": {"required": True},
            "published_date": {"required": True},
            "genres": {"required": True},
        }
