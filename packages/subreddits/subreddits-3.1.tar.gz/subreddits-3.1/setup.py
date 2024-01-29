from distutils.core import setup


setup(
    name = 'subreddits',         # How you named your package folder (MyLib)
    packages = ['subreddits'],   # Chose the same as "name"
    version = '3.1',      # Start with a small number and increase it with
    # every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Backup or Clean Reddit Account',   # Give a short description about your library
    long_description="Instructions: https://github.com/tsaklidis/subreddits/blomaster/README.md",
    homepage = "https://github.com/tsaklidis/subreddits",
    author = 'Stefanos I. Tsaklidis',
    author_email = 'stefanos@tsaklidis.gr',      # Type in your E-Mail
    url = 'https://github.com/tsaklidis/subreddits',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/tsaklidis/subreddits/archive/refs/tags/SUB-2.1.tar.gz',    # I explain this later on
    keywords = ['reddit', 'backup', 'export', 'clean', 'subreddits'],
    install_requires=[            # I get to this in a second
        'praw==7.7.1',
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: End Users/Desktop',      # Define that your audience are developers
        'Topic :: Communications',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ],
)
