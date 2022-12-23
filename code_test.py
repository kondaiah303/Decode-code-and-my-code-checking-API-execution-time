import timeit
import requests
import json
import os

body = {
  "block_id": "",
  "study_id": "cfe2e6a8-3028-4e8a-b22f-d38cf89de050",
  "tester_id": "",
  "response": []
        }

test_response_block_id = "b0d4be1c-bf81-448d-b062-f5f1a1df2dde"
thank_you_block_id = "d1fb98b3-5f34-4f17-9f7b-eebe4b3ce422"

headers1 = {"workspace_id": os.environ.get('Workspace_Id'),
"authorization": os.environ.get('Authorization'),
"id_token" : os.environ.get('Id_Token')
            }

tester_id_endpoint = "https://in.dev.apicx.getdecode.io/v1/tester"
submit_response_endpoint = "https://in.dev.apicx.getdecode.io/v1/tester_response"
thank_you_endpoint = "https://in.dev.apicx.getdecode.io/v1/tester_response"


test_response_list = []
file = open('/Users/entropik/Documents/codetesting/tester_response_data.txt', 'r')
for line in file.readlines():
    test_response_list.append([line.strip()])

num = int(input('enter the number: '))


def json_data():
    message = json.dumps(body)
    return message


def tester_response(num):
    for tester_count in range(num):
        body.update({'block_id': test_response_block_id})
        body.update({'response': test_response_list[tester_count]})
        json_data()
        test_id_response = requests.post(url=tester_id_endpoint, headers=headers1, data=json_data())
        tester_json_data = test_id_response.json()
        print(tester_json_data)
        tester_id_generate = tester_json_data['data']['tester']['tester_id']
        body.update({'tester_id': tester_id_generate})
        test_response = requests.post(url=submit_response_endpoint, headers=headers1, data=json_data())
        print(test_response.json())
        body.update({'response': []})
        body.update({'block_id': thank_you_block_id})
        thank_you_response = requests.post(url=thank_you_endpoint, headers=headers1, data=json_data())
        print(thank_you_response.json())


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
