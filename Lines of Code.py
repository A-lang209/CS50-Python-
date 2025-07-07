from sys import argv, exit; exit("Invalid argument") if len(argv) != 2 or not argv[1].endswith(".py") else None
try:
    print(sum(1 for line in open(argv[1]) if line.strip() and not line.lstrip().startswith("#")))
except FileNotFoundError:
    exit("File does not exist")


from sys import argv, exit; exit("Invalid argument") if len(argv) != 2 or not argv[1].endswith(".py") else print(sum(1 for line in open(argv[1]) if line.strip() and not line.lstrip().startswith("#"))) if open(argv[1]) else exit("File does not exist")

