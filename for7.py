import logging
logging.basicConfig(
    filename="bank7.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def missing_number(lst:list) -> int:
    logging.info("Finding missing number in the list")
    n = len(lst) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    missing = total_sum - actual_sum
    logging.info(f"Missing number calculated: {missing}")
    return missing
s = [1, 2, 4, 5]
result = missing_number(s)  
print("Missing number:", result)