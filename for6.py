import logging
logging.basicConfig(
    filename="bank6.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def duplicate(s:list) -> list:
    logging.info("Finding duplicate elements in the list")
    seen = set()
    duplicates = set()
    for item in s:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
        logging.info(f"Seen: {seen}, Duplicates: {duplicates}")
    return list(duplicates)
s = [1, 2, 3, 4, 2, 5, 1]
result = duplicate(s)
print("Duplicate elements:", result)

