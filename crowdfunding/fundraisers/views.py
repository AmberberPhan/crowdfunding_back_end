from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import status
from rest_framework.generics import get_object_or_404 #This is another option besides the one in the content
from .models import Fundraiser, Pledge
from .permissions import IsOwnerOrReadOnly
from .permissions import IsSupporterOrReadOnly
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer

class FundraiserList(APIView):
    permission_classes = [
       permissions.IsAuthenticatedOrReadOnly, #this class means Anyone can view this resource, but only logged-in users can change it
       IsOwnerOrReadOnly
    ]
    def get(self, request):
        fundraiser = Fundraiser.objects.filter(is_approved = True) #Changing this from .all to filter so only approved campaign is shown
        serializer = FundraiserSerializer(fundraiser, many = True)
        return Response(serializer.data) #This is like sending the result back to the client
    
    def post(self, request): #This function is responsible for checking our data if its valid
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class FundraiserDetail(APIView):
    permission_classes = [
       permissions.IsAuthenticatedOrReadOnly,
       IsOwnerOrReadOnly
    ]

    def get(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data)
    
    def put(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        self.check_object_permissions(request, fundraiser)
        serializer = FundraiserDetailSerializer(
            instance=fundraiser,
            data=request.data,
            partial=True
        )
        

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    # Adding Fundraiser Delete
    def delete(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        self.check_object_permissions(request, fundraiser)
        fundraiser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        fundraiser_id = request.data.get('fundraiser')
        fundraiser = get_object_or_404(Fundraiser, pk=fundraiser_id)
        
        if not fundraiser.is_open:
            return Response(
                {"detail": "This fundraiser is closed and not accepting new pledges."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]

    def get(self, request, pk):
        pledge = get_object_or_404(Pledge, pk=pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = get_object_or_404(Pledge, pk=pk)
        self.check_object_permissions(request, pledge)

        # Only allow updating comment + anonymous
        data = {
            "comment": request.data.get("comment", pledge.comment),
            "anonymous": request.data.get("anonymous", pledge.anonymous),
        }

        serializer = PledgeSerializer(instance=pledge, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pledge = get_object_or_404(Pledge, pk=pk)
        self.check_object_permissions(request, pledge)
        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
