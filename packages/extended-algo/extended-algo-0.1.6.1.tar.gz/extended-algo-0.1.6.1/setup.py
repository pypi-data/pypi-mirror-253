import time

from setuptools import setup
import shutil

try:
    print('Removing cache data before install...')
    shutil.rmtree('./build/')
    shutil.rmtree('./dist/')
    shutil.rmtree('./extended_algo.egg-info/')
    shutil.rmtree('./.pytest_cache/')
    time.sleep(1)
except:
    ...

setup(name='extended-algo',
      version='0.1.6.1',
      description='wrapper for creating event and vector algo that supports the extended-chart',
      url='https://github.com/karunkrishna/extended_algo',
      author='Karun Krishna',
      author_email='karun.krishna@gmail.com',
      license='MIT',
      packages=['extended_algo', 'extended_algo.engine', 'extended_algo.market', 'extended_algo.report',
                'extended_algo.report.calculate', 'extended_algo.report.utils', 'extended_algo.market.style',
                'extended_algo.market.utils'],
      install_requires=['pandas', 'python-dotenv', 'pandas', 'pandas-ta', 'extended-chart', 'tqdm', 'pyarrow'],
      zip_safe=False
      )
