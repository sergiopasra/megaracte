import numpy

from astropy.analytic_functions import blackbody_lambda


def sed_from_dict(dyct):
    name = dyct['name']
    flux = dyct['flux']
    wl = dyct['wavelength']
    if name == 'flat':
        return Sed(wl, flux)
    elif name == 'blackbody':
        temp = dyct['temperature']
        return BlackBody(wl, flux, temp)
    elif name == 'template':
        template = dyct['template']
        return Template(wl, flux, template)
    else:
        raise ValueError('sed name %s nor recognized' % (name,))


class Sed(object):
    def __init__(self, wl, flux):
        self.flux = flux
        self.wl = wl

    def generate(self, wl):
        return self.flux* numpy.ones_like(wl)


class BlackBody(Sed):
    def __init__(self, wl, flux, temp):
        super(BlackBody, self).__init__(wl, flux)
        self.temp = temp
        self.scale = flux / blackbody_lambda(wl, self.temp)

    def generate(self, wl):
        # WL in AA, temp in K
        return self.scale * blackbody_lambda(wl, self.temp)


class Template(Sed):
    def __init__(self, wl, flux, template):
        super(Template, self).__init__(wl, flux)
        self.template = template
        #self.scale = flux / blackbody_lambda(wl, self.temp)

    #def generate(self, wl):

    #    u, v = numpy.loadtxt(self.template)
    #    # WL in AA, temp in K
    #    return self.scale * blackbody_lambda(wl, self.temp)
