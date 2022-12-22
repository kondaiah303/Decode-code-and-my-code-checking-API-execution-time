import requests
import json
import timeit
import os


headers1 = {"workspace_id": os.environ.get('Workspace_Id'),
"authorization": os.environ.get('Authorization'),
"id_token" : os.environ.get('Id_Token')
            }

body1 = {
    "text": ""
}

endpoint = "http://localhost:3000/dev/v1/word_frequency_handler"

test_response_list = []
file = open('/Users/entropik/Documents/codetesting/tester_response_data.txt', 'r')
for line in file.readlines():
    test_response_list.append(line.strip())

num = int(input('enter the number: '))

def json_data():
    message1 = json.dumps(body1)
    return message1


def tester_response(num):
    for tester_count in range(num):
        body1.update({'text': test_response_list[tester_count]})
        response = requests.post(url=endpoint, headers=headers1, data=json_data())
        print(response.json())


def configure_tester_response():
    if num == 1:
        def test_api():
            return tester_response(1)

        print(timeit.timeit(test_api, number=1))
    else:
        tester_response(num)


def main():
    configure_tester_response()


if __name__ == "__main__":
    main()
