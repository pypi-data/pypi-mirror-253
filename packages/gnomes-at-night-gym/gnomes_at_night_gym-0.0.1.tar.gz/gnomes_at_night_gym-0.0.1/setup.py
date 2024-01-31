from setuptools import setup

setup(
    name="gnomes_at_night_gym",
    version="0.0.1",
    description='An environment for Gnomes at Night based on OpenAI gym.',
    author='Shenghui Chen',
    install_requires=[
        "gymnasium==0.29.1", 
        "pygame==2.5.2", 
        "numpy==1.26.1"
    ],
)