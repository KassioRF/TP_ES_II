from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta

from app.models import Data, DType

def imports():
  format = "%Y-%m-%d"


  n = -3
  print(range(n,0))
  date = "2022-06-03"
  dateinit = datetime.strptime(date,format)
  dateend = dateinit + relativedelta(months=n)
  
  profit = "profit"
  spent = "spent"
  

  #Ganhos
  
  #salario
  # sal = "Salário"
  # value = 1800
  # dtype = DType.objects.get(dtype=sal)
  



  # Spent
  # Aluguel
  # date = "2022-06-07"
  # dateinit = datetime.strptime(date,format)

  # aluguel = "Aluguel"
  # value = 600
  # dtype = DType.objects.get(dtype=aluguel)

  # date = "2022-05-10"
  # dateinit = datetime.strptime(date,format)

  # cat = "Internet"
  # value = 109.90
  # dtype = DType.objects.get(dtype=cat)


  # date = "2022-06-04"
  # dateinit = datetime.strptime(date,format)

  # cat = "Mercado"
  # value = 480.20
  # dtype = DType.objects.get(dtype=cat)



  # date = "2022-05-15"
  # dateinit = datetime.strptime(date,format)

  # cat = "Fatura do Cart."
  # value = 227.64
  # dtype = DType.objects.get(dtype=cat)


  for d in range(n,1):
    date = dateinit + relativedelta(months=d)
    data = Data(mode=spent, value=value, date=date ,dtype=dtype)
    data.save()



  # date = dateend
  # data = Data(mode=spent, value=value, date=date ,dtype=dtype)
  # data.salve()
  
#Gastos
  
  
  
  pass
