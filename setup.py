from setuptools import setup

setup(
    name='gaussian_anomaly_detector',
    version='0.1.0',
    packages=['gaussian_anomaly_detector'],
    url='https://dynamite.ai',
    license='',
    author='Dynamite Analytics',
    author_email='jamin@dynamite.ai',
    description='Detect anomalies in events',
    install_requires=[
        'dynamite_analyzer_framework',
        'elasticsearch',
        'scipy',
        'sklearn',
        'pandas'
    ],
)
