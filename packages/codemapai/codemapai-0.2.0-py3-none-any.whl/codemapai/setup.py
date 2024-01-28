import setuptools

setuptools.setup(
    name='codemapai',
    version='0.1.0',
    author='Ricky Ho, Oliver Wu, Temin Ghong, Andy Huang',
    author_email='horicky78@gmail.com, oliverwu@umich.edu, tghong@umich.edu, huandy@umich.edu',
    description='A diagram generator that creates ASCII diagrams of projects using generative AI',
    packages=setuptools.find_packages(),
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ],
    install_requires=[
        'openai==1.10.0',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'codemapai=codemapai.main:main',
        ],
    },
    python_requires='>=3.8',
)