from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer('56780-)(',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
