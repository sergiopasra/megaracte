import yaml
import numpy
import megaracte.cli

megaracte.cli.main()

targetsfile = 'targets.yml'

with open(targetsfile) as fd:
    allf = yaml.load(fd)


targets = allf['targets']

from megaracte.targets import target_from_dict

import matplotlib.pyplot as plt

for t in targets:
    tt = target_from_dict(t)

    print(tt.sed)

