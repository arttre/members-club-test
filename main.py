import logging
import re
from datetime import date
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_dict = dict()

regex_for_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_for_name = r'\b([A-Z][a-z. ]+[ ]*)+'

logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG, format='%(asctime)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def email_validation(email: str):
    if re.fullmatch(regex_for_email, email):
        return True
    else:
        return False


def name_validation(name: str):
    if re.fullmatch(regex_for_name, name):
        return True
    else:
        return False


@app.get("/get_all_members")
def get_all_members():
    logging.info(f"/get_all_members. Response: {main_dict}")
    return main_dict


@app.post("/add_member", status_code=201)
def add_member(request_body: dict):

    email = request_body['email']
    name = request_body['name']

    if email in main_dict:
        logging.error({HTTPException(400, f"Email already exists: {email}")})
        raise HTTPException(400, "Email already exists")

    if not email_validation(email):
        logging.error(HTTPException(400, f"Invalid email: {email}"))
        raise HTTPException(400, "Invalid email")

    if not name_validation(name):
        logging.error(HTTPException(400, f"Invalid name: {name}"))
        raise HTTPException(400, "Invalid name")

    date_now = date.today().strftime("%d.%m.%Y")

    main_dict[email] = [name, date_now]

    response = {
        "email": email,
        "name": name,
        "date": str(date_now)
    }

    logging.info(f"/add_member. Request: {request_body}. Response:{response}")

    return response


@app.delete("/clear")
def clear_all_members():
    main_dict.clear()
    logging.info(f"/get_all_members. Response: {main_dict}")
    return main_dict
