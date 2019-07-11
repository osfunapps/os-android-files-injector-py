from distutils.core import setup

setup(
    name='os-android-files-injector',
    packages=['os_android_files_injector'],
    version='1.0',
    license='MIT',
    description='Will inject strings.xml, google-services.json, logo.png, assets and more files into an android app programmatically (dynamically)',
    author='Oz Shabat',
    author_email='osfunapps@gmail.com',
    url='https://github.com/osfunapps',
    keywords=['python', 'osfunapps', 'injector', 'android', 'files', 'strings', 'logo', 'assets'],
    install_requires=['ostools'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
