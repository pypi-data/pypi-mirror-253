from setuptools import setup,find_packages
setup(name='PPM_FSE',
      version='0.0.1',
      description='Automated Generation of Diverse Programming Problems for Benchmarking Code Generation Models',
      author='Ning',
      author_email='fengxiaoning1746@link.tyut.edu.cn',
      requires= [], # 定义依赖哪些模块
      packages=find_packages(),  # 系统自动从当前目录开始找包
      license="apache 2.0"
      )
