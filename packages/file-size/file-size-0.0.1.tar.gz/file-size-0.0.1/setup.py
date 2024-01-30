from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    page_description = f.read()

setup(
    name='file-size',
    version='0.0.1',
    author="Kauã Fabricio",
    author_email="kauafabriiciio@gmail.com",
    description="It's a simple python package to calculate the file size.",
    long_description= page_description,
    long_description_content_type='text/markdown',
    python_requires= '>=3.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'file_size=file_size.size:file_size'
        ],
    },
)
