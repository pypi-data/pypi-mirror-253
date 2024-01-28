# fssh 🐟

> "fish swim fast" - someone, probably

A fast SSH tool for UT Austin CS students.

# Introduction

SSH is tedious. Go to host machine list. Find optimal machine. Enter command. Interact. Login.

It could be faster.

![fssh-demo](https://github.com/migopp/fssh/assets/128272843/7f4c80c1-f871-438b-b1ee-99a1108de418)

# Prereqs

1. have bash or zsh or some other shell
2. have python
3. set up [UT SSH](https://www.cs.utexas.edu/facilities-documentation/ssh-keys-cs-mac-and-linux)

# Installation

1. `pip install fssh`
2. `fssh-setup`
3. profit 💰

# Usage

```
fssh
```

The above commmand will do __everything__ for you.

If that's not what you want, you can opt to add in the `-p` flag to print the optimal machine (it will also copy the correct command to your clipboard, i.e., `ssh <YOUR UTCS USERNAME>@<OPTIMAL HOST>.cs.utexas.edu`).

`fssh -h` for help (there's not a lot, it's pretty simple).

# On `fssh-setup`

Part of SSH is entering your UTCS username and SSH passkey—fssh cannot bypass this, as it sadly is not magic. As such, to fully utilize fssh, [the script needs access to this information somehow](https://github.com/migopp/fssh/blob/main/src/fssh/__main__.py).

This is implemented through a setup script that logs your credentials to your respective shell profile (where you keep your API keys and such). As such, the information is recorded on a safe place on your local machine.

Without interacting with `fssh-setup`, the script cannot provide you any more information than the optimal host name.

# Terminal Choice

The full `fssh` functionality works great for most terminals. Not so much for some fancier ones (_cough, cough Warp_). You may not get full functionality of your fancy terminal emulator. In such cases, the `fssh -p` command will probably do you best.
