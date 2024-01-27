from setuptools import setup, find_packages

package_name = "lapa_authentication"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(),
    package_data={
        package_name: ["data/*"],
    },
    install_requires=[
        "uvicorn>=0.24.0.post1",
        "fastapi>=0.104.1",
        "square_logger~=1.0",
        "bcrypt>=4.1.2",
        "email_validator>=2.0.0",
        "retrying>=1.3.4",
        "pydantic>=2.5.3",
        "requests>=2.31.0",
        "database_structure>=0.0.3"
    ],
    extras_require={},
    author="Lav Sharma",
    author_email="lavsharma2016@gmail.com",
    description="lapa_authentication service.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/lavvsharma/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
