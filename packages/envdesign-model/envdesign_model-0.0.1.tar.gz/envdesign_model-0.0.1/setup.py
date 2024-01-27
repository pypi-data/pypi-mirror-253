from setuptools import setup, find_packages


INSTALL_DEPS = [
                'numpy',
                'pandas',
                'graphing',
                'optimizn'
               ]
TEST_DEPS = ['pytest']
DEV_DEPS = []


setup(name='envdesign_model',
      version='0.0.1',
      author='Akshay Sathiya, Rohit Pandey',
      author_email='akshay.sathiya@gmail.com, rohitpandey576@gmail.com',
      description='A domain-agnostic model that uses graph theory and '
      + 'optimization algorithms to design testing environments.',
      packages=find_packages(exclude=['tests']),
      long_description='A domain-agnostic model that uses graph theory and '
      + 'optimization algorithms to design testing environments.',
      zip_safe=False,
      install_requires=INSTALL_DEPS,
      include_package_data=True,
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
      extras_require={
          'dev': DEV_DEPS,
          'test': TEST_DEPS,
      },
      tests_require=['pytest'],
      )
