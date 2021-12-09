from django.test import TestCase
from accounts.models import User


class TestUserModel(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.user_data = dict(
            username='daeppe',
            password='123456',
            first_name='Daniel',
            last_name='Epichin',
            email='d.pena@hotmail.com',
            cep='29215040',
            complement='Apartamento em cima da garagem.',
            number_house='35',
            references='Em frente a auto escola Guarapari.'
        )

        cls.new_user = User.objects.create_user(**cls.user_data)

    def test_user_fields(self):
        """
        Teste dos campos da model.
        """

        # Teste do tipo do username e saida correta
        self.assertIsInstance(self.new_user.username, str)
        self.assertEqual(
            self.new_user.username,
            self.user_data['username']
        )

        # Teste do tipo do password e saida correta
        self.assertIsInstance(self.new_user.password, str)

        # Teste do tipo do first_name e saida correta
        self.assertIsInstance(self.new_user.first_name, str)
        self.assertEqual(
            self.new_user.first_name,
            self.user_data['first_name']
        )

        # Teste do tipo do last_name e saida correta
        self.assertIsInstance(self.new_user.last_name, str)
        self.assertEqual(
            self.new_user.last_name,
            self.user_data['last_name']
        )

        # Teste do tipo do email e saida correta
        self.assertIsInstance(self.new_user.email, str)
        self.assertEqual(
            self.new_user.email,
            self.user_data['email']
        )

        # Teste do tipo do cep e saida correta
        self.assertIsInstance(self.new_user.cep, str)
        self.assertEqual(
            self.new_user.cep,
            self.user_data['cep']
        )

        # Teste do tipo do complement e saida correta
        self.assertIsInstance(self.new_user.complement, str)
        self.assertEqual(
            self.new_user.complement,
            self.user_data['complement']
        )

        # Teste do tipo do number_house e saida correta
        self.assertIsInstance(self.new_user.number_house, str)
        self.assertEqual(
            self.new_user.number_house,
            self.user_data['number_house']
        )

        # Teste do tipo do references e saida correta
        self.assertIsInstance(self.new_user.references, str)
        self.assertEqual(
            self.new_user.references,
            self.user_data['references']
        )
