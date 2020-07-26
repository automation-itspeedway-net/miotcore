# miot
Modular Internet of Things - Core modules

STATUS:  PRE-ALPHA  ** UNSTABLE DO NOT INSTALL **

VERSION: 1.0.3.8
    - WARNING - Unstable development version
    - Not feature complete
    - Under development
    - Not ready for internal testing

A Pre-Alpha release:
* Is still under development and considered unstable
* May have had limited or no internal testing.
* May not be feature complete
* May have features that are partially complete or not working. 
* May have known or unknown bugs
* May operate in an unexpected way. 
* May contain output debugging data to logs or screen.
* Is NOT supported: Use at your own risk.

Please do not raise tickets for bugs found in this release.

# INFORMATION

These are the core modules that are used by MIoT.

More information about MIoT is available from it's [project page on github][https://github.com/automation-itspeedway-net/miot].

# FEATURES:

* Central modules for mqtt, logs and config used by other packages
* Adds functionality by means of REPL to 'miot' shell command

# PLATFORMS

    - Linix (Mint)  -   tbc
    - Linux (Other) -   Untested
    - Raspbarian    -   tbc
    - Windows       -   Currently Unsupported
    
# PREREQUISITES

    * [miot][https://github.com/automation-itspeedway-net/miot]
    * python 3
    * pip
    * git

# INSTALLATION

    pip3 install --upgrade miot
    
Check that is it working:

    miot version

If this fails; you probably need to add  ~/.local/bin to your path. This is a common problem on Debian/Ubuntu/Mint because it is not included by default. Run these commands and then try testing it works again.

    echo export PATH="$HOME/.local/bin:$PATH">>~/.bashrc
    source ~/.bashrc

Now that it is working, run setup

    miot setup
    
# UPGRADE

    miot disable
    pip3 install --upgrade miot
    miot enable
    
# KNOWN BUGS

* Pre-Alpha versions will contain known and unknown bugs.
