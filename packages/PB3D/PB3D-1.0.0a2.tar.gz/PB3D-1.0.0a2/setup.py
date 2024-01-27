import setuptools

setuptools.setup(
    name="PB3D",
    version="1.0.0a2",
    author="InvincibleSiwoo",
    author_email="siukk@gmail.com",
    description="A small engine",
    long_description="""
# PB3D
More convenient entity creation! Try 1.0.0a2 right now!
                        """,
    long_description_content_type="text/markdown",
    url="https://github.com/InvincibleSiwoo/engine/tree/master",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)