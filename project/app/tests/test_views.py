from django.test import TestCase
from app.models import Data


class ViewsTestCase(TestCase):
  #teste rotas de remoção
  def test_remove_data_invalid(self):
    """Força o tratamento da exceção de item não existente no banco de dados"""
    route = 'http://127.0.0.1:8000/del/ajax/data/0'
    response=self.client.get(route)
    self.assertEqual(response.status_code, 400)


  def test_remove_dtype_invalid(self):
    """Força o tratamento da exceção de item não existente no banco de dados"""
    route = 'http://127.0.0.1:8000/del/ajax/type/0'
    response=self.client.get(route)
    self.assertEqual(response.status_code, 400)
