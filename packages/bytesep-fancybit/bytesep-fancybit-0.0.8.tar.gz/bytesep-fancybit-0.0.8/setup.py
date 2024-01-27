from setuptools import find_packages, setup

setup(
    name='bytesep-fancybit',
    version='0.0.8',
    description='Music source separation fancybit 2024',
    long_description="README.md",
    long_description_content_type="text/markdown",
    author='fancybit',
    author_email="fancybit@qq.com",
    url="https://github.com/fancybit/music_source_separation",
    license='Apache 2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch==2.1.0',
        'librosa==0.8.0',  # specify the version!
        'museval==0.4.0',
        'h5py==2.10.0',
        'pytorch_lightning==1.2.1',
        'numpy==1.20.3',
        'torchlibrosa==0.0.9',
        'matplotlib==3.3.4',
        'musdb==0.4.0',
        'museval==0.4.0',
        'inplace-abn==1.1.0'
    ],
    zip_safe=False
)
