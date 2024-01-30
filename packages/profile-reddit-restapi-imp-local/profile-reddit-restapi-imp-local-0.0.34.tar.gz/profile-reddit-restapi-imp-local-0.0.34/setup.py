import setuptools

REPO_NAME = 'profile-reddit-restapi-imp-local'
package_dir = 'profile_reddit_restapi_imp_local'

setuptools.setup(
     name=REPO_NAME,
     version='0.0.34',  # https://pypi.org/project/profile-reddit-restapi-imp-local/
     author="Circles",
     author_email="info@circles.life",
     url="https://github.com/circles-zone/profile-reddit-restapi-imp-local-python-package",
     packages=[package_dir],
     package_dir={package_dir: f'{package_dir}/src'},
     package_data={package_dir: ['*.py']},
     long_description="Profile Reddit REST API Implementation Local Python Package",
     long_description_content_type='text/markdown',
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
        'praw>=7.4.0',
        'tqdm>=4.64.1',
        'database-mysql-local>=0.0.11',
        'importer-local>=0.0.6',
        'logzio-python-handler>=4.1.0',
        'profiles-local>=0.0.11',
        'url-remote>=0.0.22',
        'python-dotenv>=1.0.0',
        'logger-local>=0.0.46',
        'entity-type-local>=0.0.13',
        'group-remote>=0.0.85',
        'source-data-local>=0.0.3'
        ]
)
