from setuptools import setup, find_packages

setup(
    name='tamqp',
    version='0.0.7',
    description='Adaptable Python library to interact with cloud RabbitMQ providers',
    url='https://s-g@bitbucket.org/yployalty/tamqp',
    author='Saurabh Gupta',
    author_email='sgupta@taekus.com',
    license='GNU General Public License v3.0',
    packages=find_packages(),
    install_requires=['pika==1.3.2', ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
)
