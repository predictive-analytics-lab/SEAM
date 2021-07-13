from setuptools import find_packages, setup

# We follow Semantic Versioning (https://semver.org/)
_MAJOR_VERSION = "1"
_MINOR_VERSION = "0"
_PATCH_VERSION = "0"

_VERSION_SUFFIX = "alpha"

# Example, '0.4.0-rc1'
version = ".".join([_MAJOR_VERSION, _MINOR_VERSION, _PATCH_VERSION])
if _VERSION_SUFFIX:
    version = f"{version}-{_VERSION_SUFFIX}"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="SEAM",
    version=version,
    author="Yude Wang, Predictive Analytics Lab (PAL)",
    description="Fork of the official SEAM code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_data={},
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=[
        "imageio",
        "mxnet",
        "numpy",
        "opencv-python",
        "pandas",
        "scikit-image",
        "scipy",
        "pydensecrf @ git+https://git@github.com/lucasb-eyer/pydensecrf.git",
        "tensorboard",
        "torch",
        "torchvision",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
        ],
    },
)
