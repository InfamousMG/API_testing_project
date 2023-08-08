import requests
from payload import payload
from utilities.configuration import *
from utilities.resources import ApiResources

# creating a variable and assigning get_config method to it which reads from properties.ini
# and takes the base URL from there
config = get_config()

# creating an instance of ApiResources class
api_resource = ApiResources()

# setting up urls for particular endpoints
url_add = config["API"]["endpoint"]+api_resource.add_book
url_get = config["API"]["endpoint"]+api_resource.get_book
url_delete = config["API"]["endpoint"]+api_resource.delete_book


def test_e2e():
    # adding a book to the database
    response_add_book = requests.post(url_add,
                                      json=payload("a book",
                                                   "AD",
                                                   "10",
                                                   "Michael Block"))

    # testing if it's a valid response from the call to API
    assert response_add_book.status_code == 200

    # parsing the json from the response
    response_add_book_json = response_add_book.json()
    print(response_add_book_json)

    # getting hold of the id of the added book which is then needed to delete the book from database
    book_id = response_add_book_json["ID"]
    print(book_id)

    ########################################################################################################
    # checking if the book is in the database
    response_get_book = requests.get(url_get,
                                     params={"AuthorName": "Michael Block"})

    # testing if it's a valid response from the call to API
    assert response_add_book.status_code == 200

    # parsing the json from the response
    response_get_book_json = response_get_book.json()
    print(response_get_book_json)

    ########################################################################################################
    # deleting the book
    response_delete_book = requests.post(url_delete, json={"ID": book_id},
                                         headers={"Content-Type": "application/json"})

    # parsing the json from the response
    response_delete_book_json = response_delete_book.json()
    print(response_delete_book_json)

    # testing if it's a valid response from the call to API
    assert response_delete_book.status_code == 200
