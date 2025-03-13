
def user_schema(user)-> dict:
    response = {"user": user}
    return response

def users_schema(users)-> list[dict]:
    response = [user_schema(user) for users in users]
    return response