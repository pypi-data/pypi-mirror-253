from distutils.core import setup
setup(
  name = 'sunesh_tables1',         # How you named your package folder (MyLib)
  packages = ['sunesh_tables'],   # Chose the same as "name"
  version = 'v1.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Just for learning',   # Give a short description about your library
  author = 'Sunesh Pandita',                   # Type in your name
  author_email = 'a@a.com',      # Type in your E-Mail
  url = 'https://github.com/SUNESHPANDITA/Learning_PYPI',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/SUNESHPANDITA/Learning_PYPI/archive/refs/tags/v1.0.1.tar.gz',    # I explain this later on
  keywords = ['Tables'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)