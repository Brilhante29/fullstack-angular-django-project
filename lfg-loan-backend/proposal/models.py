from django.db import models

class Proposal(models.Model):
    status_choices = [
        ('Pending', 'Pending'),
        ('Automatically Approved', 'Automatically Approved'),
        ('Automatically Denied', 'Automatically Denied'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied')
    ]
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    status = models.CharField(max_length=30, choices=status_choices, default='Pending')
    data = models.JSONField()

    def __str__(self):
        return self.name

class ProposalField(models.Model):
    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50, choices=[('Text', 'Text'), ('Number', 'Number')])
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.name