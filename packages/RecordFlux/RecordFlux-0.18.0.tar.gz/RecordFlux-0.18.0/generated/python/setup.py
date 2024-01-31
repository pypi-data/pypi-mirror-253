


from setuptools import setup, find_packages


setup(
    name='Librflxlang',
    version='0.18.0',
    packages=['librflxlang'],
    package_data={
        'librflxlang':
            ['*.{}'.format(ext) for ext in ('dll', 'so', 'so.*', 'dylib')]
            + ["py.typed"],
    },
    zip_safe=False,
)
