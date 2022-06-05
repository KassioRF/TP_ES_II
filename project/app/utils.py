from datetime import datetime
from app.models import Data

def calc_balance(data, range=None):
  
  spent = sum([d.value for d in data.filter(mode='spent')])
  profit = sum([d.value for d in data.filter(mode='profit')])
  balance = profit - spent

  return {
    'spent': "{:,.2f}".format(spent),
    'profit': "{:,.2f}".format(profit),
    'balance': "{:,.2f}".format(balance)
  }


def get_str_date(date):
  format = "%d/%m/%y"
  return  datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%y")


def apply_filters(data, filters):
  if filters['mode']:
    data = data.filter(mode=filters['mode'])

  if filters['init_date']:
    data = data.filter(date__gte=filters['init_date'])

  if filters['end_date']:
    data = data.filter(date__lte=filters['end_date'])

  return data