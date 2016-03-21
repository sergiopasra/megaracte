
from setuptools import find_packages, setup


setup(name='megaracte',
      version='0.1.dev1',
      description='MEGARA CTE',
      url='https://github.com/sergiopasra/megaracte',
      license='GPLv3',
      packages=find_packages(),
      entry_points={'console_scripts': 
                      ['megaracte = megaracte.cli:main']
      },
      classifiers=[
        "Programming Language :: Python",
        'Development Status :: 3 - Alpha',
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Astronomy",
        ],
     long_description=open('README.txt').read()
)
