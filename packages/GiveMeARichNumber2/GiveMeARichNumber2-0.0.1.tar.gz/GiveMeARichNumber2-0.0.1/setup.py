import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GiveMeARichNumber2",  # 项目的名字，将来通过pip install ******安装，不能与其他项目重复，否则上传失败
    version="0.0.1",  # 项目版本号，自己决定吧
    author="jojo",  # 作者
    description="luckyNumber 36+2",  # 项目描述
    url="",  # 项目的地址，比如github或者gitlib地址
    packages=setuptools.find_packages(),  # 这个函数可以帮你找到包下的所有文件，你可以手动指定
    # 该软件包仅与Python 3兼容，根据MIT许可证进行许可，并且与操作系统无关。您应始终至少包含您的软件包所使用的Python版本，软件包可用的许可证以及您的软件包将使用的操作系统。有关分类器的完整列表，请参阅 https://pypi.org/classifiers/。
    install_requires=[
        'requests>=2.25.1',
        'beautifulsoup4>=4.9.3',
        'selenium>=3.141.0',
        'lxml>=4.6.3'
    ],  # 项目依赖，也可以指定依赖版本
    entry_points={
        'console_scripts': [
            'fiction=sampleSprider_old.SampleSprider3_Fiction:main',
            'comics=sampleSprider_old.SampleSprider4_Comics1:main'
        ]
    }
)

