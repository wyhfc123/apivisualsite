from rest_framework.serializers import ModelSerializer
from .models import CurrentNumber
class GetChartTwotModelSerializer(ModelSerializer):
    class Meta:
        model=CurrentNumber
        fields="__all__"