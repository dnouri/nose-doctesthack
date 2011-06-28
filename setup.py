from setuptools import setup

setup(
    name='nose-doctesthack',
    version='0.1',
    url='http://github.com/dnouri/nose-doctesthack',
    author='Daniel Nouri',
    author_email='daniel.nouri@gmail.com',
    description='Add meaningful pdb post-mortem debugging for doctests to nose',
    long_description = """\
When using the built-in plugin's ``--pdb-failures`` with doctests, the
debugger's location isn't useful.  It will happily drop you into some
doctest code.  This package adds a ``-D`` command that works the same
way as ``--pdb-failures`` except it allows debugging of the actual
failing code with doctests.
""",
    install_requires=['nose'],
    license='MIT License',
    keywords='nose nosetests plugin debug pdb',
    py_modules=['nose_doctesthack'],
    entry_points={
        'nose.plugins': ['nose-doctesthack = nose_doctesthack:Pdb']},
    )
