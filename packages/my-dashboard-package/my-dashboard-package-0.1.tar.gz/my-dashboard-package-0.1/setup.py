from setuptools import setup

setup(
    name='my-dashboard-package',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'streamlit',
        'pandas',
        # Add any other dependencies
    ],
    entry_points={
        'console_scripts': [
            'my_dashboard_app = main:main',
        ],
    },
)
