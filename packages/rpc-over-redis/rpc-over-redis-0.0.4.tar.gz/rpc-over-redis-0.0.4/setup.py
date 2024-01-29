from setuptools import setup, find_packages

setup(
    name='rpc-over-redis',
    version='0.0.4',
    description='Remote Procedure Call over Redis on Python',
    packages=['rpc_over_redis'],
    include_package_data=True,
    install_requires=[
        'redis==5.0.1',
        'pydantic==2.5.2',
    ],
    license='MIT License',
    platforms=['any'],
    author='Mark Smirnov',
    author_email='mark@mark99.ru'
)
