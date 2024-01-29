from distutils.core import setup

setup(
    name='wttch-train-helper',
    version='0.0.15',
    description="Wttch's Train Helper",
    author="wttch",
    packages=[
        'wttch',
        'wttch.train',
        'wttch.train.data',
        'wttch.train.notification',
        'wttch.train.torch',
        'wttch.train.utils',
    ],
    package_dir={
        '': 'src/wttch-train-helper'
    },
    requires=['torch', 'numpy', 'prettytable']
)
