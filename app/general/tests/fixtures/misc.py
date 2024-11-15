import pytest
from django.test import override_settings

@pytest.fixture(autouse = True)
def test_settings(settings):
    with override_settings(SECRET_KEY="django-insecure-1vmv^+s%u1fw#a*imqg=*cj3x#%ao@vsy7da%-h8q11$#b+z$x", ):
        yield