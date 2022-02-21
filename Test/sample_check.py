import requests


def test_get_status_code_equals_200():
    response = requests.get("https://api.hatchways.io/assessment/blog/posts?tag=tech")
    assert response.status_code == 200


# negative test for above test
# def test_negative_get_status_code_not_equals_200():
#     response = requests.get("https://api.hatchways.io/assessment/blog/posts?tag=tech")
#     assert response.status_code  == 201

def test_get_check_content_type_equals_json():
    response = requests.get("https://api.hatchways.io/assessment/blog/posts?tag=tech")
    assert response.headers["Content-Type"] == "application/json"

