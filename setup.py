from setuptools import setup
try:
    from setuptools_rust import Binding, RustExtension
except ImportError:
    import sys
    import subprocess
    subprocess.call([sys.executable, '-m', 'pip', 'install',
                     'setuptools-rust'])
    from setuptools_rust import Binding, RustExtension


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="retworkx",
    version="0.3.2",
    description="A python graph library implemented in Rust",
    long_description=readme(),
    long_description_content_type='text/markdown',
    author="Matthew Treinish",
    author_email="mtreinish@kortar.org",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Rust",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    url="https://github.com/Qiskit/retworkx",
    project_urls={
        "Bug Tracker": "https://github.com/Qiskit/retworkx/issues",
        "Source Code": "https://github.com/Qiskit/retworkx",
        "Documentation": "https://retworkx.readthedocs.io",
    },
    rust_extensions=[RustExtension("retworkx.retworkx", "Cargo.toml",
                                   binding=Binding.PyO3)],
    include_package_data=True,
    packages=["retworkx"],
    zip_safe=False,
    python_requires=">=3.5",
)
