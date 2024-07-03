from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import response
from rest_framework import status
from .models import Router, ONU, DropCable, DropCableUsageRecord
from .serializers import RouterSerializer, ONUSerializer, DropCableSerializer, DropCableUsageRecordSerializer


class RouterListCreateView(generics.ListCreateAPIView):
    queryset = Router.objects.all()
    serializer_class = RouterSerializer

class RouterDetailView(generics.RetriewUpdateDestroyAPIView):
    queryset = Router.objects.all()
    serializer_class = RouterSerializer

class ONUListCreateView(generics.ListCreateAPIView):
    queryset = ONU.objects.all()
    serializer_class = ONUSerializer

class ONUSerializerDetailView(generics.RetriewUpdateDestroyAPIView):
    queryset = ONU.objects.all()
    serializer_class = ONUSerializer


class DropCableListCreateView(generics.ListCreateAPIView):
    queryset = DropCable.objects.all()
    serializer_class = DropCableSerializer

class DropCableDetailView(generics.RetriewUpdateDestroyAPIView):
    queryset = DropCable.objects.all()
    serializer_class = DropCableSerializer


class DropCableUsageRecordListCreateView(generics.ListCreateAPIView):
    queryset = DropCableUsageRecord.objects.all()
    serializer_class = DropCableUsageRecordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        drop_cable = DropCable.objects.get(id=serializer.validated_data['drop_cable'].id)
        length_before_use = serializer.validated_data['length_before_use']
        length_after_use = serializer.validated_data['length_after_use']
        length_used = length_before_use - length_after_use

        if length_used > 0:
            drop_cable.use(length_used)
        else:
            drop_cable.return_item(abs(length_used))

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    class DropCableUsageRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DropCableUsageRecord.objects.all()
    serializer_class = DropCableUsageRecordSerializer