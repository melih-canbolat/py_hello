from setuptools import find_packages, setup

package_name = 'py_hello'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='melih-canbolat',
    maintainer_email='melih.canbolat@gmail.com',
    description='Simple python package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talk = py_hello.hello_world:main',
        ],
    },
)
