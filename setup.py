from distutils.core import setup

setup(
    name='ResearchR',
    version='0.1.0',
    author='Michal Cab',
    author_email='xcabmi00@stud.fit.vutbr.cz',
    packages=['researchr', 'researchr.test'],
    scripts=['bin/researchr.py'],
    url='https://merlin.fit.vutbr.cz/nlp-wiki/index.php/Rrs_researchr',
    license='LICENSE.txt',
    description='Python API module for ResearchR.org',
    long_description=open('README.txt').read(),
)