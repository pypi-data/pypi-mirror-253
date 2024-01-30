from setuptools import setup, find_packages

setup(
    name='PayPaython',
    version='0.5.8',
    keywords = "paypay",
    long_description="https://github.com/taka-4602/PayPaython\n詳細はGitHubからお願いします",
    author='taka4602',
    author_email='shun4602@gmail.com',
    url='https://github.com/taka-4602/PayPaython',
    description='A API wrapper for the PayPayAPI',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)