import setuptools
# PyPi upload Command
# rm -r dist
# python3 -m build --sdist
# python -m twine upload dist/*

setuptools.setup(
    name="pypiStatTest",
    packages=setuptools.find_packages(),
    version="1.0.0",
    license="MIT",
    description="Test",
    author="Ian Ludanik",
    install_requires=[
        "selenium",
        "Click",
        "python-dotenv",
        "webdriver_manager"
    ],
    entry_points={
    },
    )
