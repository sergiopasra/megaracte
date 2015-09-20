
import pytest

from ..profiles import profile_from_dict
from ..profiles import PointProfile
from ..profiles import ExtendedProfile

def test_profiles_from_dict():

    with pytest.raises(KeyError):
        profile_from_dict({})


def test_profiles_point():

    prof = profile_from_dict({'name': 'point'})

    assert isinstance(prof, PointProfile)


def test_profiles_extended():

    prof = profile_from_dict({'name': 'extended', 'radius': 2.0})

    assert isinstance(prof, ExtendedProfile)
