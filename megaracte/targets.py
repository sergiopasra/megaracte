
from megaracte.profiles import profile_from_dict
from megaracte.sed import sed_from_dict


def target_from_dict(dyct):
    myid = dyct['id']

    profile = profile_from_dict(dyct['profile'])
    sed = sed_from_dict(dyct['sed'])

    return Target(myid, profile, sed)

class Target(object):
    def __init__(self, myid, profile, sed):
        self.id = myid
        self.profile = profile
        self.sed = sed
