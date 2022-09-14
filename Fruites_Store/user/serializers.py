from user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)
        instance.save()

        return instance

    def get_user_type(self, obj):
        if obj.type:
            return obj.type
        return "None"
    
    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {
            'password': {'write_only': True}
        }
