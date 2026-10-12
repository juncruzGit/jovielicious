from unittest.mock import MagicMock

import pytest

from fastapi.testclient import TestClient
from src import app
from src import DishesService, DishService, DishSizesService

from src.dependencies import get_dishes_service, get_dish_service, get_dish_sizes_service
from src.data.repository.dish_repository import DishRepository

@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(autouse=True)
def clear_overrides():
    """Fixture to ensure dependency overrides are cleared after every test."""
    yield
    app.dependency_overrides.clear()


@pytest.fixture
def mocked_dishes_service(mocker):
    """Fixture to create, inject, and automatically clean up the mock service."""
    # 1. Create a mock object that mimics the UserService class structure
    mock_service = MagicMock(spec=DishesService)
    
    # 2. Inject the mock into FastAPI's dependency overrides (wrapped in a lambda)
    app.dependency_overrides[get_dishes_service] = lambda: mock_service
    
    # 3. Hand the mock over to the test function
    yield mock_service
    
    # 4. Teardown: Automatically clear the override when the test ends
    app.dependency_overrides.clear()

@pytest.fixture
def mocked_dish_service(mocker):
    """Fixture to create, inject, and automatically clean up the mock service."""
    # 1. Create a mock object that mimics the UserService class structure
    mock_service = MagicMock(spec=DishService)
    
    # 2. Inject the mock into FastAPI's dependency overrides (wrapped in a lambda)
    app.dependency_overrides[get_dish_service] = lambda: mock_service
    
    # 3. Hand the mock over to the test function
    yield mock_service
    
    # 4. Teardown: Automatically clear the override when the test ends
    app.dependency_overrides.clear()


@pytest.fixture
def mocked_dish_sizes_service(mocker):
    """Fixture to create, inject, and automatically clean up the mock service."""
    # 1. Create a mock object that mimics the UserService class structure
    mock_service = MagicMock(spec=DishSizesService)
    
    # 2. Inject the mock into FastAPI's dependency overrides (wrapped in a lambda)
    app.dependency_overrides[get_dish_sizes_service] = lambda: mock_service
    
    # 3. Hand the mock over to the test function
    yield mock_service
    
    # 4. Teardown: Automatically clear the override when the test ends
    app.dependency_overrides.clear()


@pytest.fixture
def mocked_dish_size_service(mocker):
    """Fixture to create, inject, and automatically clean up the mock service."""
    # 1. Create a mock object that mimics the UserService class structure
    mock_service = MagicMock(spec=DishSizeService)
    
    # 2. Inject the mock into FastAPI's dependency overrides (wrapped in a lambda)
    app.dependency_overrides[get_dish_sizes_service] = lambda: mock_service
    
    # 3. Hand the mock over to the test function
    yield mock_service
    
    # 4. Teardown: Automatically clear the override when the test ends
    app.dependency_overrides.clear()

