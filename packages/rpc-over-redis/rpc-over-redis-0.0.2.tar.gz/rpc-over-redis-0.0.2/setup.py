from setuptools import setup, find_packages

setup(
    name='rpc-over-redis',
    version='0.0.2',
    description='Remote Procedure Call over Redis on Python',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['rpc_over_redis.py', 'rpc_types.py'],  # включает файлы из корня проекта
    },
    install_requires=[
        'redis==5.0.1',
        'pydantic==2.5.2',
    ],
    license='MIT License',
    platforms=['any'],
    author='Mark Smirnov',
    author_email='mark@mark99.ru'
)
