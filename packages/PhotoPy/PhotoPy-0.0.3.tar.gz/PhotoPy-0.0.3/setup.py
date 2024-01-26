from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Biblioteca criada para a alterações e manipulações de imagens'
LONG_DESCRIPTION = 'Explore o potencial ilimitado da sua imaginação com o PhotoPy, uma ferramenta poderosa e intuitiva projetada para elevar suas criações visuais a novos patamares. Seja você um entusiasta amador ou um profissional experiente, este pacote oferece uma gama de recursos inovadores para transformar suas fotos em verdadeiras obras de arte.'

setup(
    name='PhotoPy',
    version=VERSION,
    author='Augusto Almondes and Rafael Barbosa',
    author_email='augusto7666@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy','opencv-python'],
    
    keywords=['python','PhotoPy','Image'],
    classifiers= [
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)