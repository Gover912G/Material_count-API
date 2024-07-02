from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import response
from rest_framework import status
from .models import Router, ONU, DropCable, DropCableUsageRecord