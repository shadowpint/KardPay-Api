from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from oauth2_provider.models import (
    AccessToken,
    RefreshToken,
    clear_expired
)


def clear_expired_token():
    now = timezone.now()
    AccessToken.objects.filter(expires__lt=now).delete()


def verify_token(data):

    client_id = data['client_id']
    # if client_id not in ['126DhNWthQyVmJ5bREA8KWJimTZuPQZdmbles2h1']:
    if client_id not in ['xrThq5fAdo24B3e962uOre8Uk6HLJ6kwzzMef638','w1yVAis5cNqo4RAXe2HZoYrepyoMfZTkFWS2EmnB','']:
        message = {'message': 'Invalid client id'}
        return message

    if data['signup']:
        user_id = ''
        r = {'message': 'valid', 'user_id': user_id}
        return r
    token = data['access_token']
    client_secret = data['client_secret']
    # clear_expired_token()
    try:
        access_token = AccessToken.objects.get(token=token)
    except ObjectDoesNotExist:
        r = {'message': 'Invalid Token'}
        return r

    if access_token:
        app = access_token.application
        if not access_token.is_expired() and client_id == app.client_id and client_secret == app.client_secret:
            user = access_token.user
            user_id = user.id
            r = {'message': 'valid', 'user_id': user_id}
            return r
        else:
            r = {'message': 'Token may expire or Invalid Client Id/secret'}
            return r

                




