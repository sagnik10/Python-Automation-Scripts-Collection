def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

with open("big.txt", "w") as f:
    for i in range(3):
        f.write(f"{i}\n")

for line in read_lines("big.txt"):
    print(line)