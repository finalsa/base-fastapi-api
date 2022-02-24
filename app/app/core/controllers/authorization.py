from models import Session, User
from models.types import SessionType
from datetime import datetime, timedelta
from secrets import token_urlsafe
from fastapi.responses import JSONResponse


def get_some_minutes_more():
    now = datetime.now()
    result = timedelta(minutes=45) + now
    return result


async def login_validate_bool(token, ip, id=0):
    token = encoder.decode(token)
    session = await Session.objects.get(token=token, ip=ip)
    if(session.id > 0):
        await session.update(
            expiration_date=get_some_minutes_more()
        )
        await session.user.load()
        await session.user.load_data()
        return True, session.user
    return False, None


async def login_validate(token, ip, id):
    token = encoder.decode(token)
    session = await Session.objects.get(token=token, ip=ip,)
    if(session.id > 0):
        await session.update(
            expiration_date=get_some_minutes_more()
        )
        session.token = encoder.encode(session.token)
        return session
    return {'status': 'error'}


async def login(ip, username, password=""):
    users = await User.objects.filter(user_name=username).all()
    if(len(users) == 0):
        return JSONResponse(content={'status': 'Revisa tu usuario.'}, status_code=403)
    u = users[0]
    u = await u.load_data()
    try:
        encoder.ph.verify(u.password, password)
        if(encoder.ph.check_needs_rehash(u.password)):
            await u.update(password=encoder.ph.hash(password))
        token = token_urlsafe(16)
        s = await Session.objects.create(
            ip=ip,
            user=u,
            token=token,
            session_type= await SessionType.objects.get(id = 1),
            creation_date=datetime.now(),
            expiration_date=get_some_minutes_more()
        )
        s.token = encoder.encode(token)
        return s
    except Exception as e:
        print(e)
        return JSONResponse(content={'status':   'Revisa la contraseña'}, status_code=403)


async def logout(ip, token):
    token = encoder.decode(token)
    session = await Session.objects.get(token=token, )
    if(session.id > 0):
        await session.update(
            user=session.user.id,
            expiration_date=datetime.now()
        )
        return {'status': 'ok'}
    return {'status': 'error'}
