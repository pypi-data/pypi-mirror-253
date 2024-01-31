from setuptools import setup, find_packages

setup(
    name="django-arcgis-address",
    python_requires=">=3.9",
    url="https://gitlab.ics.muni.cz/dobrovolnictvi/django-arcgis-address.git",
    description="Django models for storing and retrieving postal addresses.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools", "django~=4.0"],
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
    ],
)
