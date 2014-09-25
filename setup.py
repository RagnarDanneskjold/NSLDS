from distutils.core import setup

setup(name='NSLDS',
        version='1.2',
        description='Python API to National Student Loan Data System',
        author='Derek Kaknes',
        author_email='derek.kaknes@gmail.com',
        url='TBD',
        py_modules=['nslds'],
        install_requires=['requests', 'lxml'],
        )