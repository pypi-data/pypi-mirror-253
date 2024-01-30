from setuptools import setup

setup(
    name='mymodelmonitoringdashboardpackage',
    version='0.7',
    py_modules=['main'],
    install_requires=[
        'streamlit',
        'pandas',
        # Add any other dependencies
    ],
    entry_points={
        'console_scripts': [
            'my_dashboard_app = my_dashboard:main',
        ],
    }
)
