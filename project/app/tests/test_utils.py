from django.test import TestCase
from datetime import datetime

from app.models import Data
from app.utils import calc_balance

from django_mock_queries.query import MockSet, MockModel

class UtilsTestCase(TestCase):
  def test_calc_balance(self):
    """Com base em um conjunto de registros deve retornar um dicionário as informações de gasto,saldo e balanço"""
    #define dados para teste
    date = datetime(2022,6,4)
    data = MockSet (
      MockModel(mode="spent", value=10.50, date=date),
      MockModel(mode="spent", value=4.50, date=date),
      MockModel(mode="profit", value=20.00, date=date),
      MockModel(mode="profit", value=20.00, date=date),
    )

    

    balance = {'spent': "15.00",
              'profit':  "40.00",
              'balance': "25.00"}

    self.assertEqual(balance, calc_balance(data))

  