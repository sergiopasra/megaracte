
from megaracte.profiles import profile_from_dict


def target_from_dict(dyct):
    id = dyct['id']

    profile = profile_from_dict(dyct['profile'])

    return Target(id, profile)

class Target:
    def __init__(self, id, profile):
        self.id = id
        self.profile = profile
