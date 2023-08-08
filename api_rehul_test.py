# Retrieve the book details with ISBN BNO121712
import requests

response = requests.get("http://216.10.245.166/Library/GetBook.php",
                        params={"AuthorName": "Rahul Shetty"},)

response_json = response.json()

for book in response_json:
    if book["isbn"] == "BNO121712":
        actual_book = book

expected_book = {"book_name": "Learning Rest API with QA academy",
        "isbn": "BNO121712",
        "aisle": "227"}

assert expected_book == actual_book