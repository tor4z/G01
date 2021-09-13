from distutils.core import setup


def gen_code():
    import datetime
    d = datetime.datetime.now()
    date_str = d.strftime('%Y%m%d%H%M%S')
    return f'dev{date_str}'


__version__ = f'0.0.1-{gen_code()}'


setup(
    name='g01',
    version=__version__,
    description='A Computational Graph',
    author='tor4z',
    author_email='vwenjie@hotmail.com',
    # install_requires=[],
    packages=[
        'g01'
    ]
)
