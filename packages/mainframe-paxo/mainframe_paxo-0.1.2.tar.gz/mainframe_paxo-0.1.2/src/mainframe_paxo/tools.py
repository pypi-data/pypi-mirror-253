import os
import subprocess
import winreg

# different work location

p4_fingerprints = {
    "aws": "7F:24:67:0B:62:7B:9F:3A:ED:5F:26:32:23:82:8F:20:EE:13:8B:03",
    "rvk": "8C:07:9D:29:F8:03:CC:76:C0:3B:26:41:20:3D:4C:B0:F0:A4:5E:B8",
    "rvk-old": "B9:62:8C:DA:75:B7:85:0E:B1:2B:02:1A:AE:11:5B:25:7D:C8:72:CF",
    "hel": "62:95:05:A0:B4:AD:1A:61:12:F6:06:07:9A:D3:5C:83:85:A6:67:C9",
}

locations = {
    "rvk-office": {
        "desc": "Reykjavík office",
        "p4port": "ssl:p4-rvk.mainframe.zone:1666",
        "p4trust": p4_fingerprints["rvk"],
        "ddc": r"\\ddc-rvk.mainframe.zone\DDC",
    },
    "rvk-ext": {
        "desc": "Reykjavík, accessin office from the internet",
        "p4port": "ssl:p4-rvk.x.mainframe.zone:1666",
        "p4trust": p4_fingerprints["rvk"],
        "ddc": None,
    },
    "hel-office": {
        "desc": "Helsinki office",
        "p4port": "ssl:p4-hel.mainframe.zone:1666",
        "p4trust": p4_fingerprints["hel"],
        "ddc": r"\\ddc-hel.mainframe.zone\DDC",
    },
    "hel-ext": {
        "desc": "Helsinki office",
        "p4port": "ssl:p4-hel.x.mainframe.zone:1666",
        "p4trust": p4_fingerprints["hel"],
        "ddc": None,
    },
    "tailscale": {
        "desc": "working over tailscale network, e.g. from home",
        "p4port": "ssl:p4.t.mainframe.zone:1666",
        "p4trust": p4_fingerprints["aws"],
        "ddc": r"\\ddc.t.mainframe.zone\DDC",
    },
    "external": {
        "desc": "working from the internet without VPN",
        "p4port": "ssl:perforce.x.mainframe.zone:1666",
        "p4trust": p4_fingerprints["aws"],
        "ddc": None,
    },
}


# some common environment tools for us


def validate_drivename(drivename, check_exists=True):
    drivename = drivename.upper().strip()
    if not drivename.endswith(":"):
        drivename += ":"
    if not os.path.isdir(os.path.join(drivename, "\\")):
        raise ValueError(f"Drive {drivename} does not exist")
    return drivename


def workdrive_set(drivename):
    drivename = validate_drivename(drivename)
    env_var_set("PD_WORKDRIVE", drivename)


def workdrive_get(empty_ok=False):
    drivename = env_var_get("PD_WORKDRIVE")
    if not drivename and not empty_ok:
        raise ValueError("PD_WORKDRIVE not set.  Did you run initial-setup?")
    return drivename


# work location related stuff
def location_set(location):
    if location not in locations.keys():
        raise ValueError(f"Unknown location {location}")
    env_var_set("PD_LOCATION", location)


def location_get():
    location = env_var_get("PD_LOCATION")
    if not location:
        raise ValueError("PD_LOCATION not set.  Did you run initial-setup?")
    if location not in locations.keys():
        raise ValueError(f"Unknown location {location}")
    return location


# setting and getting environment variables
def env_var_get(name):
    if name in os.environ:
        return os.environ[name]

    # the env var may have been set in a previous session
    # and not yet updated in _out_ environment. so we look
    # in the registry.
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment")
        value, _ = winreg.QueryValueEx(key, name)
        return value
    except FileNotFoundError:
        pass

    # try the system environment
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",
        )
        value, _ = winreg.QueryValueEx(key, name)
        return value
    except FileNotFoundError:
        pass
    return None


def env_var_set(name, value, permanent=True, system=False):
    if permanent:
        cmd = ["setx", name, value]
        if system:
            cmd.append("/m")
        subprocess.run(cmd, check=True, capture_output=True)
    os.environ[name] = value


def env_var_del(name, permanent=True, system=False):
    if not permanent:
        try:
            del os.environ[name]
        except KeyError:
            pass
    if not permanent:
        return

    if system:
        root = winreg.HKEY_LOCAL_MACHINE
        env = "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment"
    else:
        root = winreg.HKEY_CURRENT_USER
        env = "Environment"
    try:
        key = winreg.OpenKey(root, env, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, name)
    except FileNotFoundError:
        pass


def addpath(path, permanent=False, system=False, infront=False):
    if infront:
        path = path + ";" + os.environ["PATH"]
    else:
        path = os.environ["PATH"] + ";" + path
    env_var_set("PATH", path, permanent, system)
