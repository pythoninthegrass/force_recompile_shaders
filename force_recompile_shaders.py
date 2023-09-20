#!/usr/bin/env python3

import os
import sys
import time
import platform
from pathlib import Path

# set log file
log_file = Path(__file__).parent/'force_recompile_shaders.log'

# environment variables
userprofile = os.getenv('USERPROFILE')
localappdata = os.getenv('LOCALAPPDATA')

# init set for shader cache paths
shader_cache_paths = set()

# set cache paths
if platform.system() == 'Windows':
    NVIDIA_CACHE = Path(localappdata)/'NVIDIA/DXCache'
    AMD_CACHE = Path(localappdata)/'AMD/DXCache'
    INTEL_CACHE = Path(userprofile)/'AppData/LocalLow/Intel/ShaderCache'
    PIPELINE_CACHE = Path(localappdata)/'Starfield'
    shader_cache_paths.add(NVIDIA_CACHE)
    shader_cache_paths.add(AMD_CACHE)
    shader_cache_paths.add(INTEL_CACHE)
    shader_cache_paths.add(PIPELINE_CACHE)
elif platform.system() == 'Linux':
    # if you use steam but launch as non-steam, you have to find your compatdata folder
    # then replace 1716740 directory
    SHADER_CACHE = Path.home()/'.local/share/Steam/steamapps/shadercache/1716740/mesa_shader_cache_sf'
    shader_cache_paths.add(SHADER_CACHE)


def get_shader_cache_files():
    """Get all shader cache files from shader cache paths."""

    shader_cache_files = [
        i for path in shader_cache_paths for i in path.glob("**/*")
    ]

    timestamp = time.strftime("--- %Y-%m-%d %H:%M:%S ---")

    with open(log_file, 'a') as f:
        f.write(f"{timestamp}\n")
        f.write(f"[Shader Cache Files]\n")
        [f.write(f"{i}\n") for i in shader_cache_files]

    return shader_cache_files


def delete_shader_cache_file(files):
    """Delete shader cache files."""

    # check for interactive mode
    if len(sys.argv) == 2 and sys.argv[1] == '-i':
        interactive = True
    else:
        interactive = False

    # init deleted set
    deleted_shader_cache_files = set()

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"START: {timestamp:>21}")

    # delete shader cache files
    for file in files:
        try:
            if file.is_file() and not file.name.startswith('GPU_CRASH__'):
                basename = file.name
                if interactive:
                    decision = input(f"Delete {basename}? (y/n): ")
                    match decision:
                        case 'y'|'Y':
                            file.unlink()
                            deleted_shader_cache_files.add(file)
                        case 'n'|'N':
                            print(f'Skipping {basename}')
                        case _:
                            print(f"Invalid input. Skipping {basename}.")
                else:
                    file.unlink()
                    deleted_shader_cache_files.add(file)
        except OSError as e:
            print(f"Error: {file}: {e.strerror}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"END: {timestamp:>23}")
    with open(log_file, 'a') as f:
        f.write("[Deleted Shader Cache Files]\n")
        [f.write(f"{file}\n") for file in deleted_shader_cache_files]

    print(f"DELETED: {len(deleted_shader_cache_files)} shader cache files.")


def main():
    shader_cache_files = get_shader_cache_files()
    delete_shader_cache_file(shader_cache_files)


if __name__ == '__main__':
    main()
