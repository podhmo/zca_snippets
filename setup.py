from setuptools import setup, find_packages
requires = [
    "zope.interface"
    ]

setup(name='zca_snippets',
      version='0.0.2',
      description='snippets for zope.interface',
      long_description="", 
      author='podhmo',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3'
      ],
      package_dir={'': '.'},
      packages=find_packages('.'),
      install_requires = requires,
      test_suite="zca_snippets.tests", 
      entry_points = """
      [console_scripts]
      zca-snippets = zca_snippets.snippets:main
      zca-list = zca_snippets.list:main
      """,
      )
