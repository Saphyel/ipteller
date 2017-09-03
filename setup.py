from distutils.core import setup

setup(
    name='ipteller',
    version='1.0.1',
    description='Sends an email when your IP address changes',
    url='http://github.com/Saphyel/ipteller',
    author='Saphyel',
    author_email='Saphyel@gmail.com',
    license='MIT',
    packages=['ipteller'],
    tests_require=["behave"],
    install_requires=["setuptools"],
    zip_safe=False
)
