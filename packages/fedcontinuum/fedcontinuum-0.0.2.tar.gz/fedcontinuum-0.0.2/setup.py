from setuptools import setup, find_packages

requirements = [
        'loguru',  # 依赖项列表
        'tqdm',
        'pyyaml',
        'wandb',
        'torch',
        'torchvision',
    ]

setup(
    name='fedcontinuum',  # 包名称
    version='0.0.2',  # 包版本
    author='Ray',  # 作者名称
    author_email='b6023794@newcastle.ac.uk',  # 作者邮箱
    description='FedContinuum: Federated Continual Learning Scenarios Management Tool',  # 简短描述
    long_description=open('README.md').read(),  # 长描述，通常是README
    long_description_content_type='text/markdown',  # 长描述的内容类型，例如：text/markdown 或 text/plain
    url='https://github.com/ray-ruisun/FedContinuum',  # 项目主页链接
    packages=find_packages(),  # 自动查找包含 '__init__.py' 的目录
    keywords=[
        "distributed machine learning",
        "federated learning",
        "continual learning",
        "federated continual learning",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",  # 支持的 Python 版本
        'License :: OSI Approved :: Apache Software License',  # 许可证
        'Operating System :: OS Independent',  # 操作系统
    ],
    install_requires=requirements,
    python_requires='>=3.6',  # Python 版本要求
)
