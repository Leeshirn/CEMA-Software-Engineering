from rest_framework import serializers
from .models import Client, HealthProgram

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name']


class ClientSerializer(serializers.ModelSerializer):
    programs = HealthProgramSerializer(many=True, read_only=True)
    program_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=HealthProgram.objects.all(), write_only=True, source='programs'
    )

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'programs', 'program_ids']
