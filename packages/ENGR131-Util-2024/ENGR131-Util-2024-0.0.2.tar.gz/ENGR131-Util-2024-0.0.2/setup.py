import setuptools

setuptools.setup(
    name="ENGR131-Util-2024",
    version="0.0.2",
    author="Joshua C. Agar",
    description="Drexel Jupyter Logger Package",
    packages=setuptools.find_packages(),
    install_requires=["cryptography", "drexel_jupyter_logger", "ipywidgets"],
)
