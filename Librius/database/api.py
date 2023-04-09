from rest_framework import viewsets
from .serializers import *
from .models import *

class AuthorAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
class MemberAPI(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MembershipAPI(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer