from setuptools import setup

setup(
    name='nx100_remote_control',
    packages=[
        'nx100_remote_control.module',
        'nx100_remote_control.objects'
    ],
    package_dir={'': 'nx100_remote_control'},
    include_package_data=True,
)
