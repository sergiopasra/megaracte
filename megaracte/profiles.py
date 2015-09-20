

def profile_from_dict(dyct):
    name = dyct['name']

    if name == 'point':
        return PointProfile()

    elif name == 'extended':
        radius = dyct['radius']
        return ExtendedProfile(radius)

    else:
        raise ValueError('profile name %s nor recognized' % (name,))


class Profile(object):
    """Spatial profiles"""
    pass


class PointProfile(Profile):
    pass


class ExtendedProfile(Profile):
    def __init__(self, radius):
        self.radius = radius
