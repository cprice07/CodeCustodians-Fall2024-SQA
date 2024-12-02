import random
import string
import logging
import traceback
from datetime import datetime

# Set up logging to report bugs with detailed forensics
logging.basicConfig(filename="fuzz_forensics.log", level=logging.INFO)

def random_string(length=10):
    """Generate a random string of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def log_forensics(test_id, method_name, inputs, exception=None, output=None):
    """Log detailed forensic information."""
    timestamp = datetime.now().isoformat()
    logging.info(f"Timestamp: {timestamp}")
    logging.info(f"Test ID: {test_id}")
    logging.info(f"Method: {method_name}")
    logging.info(f"Inputs: {inputs}")
    if exception:
        logging.info(f"Exception: {exception}")
        logging.info(f"Traceback: {traceback.format_exc()}")
    if output is not None:
        logging.info(f"Output: {output}")
    logging.info("=" * 80) 
    
def fuzz_split(test_id):
    test_string = random_string()
    separator = random.choice([" ", ",", ".", "|", None])
    try:
        result = test_string.split(separator)
        log_forensics(test_id, "split", {"test_string": test_string, "separator": separator}, output=result)
    except Exception as e:
        log_forensics(test_id, "split", {"test_string": test_string, "separator": separator}, exception=e)

def fuzz_strip(test_id):
    test_string = random_string()
    chars = random.choice([" ", "\t", "\n", None])
    try:
        result = test_string.strip(chars)
        log_forensics(test_id, "strip", {"test_string": test_string, "chars": chars}, output=result)
    except Exception as e:
        log_forensics(test_id, "strip", {"test_string": test_string, "chars": chars}, exception=e)

def fuzz_int(test_id):
    test_string = random.choice([random_string(), random.choice(["123", "-123", "abc", "", None])])
    try:
        result = int(test_string)
        log_forensics(test_id, "int", {"test_string": test_string}, output=result)
    except Exception as e:
        log_forensics(test_id, "int", {"test_string": test_string}, exception=e)

def fuzz_list_sort(test_id):
    test_list = [random.choice([random.randint(-1000, 1000), random_string()]) for _ in range(10)]
    try:
        result = sorted(test_list)
        log_forensics(test_id, "list_sort", {"test_list": test_list}, output=result)
    except Exception as e:
        log_forensics(test_id, "list_sort", {"test_list": test_list}, exception=e)

def fuzz_dict_get(test_id):
    test_dict = {random_string(): random.randint(0, 100) for _ in range(5)}
    test_key = random.choice([random_string(), None])
    try:
        result = test_dict.get(test_key)
        log_forensics(test_id, "dict_get", {"test_dict": test_dict, "test_key": test_key}, output=result)
    except Exception as e:
        log_forensics(test_id, "dict_get", {"test_dict": test_dict, "test_key": test_key}, exception=e)

if __name__ == "__main__":
    # Number of fuzz tests per method
    num_tests = 1000

    for test_id in range(num_tests):
        fuzz_split(f"split_{test_id}")
        fuzz_strip(f"strip_{test_id}")
        fuzz_int(f"int_{test_id}")
        fuzz_list_sort(f"list_sort_{test_id}")
        fuzz_dict_get(f"dict_get_{test_id}")

    print("Fuzz testing with forensics completed. Check 'fuzz_forensics.log' for detailed reports.")
