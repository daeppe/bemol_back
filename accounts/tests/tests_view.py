from rest_framework.test import APITestCase


class TestAccountView(APITestCase):
    """
    Teste das rotas de accounts.
    """

    def setUp(self) -> None:

        self.user_data = dict(
            username='daeppe',
            password='123456',
            first_name='Daniel',
            last_name='Epichin',
            email='d.pena@hotmail.com',
            complement='Apartamento em cima da garagem.',
            number_house='35',
            references='Em frente a auto escola Guarapari.'
        )

        self.user_login_data = dict(
            username='daeppe',
            password='123456'
        )

        self.user_successful_data = dict(
            id=1,
            username='daeppe',
            first_name='Daniel',
            last_name='Epichin',
            email='d.pena@hotmail.com',
            complement='Apartamento em cima da garagem.',
            number_house='35',
            references='Em frente a auto escola Guarapari.'
        )

        self.url_create = "/api/accounts/"
        self.url_login = "/api/login/"

    def test_create_and_login_user(self):
        """
        Teste de criação e login de usuário.
        """

        # Criação de um usuário.
        new_user = self.client.post(
            self.url_create,
            self.user_data,
            format='json'
        )

        # Teste da criação de um usuário.
        self.assertEqual(201, new_user.status_code)
        self.assertDictEqual(
            new_user.json(),
            self.user_successful_data
        )

        # Login de usuário.
        token = self.client.post(
            self.url_login,
            self.user_login_data,
            format='json'
        ).json()

        self.assertIn('token', token.keys())

    def test_login_non_existing_user(self):
        """
        Teste de login sem usuário.
        """
        # Teste de login sem estar registrado.
        response = self.client.post(
            self.url_login,
            self.user_login_data,
            format='json'
        )

        # Teste da resposta.
        self.assertEqual(response.status_code, 401)

    def test_create_user_already_exists(self):
        """
        Teste de criação de usuário repetido.
        """

        # Criando o usuário duas vezes.
        self.client.post(
            self.url_create,
            self.user_data,
            format='json'
        )

        response = self.client.post(
            self.url_create,
            self.user_data,
            format='json'
        )

        # Teste da resposta.
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            dict(username=["A user with that username already exists."])
        )

    def test_get_user_by_id(self):
        """
        Teste de requisitar um usuário pelo id.
        """

        # Criação do usuário.
        new_user = self.client.post(
            self.url_create,
            self.user_data,
            format='json'
        )

        # Login do usuário.
        token = self.client.post(
            self.url_login,
            self.user_login_data,
            format='json'
        ).json()['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        # Fazendo o request de usuários.
        response = self.client.get(
            f'{self.url_create}{new_user.data["username"]}/',
            format='json'
        )

        # Testes do request.
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json()[0],
            self.user_successful_data
        )
