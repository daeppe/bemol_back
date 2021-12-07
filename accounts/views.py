from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import CreateUserSerializer, GetIdAccountsSerializer


class AccountsView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class AccountsByIdView(ListAPIView):

    queryset = User.objects.all()
    serializer_class = GetIdAccountsSerializer

    lookup_url_kwarg = 'username'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class LoginView(APIView):

    def post(self, request):

        user = authenticate(**request.data)

        if user:
            token = Token.objects.get_or_create(user=user)[0]

            return Response(
                dict(token=token.key),
                status=status.HTTP_200_OK
                )

        return Response(status=status.HTTP_401_UNAUTHORIZED)
