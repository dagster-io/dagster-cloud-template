from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="dagster_cloud_template",
        version="1.3.5",
        author="Dagster Cloud",
        description="Template for new Dagster Cloud repos.",
        url="https://github.com/dagster-io/dagster-cloud-template",
        classifiers=[
            "Programming Language :: Python :: 3.8",
        ],
        packages=find_packages(exclude=["dagster_cloud_template_tests"]),
        include_package_data=True,
        install_requires=[
            "dagit",
            "dagster",
            "dagster_cloud",
        ],
        extras_require={
            "test": ["black", "mypy", "pylint", "pytest"],
        },
    )
