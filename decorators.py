

def decorator(func):
    def decorated(w, h):
    # def decorator(*args):
    #     w = args[0]
    #     h = args[1]
        if w > 0 or h > 0:
            print('good')
            return func(w, h)
        else:
            raise ValueError('음수다인마')
    return decorated
@decorator
def triangle(w, h):
    val = w * h / 2
    print(val)
@decorator
def box(w, h):
    val = w * h
    return val
# triangle(-22, -22)
print(box(3,3))


class User:
    def __init__(self, auth):
        self.is_authenticated = auth


user = User(auth=False)
r