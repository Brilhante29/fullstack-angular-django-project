# Create your views here.
from rest_framework import viewsets
from .models import Proposal, ProposalField
from .serializers import ProposalFieldSerializer, ProposalSerializer
from .tasks import check_credit_approval

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def perform_create(self, serializer):
        proposal = serializer.save()
        check_credit_approval(proposal.document, proposal.name, proposal.id)


class ProposalFieldViewSet(viewsets.ModelViewSet):
    queryset = ProposalField.objects.all()
    serializer_class = ProposalFieldSerializer
