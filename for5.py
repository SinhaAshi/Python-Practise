import logging

logging.basicConfig(
    filename="bank5.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def reverse_string(s:str)-> str:
    logging.info(f"Reversing string: {s}")
    rev = ""
    for ch in s:
        rev = ch + rev
    logging.info(f"Reversed string: {rev}") 
    return rev

s="hello"
result = reverse_string(s)
print(reverse_string("hello"))