from setuptools import setup, find_packages

requirements = [
    'opencv-python',
    'numpy',
    'scikit-image',
    'setuptools'
]

__version__ = 'V0.1.7'

setup(
    name='meta-cv',
    version=__version__,
    author='CachCheng',
    author_email='tkggpdc2007@163.com',
    url='https://github.com/CachCheng/metacv',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    description='Meta CV Toolkit',
    license='Apache-2.0',
    packages=find_packages(exclude=('docs', 'tests', 'scripts')),
    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
)
