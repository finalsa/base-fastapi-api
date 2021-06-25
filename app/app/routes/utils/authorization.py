from models import Session, User
from core.controllers.utils.Base64 import encoder

async def from_token(token):
    if len(token) % 4:
        token += '=' * (4 - len(token) % 4)
    token = encoder.decode(token)
    session = await Session.objects.get(token=token)
    user = await User.objects.get(id=session.user)
    return user