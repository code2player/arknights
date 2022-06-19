from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
SECRET_KEY = 'Data acquisition and integration'


class Token:

    # 生成token，有效时间为60min,3600s
    @staticmethod
    def generate_auth_token(user_id, expiration=36000):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'user_id': user_id}).decode()

    # 解析token
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            # token正确
            data = s.loads(token)
            return data
        except SignatureExpired:
            # token过期
            print("token已经过期")
            return None
        except BadSignature:
            # token错误
            print("token错误")
            return None

