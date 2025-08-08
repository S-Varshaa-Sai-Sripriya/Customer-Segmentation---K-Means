from setuptools import find_packages, setup

setup(
    name="customer_segmentation",
    version="0.1",
    author="Varshaa Sai Sripriya Saisheshadhri",
    packages=find_packages(),
    install_requires=[
        "pandas", "numpy", "scikit-learn", "matplotlib", "seaborn"
    ]
)
