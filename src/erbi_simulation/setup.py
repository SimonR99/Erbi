from setuptools import setup

package_name = 'erbi_cv'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Simon Roy',
    maintainer_email='simonroy99@hotmail.ca',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "cv_alive_pub = erbi_cv.alive_publisher:main",
            "cv_alive_sub = erbi_cv.alive_subscriber:main",
        ],
    },
)
