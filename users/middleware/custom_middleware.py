from django.http import HttpResponseRedirect
from django.urls import reverse
from jwt import decode, ExpiredSignatureError
from datetime import datetime
import os

def auth_middleware(get_response):
    def middleware(request):
        # Sua lógica da middleware aqui
        token = request.COOKIES.get('token')
        if not token:
            return HttpResponseRedirect(reverse('login'))  # Redireciona para a página de login se o token não estiver presente

        try:
            payload = decode(token, os.getenv('SECRET'), algorithms=['HS256'])
            # Verifica se o token ainda não expirou
            if datetime.fromtimestamp(payload['exp']) < datetime.utcnow():
                return HttpResponseRedirect(reverse('login'))  # Redireciona para a página de login se o token estiver expirado
        except ExpiredSignatureError:
            return HttpResponseRedirect(reverse('login'))

        # Se tudo estiver correto, chame a próxima middleware ou a view
        return get_response(request)

    return middleware

