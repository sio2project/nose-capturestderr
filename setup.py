from setuptools import setup, find_packages
setup(
    name = "nose-capturestderr",
    version = '1.0',
    author = "The SIO2 Project Team",
    author_email = 'sio2@sio2project.mimuw.edu.pl',
    description = "HTML report generation plugin for nose",
    url = 'http://github.com/sio2devel/nose-capturestderr',
    license = 'GPL',

    packages = find_packages(),

    install_requires = [
        'nose >= 0.11.1',
    ],

    entry_points = {
        'nose.plugins': [
            'capturestderr = nose_capturestderr:CaptureStderr',
        ],
    }
)

