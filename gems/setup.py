from setuptools import setup, find_packages
packages_to_include = find_packages(exclude = ['test.*', 'test', 'test_manual'])
setup(
    name = 'abhishekse2etestsprophecyioteam_projectautomationchetanpythonreleaseapi1730176548837',
    version = '17301765488371.0.0',
    packages = packages_to_include,
    description = '',
    install_requires = [],
    data_files = ["resources/extensions.idx"]
)
