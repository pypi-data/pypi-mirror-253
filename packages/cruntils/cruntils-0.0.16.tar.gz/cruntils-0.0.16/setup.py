import setuptools

setuptools.setup(
    name="cruntils",
    version="0.0.16",
    description="A collection of utilities.",
    author="Nambarc",
    packages=["cruntils"],
    include_package_data=True,
    package_data={"": ["EGM96_WW_15M_GH.GRD"]},
    install_requires=["setuptools>=61.0"]
)