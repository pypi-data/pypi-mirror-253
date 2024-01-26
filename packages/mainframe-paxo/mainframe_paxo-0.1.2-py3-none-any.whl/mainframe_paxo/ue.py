import glob
import os.path
import subprocess
import winreg
from contextlib import closing

import click

from . import tools

# various tools for setting up UE environment and running it.abs

ue = click.Group("ue")


@ue.command()
def setup():
    setup_ue(tools.workdrive_get(), tools.get_engine_path(), tools.get_location())


def setup_ue(work_drive, engine_path, location=None):
    # set up the environment variables
    set_ddc_vars(work_drive, location)

    # register the engine
    register_engine(engine_path)

    # install prerequisites
    install_prerequisites(engine_path)


def set_location(location):
    # set the env vars related to location
    loc = tools.locations[location]
    ddc = loc["ddc"]
    if ddc:
        tools.env_var_set("UE-SharedDataCachePath", ddc)
    else:
        tools.env_var_del("UE-SharedDataCachePath")


def set_ddc_vars(work_drive, location):
    # set local DDC location
    tools.env_var_set("UE-LocalDataCachePath", os.path.join(work_drive, "\DDC"))
    set_location(location)


def register_uproject_handler(engine_path):
    # the engine contains a special execution to act as a shell handler
    # for files with the .uproject extension
    handler = os.path.join(
        engine_path, "Engine", "Binaries", "Win64", "UnrealVersionSelector.exe"
    )
    handler = os.path.abspath(handler)
    cmdhandler = os.path.join(
        engine_path, "Engine", "Binaries", "Win64", "UnrealVersionSelector-Cmd.exe"
    )
    if os.path.exists(cmdhandler):
        cmdhandler = os.path.abspath(cmdhandler)
    else:
        cmdhandler = handler

    # quoted handler for the registry
    quoted_handler = '"' + handler + '"'
    quoted_cmdhandler = '"' + cmdhandler + '"'

    # we must now find the appropriate place in the registry and add it.abs
    # this is a bit tricky, but we can use the python winreg module
    key = winreg.CreateKey(winreg.HKEY_CLASSES_USER, "SOFTWARE\\Classes\\.uproject")
    with closing(key):
        winreg.SetValue(key, "", winreg.REG_SZ, "Unreal.ProjectFile")

    key = winreg.CreateKey(
        winreg.HKEY_CLASSES_USER, "SOFTWARE\\Classes\\Unreal.ProjectFile"
    )
    with closing(key):
        winreg.SetValue(key, "", winreg.REG_SZ, "Unreal Engine Project File")
        winreg.SetValue(key, "VersionSelectorExecutable", winreg.REG_SZ, quoted_handler)
        winreg.SetValue(key, "VersionSelectorCmd", winreg.REG_SZ, quoted_cmdhandler)

        # the DefaultIcon subkey
        subkey = winreg.CreateKey(key, "DefaultIcon")
        with closing(subkey):
            winreg.SetValue(subkey, "", winreg.REG_SZ, quoted_handler)

        with closing(winreg.CreateKey(key, "shell")) as subkey:
            with closing(winreg.CreateKey(subkey, "open")) as subsubkey:
                winreg.SetValue(subsubkey, "", winreg.REG_SZ, "Open")
                with closing(winreg.CreateKey(subsubkey, "command")) as subsubsubkey:
                    winreg.SetValue(
                        subsubsubkey,
                        "",
                        winreg.REG_SZ,
                        quoted_handler + ' /editor "%1"',
                    )

            with closing(winreg.CreateKey(subkey, "run")) as subsubkey:
                winreg.SetValue(subsubkey, "", winreg.REG_SZ, "Launch game")
                winreg.SetValue(subsubkey, "Icon", winreg.REG_SZ, quoted_handler)
                with closing(winreg.CreateKey(subsubkey, "command")) as subsubsubkey:
                    winreg.SetValue(
                        subsubsubkey, "", winreg.REG_SZ, quoted_handler + ' /game "%1"'
                    )

            with closing(winreg.CreateKey(subkey, "rungenproj")) as subsubkey:
                winreg.SetValue(
                    subsubkey, "", winreg.REG_SZ, "Generate Visual Studio project files"
                )
                winreg.SetValue(subsubkey, "Icon", winreg.REG_SZ, quoted_handler)
                with closing(winreg.CreateKey(subsubkey, "command")) as subsubsubkey:
                    winreg.SetValue(
                        subsubsubkey,
                        "",
                        winreg.REG_SZ,
                        quoted_handler + ' /projectfiles "%1"',
                    )

            with closing(winreg.CreateKey(subkey, "switchversion")) as subsubkey:
                winreg.SetValue(
                    subsubkey, "", winreg.REG_SZ, "Switch Unreal Engine version..."
                )
                winreg.SetValue(subsubkey, "Icon", winreg.REG_SZ, quoted_handler)
                with closing(winreg.CreateKey(subsubkey, "command")) as subsubsubkey:
                    winreg.SetValue(
                        subsubsubkey,
                        "",
                        winreg.REG_SZ,
                        quoted_handler + ' /switchversion "%1"',
                    )

    # If the user has manually selected something other than our extension, we need to delete it. Explorer explicitly disables set access on that keys in that folder, but we can delete the whole thing.
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FileExts\\.uproject",
        )
        with closing(key):
            winreg.DeleteKey(key, "UserChoice")
    except OSError:
        pass  # key was not there


def register_engine(engine_path):
    # read the engine registry name from the build_info.json file
    import json

    with open(os.path.join(engine_path, "build_info.json")) as f:
        info = json.load(f)
    engine_name = info["engine_id"]

    # now open the registry key for the user
    key = winreg.CreateKey(
        winreg.HKEY_CURRENT_USER, "SOFTWARE\\Epic Games\\Unreal Engine\\Builds"
    )
    with closing(key):
        winreg.SetValue(key, engine_name, winreg.REG_SZ, engine_path)


def register_engine_old(engine_path):
    # we have a special engine registration tool in the engine folder
    tool = os.path.join(engine_path, "build-tools", "register_engine.cmd")
    subprocess.check_call([tool])


def install_prerequisites(engine_path):
    # we have a special engine registration tool in the engine folder
    tool = os.path.join(
        engine_path, "Engine", "Extras", "Redist", "en-us", "UE4PrereqSetup_x64.exe"
    )
    subprocess.check_call([tool, "/quiet"])


def start_editor(engine_path, project_path):
    # find the .uproject file in project_path
    uproject = glob.glob(os.path.join(project_path, "*.uproject"))[0]
    uproject = os.path.abspath(uproject)

    # find the ue executable
    ue = os.path.join(engine_path, "Engine", "Binaries", "Win64", "UnrealEditor.exe")

    # start the editor
    subprocess.check_call([ue, uproject])
