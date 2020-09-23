from setuptools import setup

setup(
    name='anomaly_analyzers',
    version='0.1.0',
    packages=['gaussian_anomaly_detector'],
    url='https://dynamite.ai',
    license='',
    author='Dynamite Analytics',
    author_email='jamin@dynamite.ai',
    description='Detect anomalies in events',
    install_requires=[
        'dynamite-analyzer-framework',
        'elasticsearch',
        'scipy',
        'sklearn',
        'pandas'
    ],
)
