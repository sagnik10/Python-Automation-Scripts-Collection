try:
    f = open("test.txt", "w")
    f.write("Hello")
finally:
    f.close()

print(f.closed)