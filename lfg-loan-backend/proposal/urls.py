from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProposalViewSet, ProposalFieldViewSet

router = DefaultRouter()
router.register(r'proposals', ProposalViewSet)
router.register(r'proposal-fields', ProposalFieldViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
