import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student



######################### FIXTURE #########################

# фабрика курсов, создаем  н-количество курсов
@pytest.fixture
def course_factory():
    # *args - дает возможность принять любое количество параметров, **kwargs - именованные аргументы
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def client():
    return APIClient()

##########################################################


# # Task 1 special course check
@pytest.mark.django_db
def test_special_course(client, course_factory):
    #Arrange
    some_course = course_factory(_quantity=1)

    # Act
    response = client.get(f'/api/v1/courses/{some_course[0].id}/')

    # Assert
    assert response.status_code == 200
    assert response.json()['id'] == some_course[0].id




# # Task 2 list check
@pytest.mark.django_db
def test_list_check(client, course_factory):
    #Arrange
    some_course = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(some_course)

    for x, result in enumerate(data):
        assert result['id'] == some_course[x].id



# # Task 3 filter course by ID
@pytest.mark.django_db
def test_chek_id_course(client, course_factory):
    #Arrange
    some_course = course_factory(_quantity=10)

    # Act
    response = client.get(f'/api/v1/courses/?id={some_course[6].id}')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == some_course[6].id




# Task 4 filter course by name
@pytest.mark.django_db
def test_chek_name_course(client, course_factory):
    # Arrange
    some_course = course_factory(_quantity=10)

    # Act
    response = client.get(f'/api/v1/courses/?name={some_course[6].name}')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == some_course[6].name




# Task 5 creating course
@pytest.mark.django_db
def test_create_course(client, course_factory):
    # Arrange
    prepared_course = {'name': 'Django_course'}

    # Act
    response = client.post('/api/v1/courses/', data=prepared_course)

    # Assert
    assert response.status_code == 201  # меняем код т.к. 201 - это сообщение о создании файла по запросу.




# Task 6 PATCH course (change)
@pytest.mark.django_db
def test_patch_course(client, course_factory):
    # Arrange
    some_course = course_factory(_quantity=1)
    data_to_change = {'name': 'Django_course'}

    # Act
    response = client.patch(f'/api/v1/courses/{some_course[0].id}/', data=data_to_change)

    # Assert
    assert response.status_code == 200




# Task 7 DELETE course (change)
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # Arrange
    some_course = course_factory(_quantity=1)

    # Act
    response = client.delete(f'/api/v1/courses/{some_course[0].id}/')

    # Assert
    assert response.status_code == 204   # меняем код, т.к файл удален

