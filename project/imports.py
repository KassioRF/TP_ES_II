from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta

from app.models import Data, DType

def imports():
  format = "%Y-%m-%d"


  n = -4
  print(range(n,0))
  date = "2022-06-03"
  dateinit = datetime.strptime(date,format)
  dateend = dateinit + relativedelta(months=n)
  
  profit = "profit"
  spent = "spent"
  

  #Ganhos
  
  #salario
  sal = "Salário"
  value = 1800
  dtype = DType.objects.get(dtype=sal)
  
  
  date = dateend
  data = Data(mode=profit, value=value, date=date ,dtype=dtype)
  data.salve()



  #Spent
  #Aluguel
  # aluguel = "Aluguel"
  # value = 600
  # dtype = Dtype.objects.get(dtype=aluguel)

  # date = dateend
  # data = Data(mode=spent, value=value, date=date ,dtype=dtype)
  # data.salve()
  
#Gastos
  
  
  
  pass
