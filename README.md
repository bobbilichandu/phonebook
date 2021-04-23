# PHONEBOOK
A simple python api developed using fastapi to learn basic syntax and types and specially **pydantic** \
Python version - *3.8* \
FastAPI - *0.63.0* \
sqlalchemy - *1.4.9* \
pydantic - *1.8.1*  

This api allows a user to create an account, and add contacts to his account.

## How to use Phonebook?
1. Clone the repository 
    > git clone https://github.com/chandu1263/phonebook.git

    > cd phonebook
1. Create a virtual environment with python3.8 \
reference: https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv
1. > pip install -r requirements.txt
1. > uvicorn main:phonebook --reload


## Special Functionalities

1. Token Auth:
    What is Token Auth? \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A very simple authorization using a unique string per user that is provided while creating one's account. \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unique numeric string will be generated using a hash function, that will be provided via response for the user account creation request.
    That token has to provided whenever the user wants to make any changes to his/her data.

2. Relational database Schema: \
    __User:__ \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id: int \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name: string \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mail: string \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phonenumber: string \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;premium: bool \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;contacts: list of Contacts \
    __Contact:__ \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id: int \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name: string \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mail: string \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phonenumber: string \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;owner_id: int *user_id* 

3. SQLite database is used for this mini project, it is advisable to use postgres or other suitable databases for production purposes.

4. Validation for mail and phone number.

## Basic Functionalities

1. Create user - **POST** \
    &nbsp;&nbsp;&nbsp; http://ip:port/users/addUser/ \
    Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{\
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "string",\
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"email": "string",\
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"phonenumber": "string"\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

2. Get user data - **GET** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/ \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"param": "string" \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

3. Add contact details - **POST** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/addContact \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*token must be provided for authorization* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "string", \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"email": "string", \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"phonenumber": "string" \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token" : "string" \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

4. Get contacts of a user - **GET** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/contacts \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*token must be provided for authorization* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"param": "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token" : "string" \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

5. Update user email - **PUT** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/updateUserEmail \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number for identifying the user* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*token must be provided for authorization* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"param": "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token" : "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"update_param" : "string" (to be updated email) \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

6. Update user phone number - **PUT** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/updateUserPhonenumber \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number for identifying the user* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*token must be provided for authorization* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"param": "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token" : "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"update_param" : "string" (to be updated phone number) \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

7. Delete user - **DELETE** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/deleteUser \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number for identifying the user* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*token must be provided for authorization* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"param": "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token" : "string" \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

8. Update user contact email - **PUT** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/updateContactEmail \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number for identifying the user* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*token must be provided for authorization* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"param": "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token" : "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"email" : "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"newmail" : "string" \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

9. Update user contact phone number - **PUT** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/updateContactPhonenumber \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number for identifying the user* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*token must be provided for authorization* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"param": "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token" : "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"phonenumber" : "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"newphonenumber" : "string" \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

10. Delete user contact - **PUT** \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://ip:port/users/{param}/deleteUserContact \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*param can be mail or phone number for identifying the user* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*token must be provided for authorization* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*contact_param can be mail or phone number for identifying contact of the user* \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Request Body: \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"param": "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token" : "string" \
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contact_param" : "string" \
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
## Http exceptions

    Used Http Error Exceptions for error handling
    (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) 

    Basic exceptions were used. 



