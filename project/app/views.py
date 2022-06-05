from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse

from django.db.models import ProtectedError

from datetime import date, datetime

from app.models import DType, Data
from app.utils import calc_balance, get_str_date, apply_filters

import pprint

# Create your views here.

def index(request):
  
  data = Data.objects.order_by('-date')
  date_range = {'init': '', 'end': date.today().strftime("%d/%m/%y")}
  
  if request.method == 'POST':
    data = apply_filters(data, request.POST)

    if request.POST['init_date']:
      date_range['init'] = get_str_date(request.POST['init_date'])

    if request.POST['end_date']:
      date_range['end'] = get_str_date(request.POST['end_date'])
  
  balance = calc_balance(data)

  spent_types = [t.dtype for t in DType.objects.filter(mode="spent")]
  profit_types = [t.dtype for t in DType.objects.filter(mode="profit")]
  
  return render(request, 'app/index.html', {
    'date_range': date_range,
    'data': data.order_by('-date'),
    'balance': balance,
    'spent_types': spent_types,
    'profit_types': profit_types,
    'dtypes': DType.objects.order_by('dtype')
  
  })


def add_spent(request):
  print("spent")
  if request.method == "POST":
    #get form data
    mode = "spent"
    value = request.POST['value'].replace(".","")
    date = request.POST['date']
    dtype = request.POST['type']
    description = request.POST['description']

    value = value.replace(",",".")
    value = float(value)

    if not DType.objects.filter(dtype=dtype):
      t = DType(dtype=dtype, mode="spent")
      t.save()

    type_ = DType.objects.get(dtype=dtype)
    data_spent = Data(mode=mode, value=value, date=date, dtype=type_, description=description)
    data_spent.save()

    return JsonResponse({"status": "ok"}, status=200)

  else:
    return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)

  return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)



def add_profit(request):
  if request.method == "POST":
    #get form data
    mode = "profit"
    value = request.POST['value'].replace(".","")
    date = request.POST['date']
    dtype = request.POST['type']
    description = request.POST['description']

    value = value.replace(",",".")
    value = float(value)

    if not DType.objects.filter(dtype=dtype):
      t = DType(dtype=dtype, mode=mode)
      t.save()

    type_ = DType.objects.get(dtype=dtype)
    data_spent = Data(mode=mode, value=value, date=date, dtype=type_, description=description)
    data_spent.save()

    return JsonResponse({"status": "ok"}, status=200)
  
  else:
    return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)

  return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)



def add_dtype(request):
  if request.method == "POST":
    dtype = request.POST['dtype']
    mode = request.POST['mode']

    for t in DType.objects.all():
      if t.dtype.upper() == dtype.upper():
        return JsonResponse({"error": "A categoria já existe."}, status=400)
      
    type_ = DType(dtype=dtype, mode=mode)
    type_.save()

    return HttpResponseRedirect('/#cat')
  
  return JsonResponse({"error": "Ops! Ocorreu um erro. Operação não realizada."}, status=400)    



def remove_dtype(request, id):
  print(f"\n\t ---- {id} \n")
  try:
    dtype = DType.objects.get(id=id)
    dtype.delete()
    return HttpResponseRedirect('/#cat')
  except ProtectedError:
    return JsonResponse({"error": "Ops! Não foi possível remover a categoria. Existem registros associados a ela."}, status=400)    
  except DType.DoesNotExist:
    return JsonResponse({"error": "Ops! O item não existe."}, status=400)    



def remove_data(request, id):
  try:
    data = Data.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/')
  
  except Data.DoesNotExist:
    return JsonResponse({"error": "Ops! O item não existe."}, status=400)    