from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_members1():
    response = client.get("/get_all_members")
    assert response.status_code == 200
    assert response.json() == {}


def test_add_member1():
    response = client.post("/add_member", json={"email": "mail@mail.com", "name": "Mr. Test"})
    response_data = response.json()
    assert response.status_code == 201
    assert response_data['email'] == "mail@mail.com"
    assert response_data['name'] == "Mr. Test"


def test_add_member2():
    response = client.post("/add_member", json={"email": "mail@mail.com", "name": "Mr. Test"})
    response_data = response.json()
    assert response.status_code == 400
    assert response_data["detail"] == "Email already exists"


def test_add_member3():
    response = client.post("/add_member", json={"email": "mail1@mail.com", "name": "Mr. Test2"})
    response_data = response.json()
    assert response.status_code == 400
    assert response_data["detail"] == "Invalid name"


def test_add_member4():
    response = client.post("/add_member", json={"email": "mail@1@mail.com", "name": "Mr. Test"})
    response_data = response.json()
    assert response.status_code == 400
    assert response_data["detail"] == "Invalid email"


def test_add_member5():
    response = client.post("/add_member", json={"email": "mail1@mail.com", "name": "Test Tset"})
    response_data = response.json()
    assert response.status_code == 201
    assert response_data['email'] == "mail1@mail.com"
    assert response_data['name'] == "Test Tset"


def test_get_all_members2():
    response = client.get("/get_all_members")
    assert response.status_code == 200
    assert len(dict(response.json())) == 2


def test_clear1():
    response = client.delete("/clear")
    assert response.status_code == 200
    assert response.json() == {}


def test_get_all_members3():
    response = client.get("/get_all_members")
    assert response.status_code == 200
    assert response.json() == {}


def test_add_member6():
    response = client.post("/add_member", json={"email": "mail@mail.com", "name": "Mr. Test"})
    response_data = response.json()
    assert response.status_code == 201
    assert response_data['email'] == "mail@mail.com"
    assert response_data['name'] == "Mr. Test"


def test_get_all_members4():
    response = client.get("/get_all_members")
    assert response.status_code == 200
    assert len(dict(response.json())) == 1


def test_clear2():
    response = client.delete("/clear")
    assert response.status_code == 200
    assert response.json() == {}
