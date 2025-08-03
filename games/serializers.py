from rest_framework.serializers import ModelSerializer

from games.models import Rating


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('value',)
