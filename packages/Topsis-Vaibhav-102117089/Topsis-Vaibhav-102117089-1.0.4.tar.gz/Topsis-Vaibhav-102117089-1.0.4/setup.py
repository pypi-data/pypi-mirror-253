
from distutils.core import setup
setup(
  name = 'Topsis-Vaibhav-102117089',         # How you named your package folder (MyLib)
  packages = ['Topsis-Vaibhav'],   # Chose the same as "name"
  version = '1.0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Contains the Topsis package by Vaibhav on topsis',   # Give a short description about your library
  author = 'Vaibhav Tiwari',                   # Type in your name
  author_email = 'vtiwari1_be21@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/vteam27/topsis-vaibhav-102117089',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/vteam27/topsis-vaibhav-102117089/archive/refs/tags/1.0.4.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
)
