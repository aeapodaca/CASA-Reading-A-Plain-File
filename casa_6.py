filename = './big-mac-full-index.csv'
count = 0
with open(filename, "r", encoding="utf-8") as f:
  for line in f:
    if "USA" in line: 
        print(line.strip())
        count += 1
print("total lines found with 'USA' :", count)
