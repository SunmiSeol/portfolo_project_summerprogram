from django.test import TestCase
from django.urls import reverse
import pytest
from program.models import Program

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db
def test_create_program():
    program = Program.objects.create(
        title='Pytest',
        program_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert program.title == "Pytest"
