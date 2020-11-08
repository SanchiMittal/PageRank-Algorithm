from setuptools import setup
setup(name ='pagerank_basic',
      version = 0.2,
      url = 'https://github.com/SanchiMittal/PageRank-Algorithm.git',
      description = 'Basic Pagerank Algorithm that generates a random graph and finds ranks for the nodes (pages).',
      author='Sanchi Mittal, Satyabrata Panda',
      packages=['pagerank_basic'],
      license='MIT',
      install_requires=['matplotlib','numpy','networkx'])