from rest_framework import serializers
from .models import CustomUser

# For sign up
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

# For edit/delete  
class MeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password"] #Not showing all personal details so it meets certain customer privacy standards for now
        read_only_fields = ["id"]
        
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # update password safely (hash it)
        if password:
            instance.set_password(password)

        instance.save()
        return instance
