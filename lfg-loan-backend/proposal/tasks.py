from celery import shared_task
import requests
from .models import Proposal

@shared_task()
def check_credit_approval(document, name, proposal_id):
    response = requests.post('https://loan-processor.digitalsys.com.br/api/v1/loan/', json={'document': document, 'name': name})
    proposal = Proposal.objects.get(pk=proposal_id)
    print(response.json())
    print(response.json()['approved'])
    if response.json()['approved'] == 'Approved':
        proposal.status = 'Automatically Approved'
    else:
        proposal.status = 'Automatically Denied'
    proposal.save()
