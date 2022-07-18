![dark.jpg](https://github.com/mocowcow/coh2-dark-power/blob/master/asssets/img/dark.jpg?raw=true)
# COH2 Dark Power
**COH2 Dark Power** is an application that can observe whether specific players are currently in game(4v4 mode only), based on [coh2stats](https://coh2stats.com/) Live Games API.

Supported languages:  
- English
- Traditional Chinese
- Simplified Chinese
- Polish
- Japanese

# Features
- **Query players**: list all in game players you care about.
- **Query teams**: list all in game teams which include specific player.

# Installation
Clone this repo and run build.bat, then place lists, locales, config, icon and the .exe into same folder.

Or [download](https://mega.nz/file/tMkRHDaB#1qkfeiy81dGGOhNm9kso5YRdPHwvhrSuVFDhNAQnbpE) packaged version here.

You can also run gui.py without installation.

# Usage
Just run the application and click query buttions.
![preview.jpg](https://github.com/mocowcow/coh2-dark-power/blob/master/asssets/img/preview.jpg?raw=true)

# Localization
Modify language setting at config.ini.

# Custom Search List
It is also available to establish your own blacklist, just edit blacklist.txt.  
For each id:name pair, you must follow the format:  
> steam id  
> nickname  

Example:
> 765611983********  
> Gardener  