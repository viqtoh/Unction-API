from rest_framework import serializers
from .models import user

class DataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = user
		fields = ('id','username','firstname','lastname','DOB','mobile','address','state','country')


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=255)
    firstname = serializers.CharField(required=False, allow_blank=True, max_length=255)
    lastname = serializers.CharField(required=False, allow_blank=True, max_length=255)
    email = serializers.CharField(required=False, allow_blank=True,max_length=255)
    DOB = serializers.DateField(required=False)
    mobile = serializers.CharField(required=False, allow_blank=True, max_length=255)
    address = serializers.CharField(required=False, allow_blank=True, max_length=255)
    state = serializers.CharField(required=False, allow_blank=True, max_length=255)
    country = serializers.CharField(required=False, allow_blank=True, max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.DOB = validated_data.get('DOB', instance.DOB)
        instance.email = validated_data.get('email',instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.address = validated_data.get('address',instance.address)
        instance.state = validated_data.get('state',instance.state)
        instance.country = validated_data.get('country',instance.country)
        instance.save()
        return instance