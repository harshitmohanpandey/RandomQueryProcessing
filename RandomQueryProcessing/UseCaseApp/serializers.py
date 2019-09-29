from rest_framework import serializers

class UseCaseData(serializers.Serializer):
    date = serializers.CharField()
    group_by_columns = serializers.CharField(max_length=200)
    sortorder = serializers.CharField(max_length=200)