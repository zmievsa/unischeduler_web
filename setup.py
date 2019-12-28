from setuptools import setup


requires = [
    'unischeduler',
    'flask',
    'gunicorn'
]

setup(
    name="unischeduler_web",
    version="0.2",
    packages=['unischeduler_web'],
    install_requires=requires,

    # metadata to display on PyPI
    author="Stanislav Zmiev",
    author_email="szmiev2000@gmail.com",
    description="Web interface for unischeduler",
    license="MIT",
    project_urls={"Source Code": "https://github.com/Varabe/unischeduler_web"},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)