from setuptools import setup, find_packages

setup(
    name="TkLiteUI",
    version="0.3",
    description="Basit ve hafif bir Tkinter kullanıcı arayüzü kütüphanesi",
    long_description="Bu kütüphane, Tkinter tabanlı basit ve kullanışlı arayüzler oluşturmak için geliştirilmiştir. Kolay kullanımı ve hafif yapısıyla, çeşitli uygulamalarda hızlı arayüz geliştirmeyi sağlar.",
    author="Adem Ulker",
    author_email="ademulker055@gmail.com",
    url="https://github.com/ademulkerx/TkLiteUI",  # Projeye ait gerçek URL'nizi buraya ekleyin
    packages=find_packages(),
    install_requires=[
        # Bağımlılıklarınızı burada belirtin. Tkinter için gerek yoktur.
    ],
    classifiers=[
        # PyPI'da kütüphanenizin nasıl sınıflandırılacağına dair bilgiler
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",  # Kullanılan lisans tipi
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',  # Desteklenen minimum Python sürümü
    keywords='tkinter, GUI, user interface',  # Kütüphanenizle ilgili anahtar kelimeler
)
