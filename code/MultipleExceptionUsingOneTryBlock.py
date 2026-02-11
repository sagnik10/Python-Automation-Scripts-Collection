try:
    x = int("a")
    y = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print(type(e).__name__)