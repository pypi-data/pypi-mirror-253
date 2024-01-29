from setuptools import setup, find_packages

setup(
    name='p4pvirus',
    version='1.0.0',
    description='Eine kurze Beschreibung deines Projekts',
    author='PH',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        # Liste der Abhängigkeiten aus der Requirements.txt-Datei
        'DOCOPT==0.6.2',
        'SCIPY==1.11.4',
        'BOKEH==3.3.2',
        # weitere Abhängigkeiten hier
    ],
)

