from setuptools import setup, find_packages

exec(open('api_mqtt/_version.py').read())

setup(
    name='sotirr_mqtt_api',
    version=__version__,
    author='Borisov Anton',
    author_email='sotirr@gmail.com',
    packages=find_packages(),
    install_requires=[
        'paho-mqtt',
    ],
    python_requires='>=3.9',
    package_data={"api_mqtt": ["py.typed"]},
)
