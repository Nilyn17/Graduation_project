from rest_framework import serializers

from Fin_App.models import CustomUser, Space, Shit, Spending, SpendingCategory, SpaceLog, ReferalCode


class ShitSerializer(serializers.ModelSerializer):
    space = serializers.SlugRelatedField(slug_field='title', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Shit
        fields = ["user", "space", "user_perk", "is_banned"]

class SpendingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Spending
        fields = ["id", "category", "user", "currency", "expense", "space"]

class UsersSerializer(serializers.ModelSerializer):
    user_space = ShitSerializer(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "telegram_id", "user_space"]

class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "name", "telegram_id"]

class SpaceSerializer(serializers.ModelSerializer):
    shit_space = ShitSerializer(many=True)
    spanding_space = SpendingSerializer(many=True)
    
    class Meta:
        model = Space
        fields = ["id", "title", "currency", "spanding_space", "shit_space"]

class NewSpendingSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    user = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Spending
        fields = ["id", "category", "user", "currency", "expense", "space"]

class CreatingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ["id", "title", "currency"]

class SpendingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingCategory
        fields = ["id", "title", "space"]

class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferalCode
        fields = ["id", "code", "expiration_time", "user", "space"]

class SpaceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceLog
        fields = "__all__"