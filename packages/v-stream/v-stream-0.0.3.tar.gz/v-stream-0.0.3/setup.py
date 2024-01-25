from setuptools import setup, find_packages

setup(
    name='v-stream',
    version='0.0.3',
    description='STREAM: Spatio-TempoRal Evaluation and Analysis Metric for Video Generative Models',
    author='proinit',
    author_email='seojun.kim@unist.ac.kr',
    url='https://github.com/pro2nit/STREAM',
    install_requires=[
        'torch',
        'tqdm',
        'numpy',
        'top-pr'],
    packages=find_packages(exclude=[]),
    keywords=['pypi', 'video', 'evaluation', 'stream', 'v-stream'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)