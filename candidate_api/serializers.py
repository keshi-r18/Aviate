from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'age', 'gender', 'email', 'phone_number']

    def validate_age(self, value):
        if not 18 <= value <= 100:
            raise serializers.ValidationError("Age must be between 18 and 100.")
        return value
