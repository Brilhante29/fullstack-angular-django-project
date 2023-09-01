from rest_framework import serializers
from .models import Proposal, ProposalField

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

class ProposalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalField
        fields = '__all__'