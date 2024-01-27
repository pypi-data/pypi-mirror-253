from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ZSync',
    version='1.3',
    packages=find_packages(),
    url='https://github.com/LittleHeroZZZX/ZSync',
    license='MIT',
    author='ZhouXin',
    author_email='zhou.xin2000@outlook.com',
    description='a cli tool for syncing local files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
            'console_scripts': [
                'zsync=zsync.ZSync:main',  # 'sync'是命令名，'your_package.sync'是模块名，'main'是你的脚本中用于启动程序的函数
            ],
        },
    install_requires=['dotmap', 'tqdm', 'PyYAML'],
    python_requires='>=3.12',
)
