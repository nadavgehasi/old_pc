from rest_framework import serializers

from .models import Server, System, Team


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('name', 'base', 'status', 'tag', 'team', 'systems', 'cpu_cores', 'memory_total', 'memory_used',
                  'memory_percent')


class SystemSerializer(serializers.ModelSerializer):
    servers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = System
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    systems = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    servers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
