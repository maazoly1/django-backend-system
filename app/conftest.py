import os

# Set on the earliest possible moment
os.environ['PYTEST_RUNNING'] = 'true'

from .accounts.tests import *
from .general.tests.fixtures import *