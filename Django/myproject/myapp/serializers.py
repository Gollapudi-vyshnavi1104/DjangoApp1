from rest_framework import serializers

from myapp.models import Asset #, Segment, Route, County,Division

  
class AssetSerializer(serializers.ModelSerializer):

    class Meta:  
        model = Asset
        fields = '__all__'
