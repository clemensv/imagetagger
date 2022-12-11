from setuptools import setup, find_packages
from setuptools_scm import get_version

setup(
    name="imagetagger",
    description="A script to generate titles and descriptions for images on Flickr using Azure Vision and OpenAI GPT-3",
    #url="https://github.com/clemensv/imagetagger",
    author="Clemens Vasters",
    author_email="clemens@vasters.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "argparse",
        "flickrapi",
        "azure-cognitiveservices-vision-computervision",
        "msrest",
        "wikipedia",
        "openai"
    ],
    use_scm_version={
        "version_scheme": "post-release",
        "local_scheme": "dirty-tag"
    },
    setup_requires=["setuptools_scm"],
    entry_points={
        "console_scripts": [
            "imagetagger=imagetagger.imagetagger:main"
        ]
    },
    zip_safe=False
)
