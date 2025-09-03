from setuptools import setup, find_packages

setup(
    name="modu-muse",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "Pillow"
    ],
    author="Wissem Elkarous",
    description="Modular multimodal pipeline for vision-to-LLM integration",
    url="https://github.com/ELkarousWissem/ModuMuse"
)
