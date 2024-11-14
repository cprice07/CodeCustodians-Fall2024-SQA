import random
import string
import logging

# Set up logging to report bugs found
logging.basicConfig(filename="fuzz_report.log", level=logging.INFO)

def random_string(length=10):
    """Generate a random string of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def fuzz_split():
    test_string = random_string()
    try:
        result = test_string.split(random.choice([" ", ",", ".", "|", None]))
    except Exception as e:
        logging.info(f"Bug in str.split() with input '{test_string}': {e}")

def fuzz_strip():
    test_string = random_string()
    try:
        result = test_string.strip(random.choice([" ", "\t", "\n", None]))
    except Exception as e:
        logging.info(f"Bug in str.strip() with input '{test_string}': {e}")

def fuzz_int():
    test_string = random.choice([random_string(), random.choice(["123", "-123", "abc", "", None])])
    try:
        result = int(test_string)
    except Exception as e:
        logging.info(f"Bug in int() with input '{test_string}': {e}")

def fuzz_list_sort():
    test_list = [random.choice([random.randint(-1000, 1000), random_string()]) for _ in range(10)]
    try:
        result = sorted(test_list)
    except Exception as e:
        logging.info(f"Bug in list.sort() with input '{test_list}': {e}")

def fuzz_dict_get():
    test_dict = {random_string(): random.randint(0, 100) for _ in range(5)}
    test_key = random.choice([random_string(), None])
    try:
        result = test_dict.get(test_key)
    except Exception as e:
        logging.info(f"Bug in dict.get() with input '{test_dict}' and key '{test_key}': {e}")

if __name__ == "__main__":
    # Number of fuzz tests per method
    num_tests = 1000

    for _ in range(num_tests):
        fuzz_split()
        fuzz_strip()
        fuzz_int()
        fuzz_list_sort()
        fuzz_dict_get()

    print("Fuzz testing completed. Check 'fuzz_report.log' for bug reports.")
