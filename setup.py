#
#
# Setup prog for Harvester
#
#

import sys
sys.path.insert(0,'.')

# get release version
import os
import PandaPkgInfo
release_version = PandaPkgInfo.release_version

from setuptools import setup,find_packages
        
setup(
    name="pandaharvester",
    version=release_version,
    description='Harvester Package',
    long_description='''This package contains Harvester components''',
    license='GPL',
    author='Panda Team',
    author_email='atlas-adc-panda@cern.ch',
    url='https://twiki.cern.ch/twiki/bin/view/Atlas/PanDA',
    packages=find_packages(),
    data_files=[
                # config and cron files
                ('etc/panda', ['templates/panda_harvester.cfg.rpmnew.template',
                                'templates/logrotate.d/panda_harvester.template',
                               ]
                 ),
                # sysconfig
                ('etc/sysconfig', ['templates/sysconfig/panda_harvester.rpmnew.template',
                                   ]
                 ),
                # init script
                ('etc/rc.d/init.d', ['templates/init.d/panda_harvester.exe.template',
                                   ]
                 ),
                ],
)