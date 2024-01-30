from setuptools import setup, find_packages

setup(
    name="base-service",
    version="0.1.0",
    description="Base service for common functionalities",
    packages=find_packages(),
    install_requires=[
        # Buraya requirements.txt'deki bağımlılıklarınızı ekleyin
        "fastapi",
        "sqlalchemy",
        "psycopg2-binary"
    ]
)
