from distutils.core import setup
setup(
    name='topsis102116086',         # How you named your package folder (MyLib)
    packages=['topsis102116086'],   # Chose the same as "name"
    version='0.2',      # Start with a small number and increase it with every change you make
    license='MIT',
    install_requires=[            # I get to this in a second
        'pandas',
        'numpy',
        'sklearn',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
