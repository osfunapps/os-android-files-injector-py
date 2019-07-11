Introduction
------------

Thi script will inject:
* strings.xml
* google-services.json
* logo.png 
* assets\
and more files into an android app programmatically (dynamically).

## Installation
Install via pip:

    pip install os-android-files-injector

## Usage       
From Python:
    
    import os_android_files_injector.AppFilesInjector as fi
    
    fi.run('/path/to/android/project',
           '/path/to/strings.xml',
           '/path/to/logo.png',
           '/path/to//google-services.json',
           ['/path/to/asset_file_1.png', '/path/to/asset_file_2.mov', '/path/to/asset_file_3.txt'],
           clear_old_assets=False)
  
Or from the command line:

    python3 -c 'import os_android_files_injector.AppFilesInjector as fi; 
    fi.run("/path/to/android/app",
           "/path/to/strings.xml",
           "/path/to/logo.png",
           "/path/to//google-services.json",
           ["/path/to/asset_file_1.png", "/path/to/asset_file_2.mov", "/path/to/asset_file_3.txt"],
           clear_old_assets=False)'


## Licence
MIT