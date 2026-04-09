# in pytest yield is mainly used inside fixtures to provide a value to the test and define teardown
#(cleanup) logic after the test finishes.

'''basic idea:
@pytest.fixture
def my_fixture():
    # Setup code before the test runs
    resource = create_resource()
    yield resource  # Provide the resource to the test
    # Teardown code after the test runs
    cleanup_resource(resource)
'''
import pytest

# basic yield fixture
@pytest.fixture
def numbers():
    print("SETUP")
    nums = [1, 2, 4]
    
    yield nums       # setup and teardown
    # return nums    # only setup
    print("TEARDOWN")
    #nums.clear()

def test_sum(numbers):
    assert sum(numbers) == 7

import os
import subprocess

# file creation and deletion using yield in fixture
@pytest.fixture
def temp_file():
    filename = "test.txt"

    with open(filename, "w") as f:
        f.write("Hello, World!")
    
    result = subprocess.run(
        ["cat", filename],
          #capture_output = True,
          #  text = True
      )
    print(result.stdout)  # just to show the file content during teardown
    yield filename
    
    os.remove(filename)

def test_file_exists(temp_file):
    assert os.path.exists(temp_file)

def test_file_content(temp_file):
    with open(temp_file, "r") as f:
       assert f.read() == "Hello, World!"

# yield without returning a value
@pytest.fixture
def set_env():
    os.environ["MODE"] = "test"

    yield

    del os.environ["MODE"]

def test_env(set_env):
    assert os.environ["MODE"] == "test"

# fixture with scope
@pytest.fixture(scope="module")
def shared_resource():
    print("SETUP ONCE")

    yield {"key": "value"}

    print("TEARDOWN ONCE")

def test_one(shared_resource):
    assert shared_resource["key"] == "value"

def test_two(shared_resource):
    assert "key" in shared_resource

# multiple fixtures with yield
@pytest.fixture
def user():
    print("Creating user")
    user = {"name": "Alice"}
    yield user
    print("Deleting user")
    user.clear()

@pytest.fixture
def account():
    print("Creating account")
    account = {"balance": 100}
    yield account
    print("Deleting account")
    account.clear()

def test_user_account(user, account):
    assert user["name"] == "Alice"
    assert account["balance"] == 100

# class-level fixture with yield
@pytest.fixture(scope="class")
def class_resource():
    print("SETUP CLASS")
    yield
    print("TEARDOWN CLASS")

class TestExample:
    def test_one(self, class_resource):
        assert True

    def test_two(self, class_resource):
        assert True

    
    def ok():
        yield True
    def test_something(ok):
        pass
