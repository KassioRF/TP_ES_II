from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from datetime import date, datetime

import pprint

# Create your views here.



def index(request):
  spent_types = ["água", "luz", "internet", "telefone", "boleto", "outros"]
  
  date_today = date.today().strftime("%d/%m/%y")
  return render(request, 'app/index.html', {
    'date_today': date_today,
    'spent_types': spent_types
  })


def add_spent(request):
  print(pprint.pformat(request))
  if request.method == "POST":
    #get form data
    print(request.POST)

    
    return JsonResponse({"status": "ok"}, status=200)
  
  
  else:
    return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)

  return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)



def add_profit(request):
  pass