import requests

BASE_URL = "https://reqres.in/api"


def test_register_success():
    """Test successful user registration"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(f"{BASE_URL}/register", json=payload)

    assert response.status_code == 200
    assert "token" in response.json()
    print("✅ Registration Success Test Passed")


def test_register_failure():
    """Test registration failure with missing password"""
    payload = {
        "email": "test@test.com"
        # Missing password
    }

    response = requests.post(f"{BASE_URL}/register", json=payload)

    assert response.status_code == 400
    assert "error" in response.json()
    print("✅ Registration Failure Test Passed")


def test_login_success():
    """Test successful login"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(f"{BASE_URL}/login", json=payload)

    assert response.status_code == 200
    assert "token" in response.json()
    print("✅ Login Success Test Passed")


def test_login_failure():
    """Test login failure with missing password"""
    payload = {
        "email": "peter@klaven"
    }

    response = requests.post(f"{BASE_URL}/login", json=payload)

    assert response.status_code == 400
    assert "error" in response.json()
    print("✅ Login Failure Test Passed")