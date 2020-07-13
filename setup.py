# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('readme.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="easy_vk",
    version="0.0.28",
    author="Phinnik",
    author_email="elecdron@gmail.com",
    description="Обертка для VK api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Phinnik/easy_vk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <3.8',
    install_requires=['requests', 'aiohttp', 'pydantic']
)