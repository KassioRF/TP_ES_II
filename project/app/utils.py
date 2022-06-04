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

