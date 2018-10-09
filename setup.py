from setuptools import setup, find_packages

setup(
    name='cert-pruner',
    description='Prune IAM Server Certificates that are not attached to an ELB',
    keywords='certificate cert prune delete iam aws',
    url='https://github.com/GESkunkworks/cert-pruner',
    use_scm_version=True,
    author='Michael Palmer',
    author_email='github@michaeldpalmer.com',
    packages=find_packages(),
    setup_requires=['setuptools_scm~=2.0.0'],
    install_requires=[
        'boto3~=1.7.16',
        'pytz~=2018.4'
    ],
    entry_points={
        'console_scripts': [
            'cert-pruner = cert_pruner.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta',
        'Topic :: Utilities'
    ]
)
