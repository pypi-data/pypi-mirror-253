
from distutils.core import setup
setup(
  name = 'Topsis-Harsiddak_102117091',         # How you named your package folder (MyLib)
  packages = ['Topsis-Harsiddak'],   # Chose the same as "name"
  version = '1.0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Contains the Topsis package by Harsiddak on topsis',   # Give a short description about your library
  author = 'Harsiddak Bedi',                   # Type in your name
  author_email = 'bediharsiddak@gmail.com',      # Type in your E-Mail
  url = '',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
)
