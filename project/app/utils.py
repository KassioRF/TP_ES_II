from app.models import Data



def calc_balance(range=None):
  """
    Range é um par ordenado com 2 datas
    Filter data by range
    Sum mode.profit values
    Sum mode.spent values
    sum spent - proft

    return {proft, spent, balance}
  """
  spent = sum([d.value for d in Data.objects.filter(mode='spent')])
  profit = sum([d.value for d in Data.objects.filter(mode='profit')])
  balance = profit - spent

  return {
    'spent': "{:,.2f}".format(spent),
    'profit': "{:,.2f}".format(profit),
    'balance': "{:,.2f}".format(balance)
  }


# "{:,.2f}".format(self.value)