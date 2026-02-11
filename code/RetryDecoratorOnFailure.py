def retry(times):
    def decorator(func):
        def inner(*a, **k):
            for _ in range(times):
                try:
                    return func(*a, **k)
                except Exception:
                    pass
            raise RuntimeError("Failed after retries")
        return inner
    return decorator

count = {"x": 0}

@retry(3)
def flaky():
    count["x"] += 1
    if count["x"] < 3:
        raise ValueError
    return "Success"

print(flaky())