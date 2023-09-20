# force_recompile_shaders

Removes all shader caches from Nvidia, AMD, and Intel Arc GPUs on Windows.

Used to troubleshoot Starfield in particular, but applies to other games generally.

**NOTE**  
On Linux, only Starfield shaders will be removed.

## Setup
Requires [Python 3.11](https://www.python.org/downloads/).

## Usage
```bash
# run interactively (prompts before deleting individual files)
python force_recompile_shaders.py -i

# run unattended
python force_recompile_shaders.py
```

## Development
VSCode [launch.json](.vscode/launch.json) is included for debugging and passing arguments.

Uses standard library so no dependencies outside Python itself are required.

Currently only supports the interactive flag:
```json
"args": ["-i"]
```


## Futher Reading
[[Guide] How to force recompile shaders : Starfield](https://www.reddit.com/r/Starfield/comments/16703yo/guide_how_to_force_recompile_shaders/)

[MoscaDotTo/Winapp2: A database of extended cleaning routines for popular Windows PC based maintenance software.](https://github.com/MoscaDotTo/Winapp2/)
