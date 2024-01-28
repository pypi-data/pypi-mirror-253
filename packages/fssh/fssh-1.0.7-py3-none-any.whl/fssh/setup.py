#!/usr/bin/python3

import subprocess
import os
import getpass

def setup():
    print(
    '''
    SETUP `fssh`

          /\\
        _/./
    ,-'    `-:.,-'/
    > O )<)    _  (
    `-._  _.:' `-.\\
        `` \;
    '''
          )

    shell = os.environ['SHELL']
    if shell == '/bin/bash':
        shellrc = os.path.join(os.path.expanduser('~'), '.bashrc')
    elif shell == '/bin/zsh':
        shellrc = os.path.join(os.path.expanduser('~'), '.zshrc')
    else:
        print(
        '''
        You will need to manually set the environment variables UTCS_USERNAME (with your username)
        and UTCS_PASSPHRASE (with your SSH passphrase, if applicable) in your shell profile.
        '''
              )
        return;

    print(
    '''
    To fully automate the SSH login process, please provide your UTCS SSH credentials.

    Enter your credentials into the input spaces below, and this script will automatically
    populate your shell profile. These will be saved in the environment variables UTCS_USERNAME
    and UTCS_PASSPHRASE respectively. if you would like to do this manually, follow the below
    instructions.

    skip past these commands below by leaving them both blank.
    you will need to manually set the environment variables utcs_username (with your username)
    and utcs_passphrase (with your ssh passphrase, if applicable) in your shell profile.
    if you are using bash then your shell profile is `~/.bashrc`.
    if you are using zsh then it is `~/.zshrc`.
    '''
          )
    
    username = input('utcs username (required): ')
    passphrase = getpass.getpass('utcs ssh passphrase (optional): ')

    if username:
        with open(shellrc, 'a') as f:
            f.write(f'export UTCS_USERNAME="{username}"\n')

    if passphrase:
        with open(shellrc, 'a') as f:
            f.write(f'export UTCS_PASSPHRASE="{passphrase}"\n')

    print(
    '''
    Setup complete.
    You may now use `fssh`. See `fssh -h` for help.
    '''
        )


if __name__ == '__main__':
    setup()
