from setuptools import setup


def readme():
    with open('README.md') as target:
        return target.read()


setup(
    name='flask_boilerplate',
    version='0.1',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='flask starter templates boilerplate',
    url='https://github.com/atulmishra-one/flask-boilerplate',
    author='Atul Mishra',
    author_email='atulmishra.one@gmail.com',
    license='MIT',
    packages=['flask_boilerplate'],
    install_requires=[
        'markdown',
    ],
    include_package_data=True,
    zip_safe=False
)