import logging

logging.basicConfig(
    filename="bank2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def freq(s:str) -> dict:
    logging.info("Calculating character frequency")
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
        logging.info(f"Character '{char}' frequency updated: {char_freq[char]}")
    return char_freq
s = "hello world"
result = freq(s)
print("Character frequency:", result)