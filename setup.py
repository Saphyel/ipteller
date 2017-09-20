from distutils.core import setup
import ipteller

setup(
    name=ipteller.__name__,
    version=ipteller.__version__,
    description='Sends an email when your IP address changes',
    author=ipteller.__author__,
    author_email=ipteller.__email__,
    url=ipteller.__url__,
    license='MIT',
    platforms='unix',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Operating System :: Unix",
        "Topic :: Internet",
        "Topic :: Utilities",
    ],
    packages=['ipteller'],
    tests_require=["behave"],
    install_requires=open('requirements.txt').read(),
    zip_safe=False
)