from rest_framework import serializers

from Fin_App.models import CustomUser, Space, Shit, Spanding

class ShitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shit
        fields = "__all__"

class SpandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spanding
        fields = "__all__"

class UsersSerializer(serializers.ModelSerializer):
    user_space = ShitSerializer(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "telegram_id", "user_space"]

class SpaceSerializers(serializers.ModelSerializer):
    shit_space = ShitSerializer(many=True)
    spanding_space = SpandingSerializer(many=True)
    
    class Meta:
        model = Space
        fields = ["id", "title", "currency", "spanding_space", "shit_space"]