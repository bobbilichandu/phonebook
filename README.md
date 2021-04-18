# PHONEBOOK
A simple python api developed using fastapi to learn basic syntax and types and specially **pydantic**
Python version - 3.8
FastAPI - 0.63.0
sqlalchemy - 1.4.9
pydantic - 1.8.1

This api allows a user to create an account, and add contacts to his account.

## How to use Phonebook?
1. Clone the repository 
    > cd phonebook
2. Create a virtual environment with python3.8 (https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv)
3. > pip install -r requirements.txt
4. > uvicorn main:phonebook --reload


### Special Functionalities

1. Token Auth:
    What is Token Auth? 
        A very simple authorization using a unique string per user that is provided while creating one's account.
    Unique numeric string will be generated using a hash function, that will be provided via response for the user account creation request.
    That token has to provided whenever the user wants to make any changes to his/her data.

2. Relational database Schema:
    User:
        id: int
        name: string
        mail: string
        phonenumber: string
        premium: bool
        contacts: list of Contacts
    Contact:
        id: int
        name: string
        mail: string
        phonenumber: string
        owner_id: int *user.id*

3. SQLite database is used for this mini project, it is advisable to use postgres or other suitable databases for production purposes.

4. Validation for mail and phone number.

### Basic Functionalities

1. Create user **POST**
    http://ip:port/users/addUser/
    Request Body: 
        {
            "name": "string",
            "email": "string",
            "phonenumber": "string"
        }

2. Get user data **GET**
    http://ip:port/users/{param}/
    *param can be mail or phone number*
    Request Body:
        {
            "param": "string"
        }

3. Add contact details **POST**
    http://ip:port/users/{param}/addContact
    *param can be mail or phone number*
    *token must be provided for authorization*
    Request Body:
    {
        "name": "string",
        "email": "string",
        "phonenumber": "string"
        "token" : "string"
    }

4. Get contacts for a user **GET**
    http://ip:port/users/{param}/contacts
    *param can be mail or phone number*
    *token must be provided for authorization*
    Request Body:
        {
            "param": "string"
            "token" : "string"
        }

### Http exceptions

    Used Http Error Exceptions for error handling
    (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)


