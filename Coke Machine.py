due = 50
inserted = 0

while inserted < 50:
    print(f"Amount Due: {due - inserted}")
    insert = int(input("Insert coin: "))
    if insert == 5 or insert == 10 or insert == 25:
        inserted += insert
    else:
        continue

print(f"Change Owed: {abs(due - inserted)}")
