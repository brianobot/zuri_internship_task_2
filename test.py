import requests
from requests import Response


BASE_URL = "https://brianobot.pythonanywhere.com/"


def test_list_persons():
    url = BASE_URL + "api/"
    response: Response = requests.get(url)
    assert response.status_code == 200


def test_create_person():
    url = BASE_URL + "api/"
    data = {"name": "Brian David Obot"}
    response: Response = requests.post(url, data)
    assert response.status_code == 201


def test_person_detail():
    random_id = list(requests.get(BASE_URL + "api/").json()[0].values())[0]
    url = BASE_URL + f"api/{random_id}/"
    response: Response = requests.get(url)
    assert response.status_code == 200


def test_update_person():
    random_id = list(requests.get(BASE_URL + "api/").json()[0].values())[0]
    url = BASE_URL + f"api/{random_id}/"
    response: Response = requests.put(url, data={"name": "Jamie"})
    assert response.status_code == 200
    assert response.json()["name"] == "Jamie"


def test_delete_person():
    random_id = list(requests.get(BASE_URL + "api/").json()[0].values())[0]
    url = BASE_URL + f"api/{random_id}/"
    response: Response = requests.delete(url)
    assert response.status_code == 204


if __name__ == "__main__":
    print(
        """
    ++++++++++++++++++++++++++++++++++
    Starting Tests🔥🔥🔥🔥
    ++++++++++++++++++++++++++++++++++
    """
    )
    test_functions = [
        test_list_persons,
        test_create_person,
        test_person_detail,
        test_update_person,
        test_delete_person,
    ]
    passed = []
    errors = []

    for test in test_functions:
        try:
            test()
        except:
            errors.append(test.__name__)
        else:
            passed.append(test.__name__)

    print(
        """
    ++++++++++++++++++++++++++++++++++
    Test Completed 💧💧💧💧
    ++++++++++++++++++++++++++++++++++
    """
    )
    print(
        f"-------------{len(passed)} Tests Passed, {len(errors)} Tests Failed ----------------"
    )

    print("Passed: ", passed)
    print("Failed: ", errors)
