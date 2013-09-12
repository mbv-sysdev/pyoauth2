from distutils.core import setup
# TODO: optimize client for webob
setup(
    name='pyoauth2',
    version='1.0',
    author='GraphEffect, Inc.',
    author_email='nate@grapheffect.com',
    packages=['pyoauth2', 'pyoauth2.tests'],
    scripts=[],
    url='https://github.com/GraphEffect/pyoauth2',
    license='LICENSE.txt',
    description='OAuth 2.0 compliant client and server library.',
    long_description=open('README.txt').read(),
    install_requires=[
        'WebOb',
        "PyCrypto >= 2.6"
    ]
)
