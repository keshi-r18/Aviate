from rest_framework import viewsets
from .models import Candidate
from .serializers import CandidateSerializer
from .filters import CandidateFilter 

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filterset_class = CandidateFilter
