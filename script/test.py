import yaml

import megaracte.cli

megaracte.cli.main()

targetsfile = 'targets.yml'

with open(targetsfile) as fd:
    allf = yaml.load(fd)


targets = allf['targets']

from megaracte.targets import target_from_dict

for t in targets:
    print(target_from_dict(t))
