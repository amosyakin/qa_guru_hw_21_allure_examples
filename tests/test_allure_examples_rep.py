import allure
import pytest


@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1255')
class TestAllureExamples:
    @allure.id("32688")
    @allure.feature('Code')
    @allure.title('Копирование репозитория с помощью SSH')
    def test_copy_ssh(self):
        with allure.step('Нажать кнопку Code'):
            pass

        with allure.step('Выбрать вкладку SSH'):
            pass

        with allure.step('Нажать кнопку "Copy url to clipboard"'):
            pass

            with allure.step('Кнопка сменила название на "Copied!"'):
                pass

    @allure.id("32689")
    @allure.feature('Issue')
    @allure.title('Создание новой Issue')
    def test_new_issue(self):
        with allure.step('Нажать вкладку Issue'):
            pass

        with allure.step('Нажать кнопку "New issue"'):
            pass

        with allure.step('Ввести Titile'):
            pass

        with allure.step('Нажать кнопку "Submit new issue"'):
            pass

    @allure.id("32690")
    @allure.feature('Branch')
    @allure.title('Создание новой ветки')
    def test_new_branch(self):
        with allure.step('Нажать кнопку Branches'):
            pass

        with allure.step('Нажать кнопку "New branch"'):
            pass

        with allure.step('Ввести название новой ветки'):
            pass

        with allure.step('Нажать кнопку "Create new branch"'):
            pass

    @allure.id("32691")
    @allure.feature('Branch')
    @allure.title('Смена ветки')
    @pytest.mark.parametrize("branch", ['main', "test_1"])
    def test_change_branch(self, branch):
        with allure.step('Нажать кнопку для выбора веток'):
            pass

        with allure.step(f'В выпадающем списке выбрать ветку "{branch}"'):
            pass

    @allure.feature('Pull requests')
    @allure.title('Создание pull requests')
    def test_new_pull_requests(self):
        with allure.step('Нажать вкладку Pull requests'):
            pass

        with allure.step('Выбрать compare-ветку'):
            pass

        with allure.step('Ввести название новой ветки'):
            pass

        with allure.step('Нажать кнопку "Create new branch"'):
            pass

    @allure.id("32692")
    @allure.feature('File')
    @allure.title('Добавление нового файла')
    def test_new_file(self):
        with allure.step('Нажать кнопку "Add file"'):
            pass

        with allure.step('Нажать кнопку "Create new file"'):
            pass

        with allure.step('Ввести имя файла'):
            pass

        with allure.step('Ввести текст в файл'):
            pass

        with allure.step('Нажать кнопку "Commit changes"'):
            pass

        with allure.step('Ввести commit message'):
            pass

        with allure.step('Нажать кнопку "Commit changes"'):
            pass

        with allure.step('Проверка, что новый файл отображается в репозитории'):
            pass
