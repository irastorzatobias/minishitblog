from django.test import TestCase, Client
from .models import Entrada, Comentario, CustomUser

class BlogAppTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='user', password='user')
        self.entrada = Entrada.objects.create(titulo='HASBULLAH', contenido='ES UN CAPO', autor=self.user)
        self.comentario = Comentario.objects.create(texto='TENES RAZON', autor=self.user, entrada=self.entrada)

    def test_entrada_list_view_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'HASBULLAH')
        self.assertContains(response, 'ES UN CAPO')
        self.assertContains(response, 'TENES RAZON')

    def test_entrada_delete_view(self):
      self.client.login(username='user', password='user')
      response = self.client.post(f'/entrada/{self.entrada.id}/delete/')
      self.assertEqual(response.status_code, 302)
      self.assertFalse(Entrada.objects.filter(id=self.entrada.id).exists())