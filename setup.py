import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-grappelli-themed",
    version="0.0.1",
    author="Yury Lapshinov (Raagin)",
    author_email="y.raagin@gmail.com",
    description="other style for grappelli with css vars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raagin/django-grappelli-themed",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    python_requires='>=3',
    install_requires=[
        'django-grappelli',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)