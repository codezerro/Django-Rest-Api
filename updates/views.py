from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from updates.models import Update
# Create your views here.


def update_model_detail_view(request):

    data = {
        "count": 100,
        "content": "Some new content",
    }
    return JsonResponse(data)
