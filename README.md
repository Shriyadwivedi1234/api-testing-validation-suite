# api-testing-validation-suite
# 🚀 API Testing & Validation Suite

## 📌 Overview
Comprehensive automated API testing project demonstrating backend testing, validation, and quality assurance skills using Python and Postman.

## 🎯 Objective
Test real-world REST APIs to validate:
- Authentication flows (registration, login)
- CRUD operations (Create, Read, Update, Delete)
- Error handling and edge cases
- Response validation (status codes, data structure, tokens)

## 🌐 APIs Tested
**Base URL:** https://jsonplaceholder.typicode.com

### Endpoints Covered:
- `GET /posts` - Fetch all posts
- `GET /posts/{id}` - Fetch single post
- `POST /posts` - Create new post
- `PUT /posts/{id}` - Update post
- `DELETE /posts/{id}` - Delete post
- `GET /users` - Fetch all users
- `GET /users/{id}` - Fetch single user
- `GET /comments` - Fetch comments
- `GET /todos` - Fetch todos

## 🛠️ Tech Stack
- **Python 3.x** - Programming language
- **Requests** - HTTP library for API calls
- **PyTest** - Testing framework
- **Postman** - API testing and documentation
- **JSON** - Data format

## 📁 Project Structure
```
api-testing-validation-suite/
│
├── tests/
│   ├── test_auth.py          # Authentication tests
│   ├── test_users.py          # User management tests
│
├── postman/
│   └── collection.json        # Postman collection
│
├── report.py                  # Custom test reporter
└── README.md                  # Project documentation
```

## ✅ Features Implemented

### 1. Authentication Testing
- ✔ Successful registration validation
- ✔ Registration failure handling (missing fields)
- ✔ Successful login validation
- ✔ Login failure handling

### 2. User Management Testing
- ✔ Fetch user list with pagination
- ✔ Fetch single user details
- ✔ Handle user not found (404)
- ✔ Create new user
- ✔ Update existing user
- ✔ Delete user

### 3. Validation Points
- ✔ HTTP status code validation (200, 201, 400, 404)
- ✔ Response body structure validation
- ✔ Token existence validation
- ✔ Data integrity checks
- ✔ Error message validation

### 4. Reporting
- ✔ Automated test execution
- ✔ Pass/Fail summary
- ✔ Detailed test output
- ✔ Timestamp tracking

## 🚀 How to Run

### Prerequisites
```bash
pip install requests pytest
```

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_auth.py -v
pytest tests/test_users.py -v
```

### Run with Custom Report
```bash
python report.py
```

### Expected Output
```
============================================================
🚀 API TESTING & VALIDATION SUITE
============================================================
📅 Test Run Date: 2026-02-07 14:30:00
🌐 Base URL: https://reqres.in/api
============================================================

tests/test_auth.py::test_register_success PASSED
tests/test_auth.py::test_register_failure PASSED
tests/test_auth.py::test_login_success PASSED
tests/test_auth.py::test_login_failure PASSED
tests/test_users.py::test_get_users PASSED
tests/test_users.py::test_get_single_user PASSED
tests/test_users.py::test_get_user_not_found PASSED
tests/test_users.py::test_create_user PASSED
tests/test_users.py::test_update_user PASSED
tests/test_users.py::test_delete_user PASSED

============================================================
✅ ALL TESTS PASSED!
============================================================
```

## 📊 Test Coverage

| Category | Tests | Status |
|----------|-------|--------|
| Authentication | 4 | ✅ |
| User Management | 6 | ✅ |
| Error Handling | 3 | ✅ |
| **Total** | **10** | **✅** |

## 🧪 Postman Collection

Import `postman/collection.json` into Postman to:
- Manually test all endpoints
- View request/response examples
- Share API documentation
- Run collection tests

### Import Steps:
1. Open Postman
2. Click **Import**
3. Select `postman/collection.json`
4. Run collection or individual requests

## 📚 Skills Demonstrated
- REST API testing
- HTTP methods (GET, POST, PUT, DELETE)
- JSON parsing and validation
- Status code verification
- Authentication testing
- Error handling
- Test automation
- Documentation

## 🎓 Learning Outcomes
- Understanding of REST API architecture
- Hands-on experience with PyTest framework
- API validation best practices
- Automation scripting
- Quality assurance mindset

## 🔧 Future Enhancements
- [ ] Add response time validation
- [ ] Implement data-driven testing
- [ ] Add HTML test reports
- [ ] CI/CD integration
- [ ] Performance testing
- [ ] Security testing

## 👤 Author
**Shriya Dwivedi**  
Customer Engineer Aspirant | QA Automation | API Testing

## 📄 License
This project is for educational and portfolio purposes.

---

**⭐ Star this repository if you found it helpful!**
