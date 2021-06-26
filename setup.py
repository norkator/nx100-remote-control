from setuptools import setup

setup(
    name='nx100_remote_control',
    packages=[
        'nx100_remote_control',
        'nx100_remote_control.module',
        'nx100_remote_control.objects'
    ],
    package_dir={'': 'src'},
    include_package_data=True,
)
