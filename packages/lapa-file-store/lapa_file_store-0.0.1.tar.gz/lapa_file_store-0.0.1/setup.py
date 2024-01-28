from setuptools import setup, find_packages

package_name = "lapa_file_store"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(),
    package_data={
        package_name: ["data/*", "pydantic_models/*"],
    },
    install_requires=[
        "sqlalchemy>=2.0.23",
        "psycopg2-binary>=2.9.9",
        "uvicorn>=0.24.0.post1",
        "fastapi>=0.104.1",
        "python-multipart>=0.0.6",
        "square_logger~=1.0"
    ],
    author="Aaditya sangishetty",
    author_email="adityashetty35@gmail.com",
    description="oss layer ",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/adityashetty35/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
