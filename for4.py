import logging

logging.basicConfig(
    filename="bank4.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def is_sorted(lst:list) -> bool:
    logging.info("Checking if list is sorted in ascending order")
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        logging.info(f"Checked elements {lst[i]} and {lst[i + 1]}: in order")
    return True
s=[1, 2, 3, 4, 5]
result = is_sorted(s)
print("Is the list sorted?", result)