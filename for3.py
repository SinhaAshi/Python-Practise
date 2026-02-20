import logging

logging.basicConfig(
    filename="bank3.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def second_largest(lst:list) -> int:
    logging.info("Finding second largest number in the list")
    first = second = -1
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num != first and num > second:
            second = num
        logging.info(f"Second largest: {second}")
    return second 
s = [3, 1, 4, 1, 5, 9]
result = second_largest(s)
print("Second largest number:", result)