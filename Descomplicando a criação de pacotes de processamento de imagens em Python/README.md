# Desafios e soluções da [Dio](https://www.dio.me/)

## Bootcamp Geração Tech Unimed-BH - Ciência de Dados

### Descomplicando a criação de pacotes de processamento de imagens em Python

Nesta pasta você encontrará os desafios para conclusão da etapa "Descomplicando a criação de pacotes de processamento de imagens em Python" do Bootcamp "Geração Tech Unimed-BH - Ciência de Dados" da [dio.me](https://www.dio.me/).

Neste projeto você ecnontrará como criar o seu pacote de processamento de imagens em Python e disponibilizá-lo no repositório Pypi. Assim você poderá reutilizá-lo facilmente e compartilhá-lo com outras pessoas. A especialista, professora Karina Kato, também vai mostrar um exemplo de pacote para processamento de imagens.

## ✏️ Objetivos
- [X] Entender conceitos relacionados aos pacotes;
- [X] Atualizar o projeto e gerar as distribuições;
- [X] Publicar o pacote.

## ✔️ Requisitos 
Os requisitos para realizar este trabalho são:

<p align="center">
	<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
	<img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white">
</p>

- `Python`;
- `Ter um projeto a ser empacotado`;
- `Git (recomendado)`.

## 🖼️ Image_processing
O pacote image_procesing é usado para:
	Processamento:
		- Correspondências de histogramas;
		- Semelhança estrutural;
		- Redimensionar imagem.
	Utilidades:
		- Ler imagem;
		- Salvar imagem;
		- Plotar imagem;
		- Plotar resultado;
		- Plotar histograma.

## ⚙️ Instalação
Utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar o image procesing package.

```bash
pip install image_processing
```

## 🕹️ Comandos para criar o pacote:
- Comandos de instalação:
```bash
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools
```
- Comanods para criar distribuição:
```bash
python setup.py sdist bdist_wheel
```