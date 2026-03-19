
FILES_PATH = "base_de_dados/"

words = []

with open(FILES_PATH + "teste 2.txt", "r") as f:
    content = f.read()
    
    for line in content.splitlines():
        print(line)
        words += line.strip().split("\n")
    print("=" * 50)
    print(words)
    print("=" * 50)
for i in range(len(words)):
    words[i] = words[i].replace("H", "J")
    print(words[i])