import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_all_posts():
    """Test fetching all posts"""
    response = requests.get(f"{BASE_URL}/posts")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert isinstance(data, list)
    print("✅ Get All Posts Test Passed")


def test_get_single_post():
    """Test fetching single post"""
    response = requests.get(f"{BASE_URL}/posts/1")
    
    data = response.json()
    
    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    print("✅ Get Single Post Test Passed")


def test_create_post():
    """Test creating a new post"""
    payload = {
        "title": "Test Post",
        "body": "This is a test post for API validation",
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    data = response.json()
    
    assert response.status_code == 201
    assert data["title"] == "Test Post"
    assert data["body"] == "This is a test post for API validation"
    assert data["userId"] == 1
    print("✅ Create Post Test Passed")


def test_update_post():
    """Test updating a post"""
    payload = {
        "id": 1,
        "title": "Updated Post",
        "body": "This post has been updated",
        "userId": 1
    }
    
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    
    data = response.json()
    
    assert response.status_code == 200
    assert data["title"] == "Updated Post"
    print("✅ Update Post Test Passed")