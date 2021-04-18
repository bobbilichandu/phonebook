import re

def validate_email(email: str):
    """ Validates User email-id using regular expression

    Args:
        email (str): [email id of the user]

    Returns:
        [bool]: [returns if the user mailid is valid or not]
    """

    Pattern = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return re.search(Pattern, email) # courtesy of GFG https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/


def validate_phonenumber(phonenumber: str):
    """[Validates User Phone number using regular expression]

    Args:
        phonenumber (str): [phone number of the user]

    Returns:
        [type]: [returns if the user phonenumber is valid or not]
    """

    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(phonenumber) # courtesy of GFG https://www.geeksforgeeks.org/java-program-check-valid-mobile-number/