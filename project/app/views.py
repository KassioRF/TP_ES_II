from django.shortcuts import render

from datetime import date, datetime
# Create your views here.

def index(request):
  date_today = date.today().strftime("%d/%m/%y")
  return render(request, 'app/index.html', {
    'date_today': date_today
  })