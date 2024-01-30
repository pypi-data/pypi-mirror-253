from setuptools import setup

setup(
    name='my-dashboard-package',
    version='0.2',
    py_modules=['main'],
    install_requires=[
        'streamlit',
        'pandas',
        # Add any other dependencies
    ],
    entry_points={
        'console_scripts': [
            'my_dashboard_app = monitoring_dashboard:main',
        ],
    },
)
