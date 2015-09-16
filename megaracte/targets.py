
from megaracte.profiles import profile_from_dict
from megaracte.sed import sed_from_dict


def target_from_dict(dyct):
    id = dyct['id']

    profile = profile_from_dict(dyct['profile'])
    sed = sed_from_dict(dyct['sed'])

    return Target(id, profile, sed)

class Target:
    def __init__(self, id, profile, sed):
        self.id = id
        self.profile = profile
        self.sed = sed
