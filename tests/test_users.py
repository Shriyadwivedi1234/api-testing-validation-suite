import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_all_users():
    """Test fetching all users"""
    response = requests.get(f"{BASE_URL}/users")
    
    data = response.json()
    
    assert response.status_code == 200
    assert len(data) == 10
    assert isinstance(data, list)
    print("✅ Get All Users Test Passed")


def test_get_single_user():
    """Test fetching single user"""
    response = requests.get(f"{BASE_URL}/users/1")
    
    data = response.json()
    
    assert response.status_code == 200
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data
    print("✅ Get Single User Test Passed")


def test_get_user_posts():
    """Test fetching posts by user"""
    response = requests.get(f"{BASE_URL}/posts?userId=1")
    
    data = response.json()
    
    assert response.status_code == 200
    assert len(data) > 0
    assert all(post["userId"] == 1 for post in data)
    print("✅ Get User Posts Test Passed")


def test_get_comments():
    """Test fetching comments"""
    response = requests.get(f"{BASE_URL}/comments?postId=1")
    
    data = response.json()
    
    assert response.status_code == 200
    assert len(data) > 0
    assert "email" in data[0]
    assert "body" in data[0]
    print("✅ Get Comments Test Passed")


def test_delete_post():
    """Test deleting a post"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    print("✅ Delete Post Test Passed")


def test_get_todos():
    """Test fetching todos"""
    response = requests.get(f"{BASE_URL}/todos?userId=1")
    
    data = response.json()
    
    assert response.status_code == 200
    assert len(data) > 0
    assert "completed" in data[0]
    print("✅ Get Todos Test Passed")