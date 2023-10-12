import requests

def fetch_data():
    url = "https://getcharacter-tn66svqhpq-uc.a.run.app/"
    typeimportid = input("Enter id: ")
    params = {"id": typeimportid}

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            handle_complete(response.text)
        else:
            handle_io_error(response.status_code)

    except requests.exceptions.RequestException as e:
        handle_io_error(str(e))

def handle_complete(response_data):
    # Your code to handle a successful response goes here
    print("Request successful. Response data:", response_data)

def handle_io_error(error_message):
    # Your code to handle an IO error goes here
    print("IO Error:", error_message)

fetch_data()
