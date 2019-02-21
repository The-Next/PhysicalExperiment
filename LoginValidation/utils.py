def jwt_response_payload_handler(token, user=None, request=None):
    '''
    自定义令牌签发
    '''
    return {
        'token': token,
        'user_s': user.s_num,
        'username': user.username,
        'user_id' :user.id
    }