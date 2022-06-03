from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from datetime import date, datetime

from app.models import DType, Data

import pprint

# Create your views here.



def index(request):
  # spent_types = ["água", "luz", "internet", "telefone", "boleto", "outros"]
  spent_types = [t.dtype for t in DType.objects.filter(mode="spent")]
  
  date_today = date.today().strftime("%d/%m/%y")
  return render(request, 'app/index.html', {
    'date_today': date_today,
    'spent_types': spent_types
  })


def add_spent(request):
  print("spent")
  if request.method == "POST":
    #get form data
    print(request.POST)

    
    return JsonResponse({"status": "ok"}, status=200)
  
  
  else:
    return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)

  return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)



def add_profit(request):
  print("profit")
  if request.method == "POST":
    #get form data
    print(request.POST)

    
    return JsonResponse({"status": "ok"}, status=200)
  
  
  else:
    return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)

  return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)