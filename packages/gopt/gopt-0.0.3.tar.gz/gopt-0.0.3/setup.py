import setuptools

packages = setuptools.find_packages()  # 唯一的包名，自己取名
setuptools.setup(name='gopt',
                 version='1.0',
                 author='xgh',
                 packages=packages,
                 package_dir={'requests': 'requests'}, )
