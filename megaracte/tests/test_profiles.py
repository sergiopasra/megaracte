
import pytest

from ..profiles import profile_from_dict

def test_profiles_from_dict():

    with pytest.raises(KeyError):
        profile_from_dict({})