from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.0',
    author='Abhishek Das',
    author_email='das.abhishek15@gmail.com',
    description='A simple demonstration of a package with various types of calculators',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AbhishekD15/mypackage',  # Use the URL to the github repo.
    packages=find_packages(where="src"),  # Include all packages under src
    package_dir={"": "src"},  # Tell distutils packages are under src
    include_package_data=True,  # Include everything in source control
    classifiers=[
        'Development Status :: 3 - Alpha',  # Change as appropriate
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, change as appropriate
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add your dependencies here
        # 'numpy',  # Uncomment or add if your project depends on it
        # No dependencies for now
    ],
    entry_points={
        # Entry points, if needed
        'console_scripts': [
            'mycalculator=mypackage.base_calculator:main',  # Adjust as appropriate
        ],
    },
)
