import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="YoloRec",
    version="0.1",
    author="egor.bakharev",
    author_email="progr18@pancir.it",
    description="This is a Yolo wrapper",
    long_description=read_me_description,
    install_requires=[
        "ultralytics"
    ],
    long_description_content_type="text/markdown",
    url="https://git.pancir.it/egor.bakharev/SharedLib-YoloRec",
    packages=['YoloRec'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
