from setuptools import setup,find_packages

setup(
    name='database_num_sort',
    version='0.0.1',
    description='整理表中此列的数字是否中断，中断将后面的数字减一 ',
    author='yuchu',
    author_email='yuchus@foxmail.com',
    packages=find_packages(),
    long_description_content_type="text/markdown",
)
