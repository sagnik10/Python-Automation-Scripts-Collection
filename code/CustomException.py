class CustomError(Exception):
    pass

def check(n):
    if n < 0:
        raise CustomError("Negative value")

try:
    check(-1)
except CustomError as e:
    print(e)