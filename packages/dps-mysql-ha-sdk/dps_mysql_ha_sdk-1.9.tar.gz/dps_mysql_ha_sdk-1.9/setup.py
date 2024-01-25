import setuptools
from setuptools import setup

setup(
    name='dps_mysql_ha_sdk',
    version='1.9',
    packages=setuptools.find_packages(),
    package_data={'': ['dynamic_pooled_db.py','test_demo.py']},
    install_requires=[
    ],
    # Other project metadata
    author='daijiacong',
    description='高可用数据库连接',
    license='MIT',
)
