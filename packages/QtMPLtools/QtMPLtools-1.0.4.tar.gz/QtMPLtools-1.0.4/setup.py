from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

s = setup(
    name='QtMPLtools',
    version='1.0.4',
    description='Matplotlib plugins for Qt designer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/dresis/QtMPLtools',
    author='Andy Velasco',
    author_email='',
    license='MIT',
    install_requires=['matplotlib', 'PyQt6', 'pyqt6-tools', 'qtpy'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'designer=QtMPLtools.scripts.designer:main',
        ],
    },
    package_data={'QtMPLtools': ['figures/*.ico', 'Test Trial/*']},
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    keywords=['python', 'qt', 'matplotlib', 'plugins', 'plots']
)
