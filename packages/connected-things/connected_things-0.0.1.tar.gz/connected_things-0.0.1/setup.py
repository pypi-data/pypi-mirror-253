from setuptools import setup

setup(
    name='connected_things',
    version='0.0.1',    
    description='connected things file uploader',
    url='https://github.com/con-things/pip_package',
    author='Andrew Tocchi',
    author_email='andrew@connected-things.com',
    license='apache 2,0 license',
    packages=['connected_things'],
    install_requires=[
                      'boto3',
                      'requests',                     
                      ],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',  
        'Programming Language :: Python :: 3.8',
    ],
)