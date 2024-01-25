# PyCUPS CLI
Allows to interact with CUPS in CLI using pycups. This script outputs the data in JSON, which allows to easily parse it in scripts with `jq`. For example getting a list of installed printers and their status is as simple as: `pycupscli printers | jq -r 'keys[] as $k | "\($k): \(.[$k]["printer-state"])"'`.

## Usage
```
pycupscli [check, devices, printers, cancel, remove, add, info, print] -j jobid -p name -u uri -d driver -f file -o opts -a
```

Where subcommands are:

- check: check that the CUPS server is running and accessible, similar to `lpstat -r`
- devices: returns a list of available devices, including network printers, similar to `lpinfo -v`
- printers: returns the list of configured printers, similar to `lpstat -v`
- cancel: cancels one or all jobs for a printer, requires `-u uri` and either `-a` or `-j jobid`
- remove: remove a printer, requires either `-u uri` or `-p name`
- add: add a printer, requires `-u uri`, `-p name` and `-d driver`
- info: returns the attributes of an existing job or printer, requires `-j jobid` or `-p name` or `-u uri`
- print: print a file, requires `-p name` and `-f file`, optionally `-o opts` with options seralized as a json object

The output of the script is just the raw data returned by pycups, serialized as json.
