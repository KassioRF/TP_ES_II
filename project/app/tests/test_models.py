from django.test import TestCase
from datetime import datetime

from app.models import Data

# Classe de testes par o modelo Data
class ModelsTestCase(TestCase):
  
  def test_get_date(self):
    """ Verifica se o método get_date retorna a representação da data no formato dd/mm/yy"""
    #formato da data armazenado no modelo : dd,mm,yy
    date = datetime(2022,6,4)
    data = Data(mode="spent", value=20, date=date)

    self.assertEqual("04/06/22", data.get_date())

  def test_get_value(self):
    """Verifica se o método get_value retorna a representação do valor no formato de cotação x,xxx.dd """
    data = Data(mode="spent", value=1234.56, date=datetime.today())

    self.assertEqual("1,234.56", data.get_value())

