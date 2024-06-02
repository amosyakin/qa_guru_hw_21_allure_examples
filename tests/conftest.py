import allure
import pytest


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    with allure.step('Открыть репозиторий Allure Examples'):
        pass
