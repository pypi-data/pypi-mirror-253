import os
import re
import io
import setuptools

ROOT_DIR = os.path.dirname(__file__)


def find_version(*filepath):
    # Extract version information from filepath
    # Adapted from:
    #  https://github.com/ray-project/ray/blob/master/python/setup.py
    with open(os.path.join(ROOT_DIR, *filepath)) as fp:
        version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                                  fp.read(), re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError('Unable to find version string.')


def parse_readme(readme: str) -> str:
    """Parse the README.md file to be pypi compatible."""
    # Replace the footnotes.
    readme = readme.replace('<!-- Footnote -->', '#')
    footnote_re = re.compile(r'\[\^([0-9]+)\]')
    readme = footnote_re.sub(r'<sup>[\1]</sup>', readme)

    # Remove the dark mode switcher
    mode_re = re.compile(
        r'<picture>[\n ]*<source media=.*>[\n ]*<img(.*)>[\n ]*</picture>',
        re.MULTILINE)
    readme = mode_re.sub(r'<img\1>', readme)
    return readme


install_requires = [
    'wheel',
    # NOTE: ray requires click>=7.0.
    'click >= 7.0',
    'pytest==7.4.3',
    'prettytable',
    'schema==0.7.5',
    'jinja2',
    # Cython 3.0 release breaks PyYAML 5.4.* (https://github.com/yaml/pyyaml/issues/601)
    # <= 3.13 may encounter https://github.com/ultralytics/yolov5/issues/414
    'pyyaml > 3.13, != 5.4.*',
    'ray[default]',
    # Ray job requires pydantic<2.0.0, due to pydantic API changed from version 1.x to 2.x
    # Ref: https://github.com/ray-project/ray/issues/37239
    # >=1.10.8 is needed for ray>=2.6.
    # Ref: https://github.com/ray-project/ray/issues/35661
    'pydantic < 2.0, >= 1.10.8',
    'pendulum==2.1.2',
    'requests==2.31.0',
    'paramiko==3.3.1',
    'colorama',
    'kubernetes>=20.13.0',
    'portforward',
]

long_description = ''
readme_filepath='README.md'
if os.path.exists(readme_filepath):
    long_description = io.open(readme_filepath, 'r', encoding='utf-8').read()
    long_description = parse_readme(long_description)

setuptools.setup(
    name='pj-opus',
    version=find_version('opus', '__init__.py'),
    packages=setuptools.find_packages(),
    author='AST',
    author_email='zhuzhihao@pjlab.org.cn',
    license='Apache 2.0',
    readme='README.md',
    description='Opus: An auto-launcher for ray clusters on clouds',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['opus = opus.cli:cli']
    },
    include_package_data=True,
)
