import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tinytmktoolbox',
    version='0.0.41',
    author='Tarik Metin Kaya',
    author_email='tarikmetink@gmail.com',
    description='Some simple functions for general using',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/TarikMetinKaya/TMK_Library',
    project_urls = {
        "Bug Tracker": "https://github.com/TarikMetinKaya/TMK_Library/issues"
    },
    license='MIT',
    packages=["tinytmktoolbox"],
    install_requires=['setuptools','pandas','requests','numpy'],
)