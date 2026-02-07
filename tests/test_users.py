import requests

BASE_URL = "https://reqres.in/api"


def test_get_users():
    """Test fetching list of users"""
    response = requests.get(f"{BASE_URL}/users?page=2")

    data = response.json()

    assert response.status_code == 200
    assert len(data["data"]) > 0
    assert "page" in data
    assert data["page"] == 2
    print("✅ Get Users Test Passed")


def test_get_single_user():
    """Test fetching single user"""
    response = requests.get(f"{BASE_URL}/users/2")

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["id"] == 2
    assert "email" in data["data"]
    print("✅ Get Single User Test Passed")


def test_get_user_not_found():
    """Test user not found error"""
    response = requests.get(f"{BASE_URL}/users/999")

    assert response.status_code == 404
    print("✅ User Not Found Test Passed")


def test_create_user():
    """Test creating a new user"""
    payload = {
        "name": "John Doe",
        "job": "QA Engineer"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload)

    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "John Doe"
    assert data["job"] == "QA Engineer"
    assert "id" in data
    assert "createdAt" in data
    print("✅ Create User Test Passed")


def test_update_user():
    """Test updating user"""
    payload = {
        "name": "Jane Doe",
        "job": "Senior QA Engineer"
    }

    response = requests.put(f"{BASE_URL}/users/2", json=payload)

    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Jane Doe"
    assert data["job"] == "Senior QA Engineer"
    print("✅ Update User Test Passed")


def test_delete_user():
    """Test deleting user"""
    response = requests.delete(f"{BASE_URL}/users/2")

    assert response.status_code == 204
    print("✅ Delete User Test Passed")