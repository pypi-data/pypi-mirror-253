import random
import string

# TODO Move this method to python-sdk-local-package /src/identifier
def generate_random_string(length: int) -> str:

    # TODO while loop
    letters = string.ascii_letters + string.digits
    # TODO result -> identifier
    result = ''.join(random.choice(letters) for i in range(length))

    # TODO Change in identifier.identifier_table it doesn't exist using INSERT, if exits generate another identifier

    return result
