from setuptools import setup


setup(
    name='parentheses',

    packages=['parentheses'],

    version='1.0.1',

    license='MIT',

    description='Light parentheses parser in Python.',

    long_description_content_type='text/x-rst',
    long_description=open('README.rst', 'r').read(),

    author='Ivan Perzhinsky.',
    author_email='name1not1found.com@gmail.com',

    url='https://github.com/xzripper/parentheses',
    download_url='https://github.com/xzripper/parentheses/archive/refs/tags/v1.0.0-r.tar.gz',

    keywords=['utility', 'string', 'parentheses', 'parsing'],

    classifiers=[
        'Development Status :: 5 - Production/Stable ',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
