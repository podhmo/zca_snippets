from setuptools import setup, find_packages
requires = [
    "zope.interface"
    ]

setup(name='zca_snippets',
      version='0.0.1',
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
      zca_snippets = zca_snippets.snippets:main
      zca_list = zca_snippets.list:main
      """,
      )
