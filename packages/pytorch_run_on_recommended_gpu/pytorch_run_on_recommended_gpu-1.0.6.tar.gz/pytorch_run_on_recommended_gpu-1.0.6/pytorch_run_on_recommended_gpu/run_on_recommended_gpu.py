#!/usr/bin/env python

import sys
import os
import io
import subprocess

import shlex
import argparse
import getpass
import csv
import re
import xml.etree.ElementTree as ET

import paramiko
import socket
from paramiko.ssh_exception import (AuthenticationException,
                                    NoValidConnectionsError, SSHException)
from tabulate import tabulate

OUT_FILEPOSTFIX = "_nvidia-smi_out.xml"
NVIDIA_COMMAND = "nvidia-smi -q -x"
THIS_MACHINE = "this-machine"

class ParentMap():
    def __init__(self, root):
        self.map = {c: p for p in root.iter() for c in p}

    def get_parent(self, node):
        return self.map[node]



def _parse_mem(in_str, parse_to='B'):
    """Returns a float memory value to the given unit specified
        by parse_to arg. If input is invalid 0.0 will be returned.
    """
    regex = re.compile(r"([0-9]+)\s(.*)")

    # https://stackoverflow.com/questions/42865724/python-parse-human-readable-filesizes-into-bytes
    units = {"B": 1, "KB": 10**3, "MB": 10**6, "GB": 10**9, "TB": 10**12, \
                     "KiB": 2**10, "MiB": 2**20, "GiB": 2**30, "TiB": 2**40}

    if regex.search(in_str):
        match = regex.findall(in_str)[0]
        number = match[0]
        unit = match[1]
        return int(float(number)*units[unit]/units[parse_to])

    return 0.0



def _run_command_on_host(host_name, host_username, command, silent=False, verbose=False):
    PORT = 22
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()

    ssh.load_host_keys(os.path.expanduser("~/.ssh/known_hosts"))
    try:
        ssh.connect(host_name, PORT, username=host_username)

        if not silent:
            print(f"Connection to host '{host_name}' successful.")

    except (SSHException, NoValidConnectionsError, AuthenticationException,
            ConnectionRefusedError, socket.gaierror) as err:

        err_msg, hint = "", ""

        if type(err) is SSHException and "No authentication methods available" in str(err):
            err_msg = f"Connection to host '{host_name}' failed."
            hint = f"Did you generate a clientside private/public key?"

        elif type(err) is NoValidConnectionsError:
            err_msg = f"Connection to host '{host_name}' failed. Connection error."

        elif type(err) is AuthenticationException:
            err_msg = "Authentification with key failed."
            hint = f"Did you use the correct host username? " + \
                   f"Try --user option \n"\
                   f"Is your public key present on the host? " + \
                   f"Try 'ssh-copy-id -i ~/.ssh/<key_id> <username>@{host_name}"

        elif type(err) is socket.gaierror:
            err_msg = f"Connection to host '{host_name}' failed."
            hint = "Check hostname."


        if verbose:
            print(f"{err_msg} {hint} \n({err})")

        elif not silent:
            print(f"{err_msg} {hint}")

        return "", err


    _, stdout, stderr = ssh.exec_command(command)
    (stdout, stderr) = (stdout.read(), stderr.read())
    ssh.close()

    return stdout, stderr



def _get_remotes_nvidiasmi_xml(host_list, user, verbose=False) -> list:

    parsed_hosts = []
    for host in host_list:

        (stdout, stderr) = _run_command_on_host(host, user, NVIDIA_COMMAND, \
            silent=False, verbose=verbose)

        if len(stdout) > 0 and len(stderr) == 0:
            xml_root = ET.parse(io.StringIO(stdout.decode('utf-8'))).getroot()
            host_name = ET.SubElement(xml_root, 'host_name')
            host_name.text = host
            user_name = ET.SubElement(xml_root, 'user_name')
            user_name.text = user
            parsed_hosts.append(xml_root)

    return parsed_hosts



def _get_nvidiasmi_xml():

    parsed_this_machine = None
    sub = subprocess.Popen(NVIDIA_COMMAND, \
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = sub.communicate()

    if len(stdout) > 0 and len(stderr) == 0:
        xml_root = ET.parse(io.StringIO(stdout.decode('utf-8'))).getroot()
        host_name = ET.SubElement(xml_root, 'host_name')
        host_name.text = THIS_MACHINE
        user_name = ET.SubElement(xml_root, 'user_name')
        user_name.text = getpass.getuser()
        parsed_this_machine = xml_root

    return parsed_this_machine



def _get_user_from_pid(pid, host_name=THIS_MACHINE, host_user=getpass.getuser()):
    WINDOWS_COMMAND_CHAIN = ["tasklist", "/v", "/fo", "csv", "/fi", "PID eq "+pid]
    UNIX_COMMAND_CHAIN = ["ps", "-o", "user=", "-p", pid]

    def postprocess(output, os_name):
        output = output.decode("utf-8")
        if os_name == 'nt':
            reader = csv.DictReader(output.splitlines())
            return next(reader)["User Name"].strip()
        else:
            return output.strip()

    if host_name!=THIS_MACHINE:
        get_output = lambda host_name, cmd_chain: \
            _run_command_on_host(host_name, host_user," ".join(cmd_chain), silent=True)[0]

        # We need to read from remote. Try windows
        if res:= get_output(host_name, WINDOWS_COMMAND_CHAIN):
            return postprocess(res, 'nt')
        elif res:= get_output(host_name, UNIX_COMMAND_CHAIN):
            return postprocess(res, 'posix')

    elif os.name == 'nt':
        try:
            if res:= subprocess.check_output(WINDOWS_COMMAND_CHAIN):
                return postprocess(res, 'nt')
        except Exception:
            pass
    elif os.name == 'posix':
        try:
            if res:= subprocess.check_output(UNIX_COMMAND_CHAIN):
                return postprocess(res, 'posix')
        except Exception:
            pass
    return f"<pid={pid}>"





def _get_gpu_stats(xml_root):
    stats = []

    percent_re = re.compile(r"[0-9]{1,3}")
    attached_gpus = int(xml_root.find("./attached_gpus").text)
    host_name = xml_root.find("./host_name").text

    cuda_ver = xml_root.find("./cuda_version")
    cuda_ver = "" if cuda_ver is None else cuda_ver.text
    driver_ver = xml_root.find("./driver_version")
    driver_ver = "" if driver_ver is None else driver_ver.text

    for gpu_node in xml_root.findall("./gpu"):
        gpu_info = {}
        gpu_id = gpu_node.find("./minor_number").text

        if gpu_id == "N/A" and attached_gpus == 1:
            gpu_id = 0
        else:
            gpu_id = int(gpu_id)

        gpu_info['gpu_id'] = gpu_id
        gpu_info['card_name'] = gpu_node.find("./product_name").text
        gpu_info['host_name'] = host_name
        gpu_info['cuda_version'] = cuda_ver
        gpu_info['driver_version'] = driver_ver

        # Add util keys to dict and convert percentage string to integer
        util_node = gpu_node.find("./utilization")
        util_dict = {elem.tag:int(percent_re.match(elem.text)[0]) for elem in util_node}
        gpu_info.update(util_dict)

        fb_mem_node = gpu_node.find("./fb_memory_usage")
        mem_dict = {'fb_mem_'+elem.tag:_parse_mem(elem.text, 'MiB') for elem in fb_mem_node}
        gpu_info.update(mem_dict)

        # Get processes
        gpu_info['processes'] = _get_processes_info(xml_root, gpu_id)
        # Add host name as well

        stats.append(gpu_info)

    return stats



def _get_processes_info(xml_root, gpu_id):
    all_processes_info = []

    xml_parent_map = ParentMap(xml_root)

    host_name = xml_root.find("./host_name").text
    user_name = xml_root.find("./user_name").text

    for p_info_node in xml_root.findall("./gpu/processes/process_info"):
        p_info = {}

        gpu = xml_parent_map.get_parent(xml_parent_map.get_parent(p_info_node))
        current_gpu_id = int(gpu.find("./minor_number").text)

        if current_gpu_id == gpu_id:
            pid = p_info_node.find("./pid")
            used_mem = p_info_node.find("./used_memory")
            p_info['process_name'] = p_info_node.find("./process_name").text
            p_info['pid'] = pid
            p_info['used_mem'] = _parse_mem(used_mem.text, "MiB")

            p_info['user'] = _get_user_from_pid(pid.text, host_name, user_name)

            all_processes_info.append(p_info)

    return all_processes_info



def _print_processes(gpu_info):
    print("### Running processes ###")

    for process in gpu_info['processes']:
        print(f"GPU-ID: {gpu_info['gpu_info']}\tuser: {process['user']:10}\tmemory: {process['used_mem']:6} MiB\tprocess: {process['name']}")
    print()


def _print_gpu_stats(stats, gpu_util_max, print_host_name=False, print_headers=True):
    table = []
    for gpu_info in stats:
        gpu_id = gpu_info['gpu_id']

        gpu_util = gpu_info['gpu_util']
        # Get all users with processes on current gpu_id
        users = {process["user"] for process in gpu_info['processes']}

        parsed_util = f"{gpu_util:3} %" if gpu_util <= gpu_util_max else f"! {gpu_util} %"
        table_entry = [gpu_id,
                       gpu_info['card_name'],
                       parsed_util,
                       f"{gpu_info['fb_mem_free']:6} MiB",
                       f"{gpu_info['cuda_version']} ({gpu_info['driver_version']})",
                       ', '.join(users)
        ]
        if print_host_name:
            table_entry = [gpu_info['host_name']] + table_entry

        table.append(table_entry)


    headers = ["Host", "ID", "Card name", "Util", "Mem free", "Cuda", "User(s)"]
    colalign = ['left', 'right', 'left', 'right', 'right', 'left', 'left']

    if not print_host_name:
        headers = headers[1:]
        colalign = colalign[1:]

    if not print_headers:
        headers = []

    print(tabulate(table, headers=headers, colalign=colalign, ))



def _sort_and_print_machine_stats(all_xml_roots, gpu_util_max, print_host_name=False):

    unsorted_stats = []
    # Get stats and sort least gpu usage and max memory free = first
    for xml_root in all_xml_roots:
        unsorted_stats = unsorted_stats + _get_gpu_stats(xml_root)

    sorted_stats = sorted(unsorted_stats, key=lambda d: (d['gpu_util'], -d['fb_mem_free']))

    _print_gpu_stats(sorted_stats, gpu_util_max, print_host_name, True)

    return sorted_stats



def _parse_select_str(select_str, ordered_gpu_ids):
        sel_ids = []

        if not select_str:
            return [-1]

        def get_star_count(select_str):
            return len([char for char in select_str if char == '*'])

        if get_star_count(select_str) == len(select_str.replace(' ', '')):
            # Select string does only contain stars

            # Pick first n indices from ordered list
            sel_ids = ordered_gpu_ids[:get_star_count(select_str)]
            return sel_ids

        else:
            # We got a more complicated string

            try:
                # Id string with '-' indicates exclusion
                deselected_ids = [abs(int(neg)) for neg in select_str.split() if '-' in neg]
                all_valid_ids = [idd for idd in ordered_gpu_ids if idd not in deselected_ids]

                # Get ids selected by stars and any numeric ids (even negative ones, these are filtered in the next step)
                starred_sel_ids = all_valid_ids[:get_star_count(select_str)]
                any_numeric_ids = [int(idd) for idd in select_str.replace('*', '').split() if int(idd) >= 0]

                # Now only list unique ids which are actually available in gpu list and not explicitly excluded
                sel_ids = [idd for idd in set(starred_sel_ids + any_numeric_ids) if idd in all_valid_ids]

                # If input is not numeric int conversion above could raise a value error
                if not sel_ids:
                     raise ValueError

            except ValueError:
                print("Input must be '*' character(s), GPU ids in range of shown list or empty.")

        return sel_ids



def select_cuda_ids(xml_root, gpu_util_max, select_str="select_interactively", force_usage=False):
    """Return list of recommended cuda gpu indices.

    Args:
        select:
            "select_interactively"
            "****" -> top four gpus
            "1 5 6" -> by minor id
            "" -> disable cuda at all
            "*** -4" -> disable id 4

    """

    if select_str == "":
        # Disable cuda
        return [-1]

    collect_input_here = (select_str == 'select_interactively')

    print(f"\n### Recommended gpus on this machine (descending order) ###")
    sorted_stats = _sort_and_print_machine_stats([xml_root], gpu_util_max, print_host_name=False)

    free_gpu_ids = [gpu_info['gpu_id'] for gpu_info in sorted_stats if gpu_info['gpu_util'] <= gpu_util_max]
    ordered_ids = [gpu_info['gpu_id'] for gpu_info in sorted_stats]

    if not collect_input_here:
        # Autoselecting TOP ({select}) GPUs.
        sel_ids = _parse_select_str(select_str, ordered_ids)

    else:
        # No select value was given. Let the user select top N value via user input.
        input_valid = False

        # Get user input and validate
        while not input_valid:
            select_str = input("\nWhich GPUs shall be used? Give stars or ids. Input=")
            sel_ids = _parse_select_str(select_str.strip(), ordered_ids)
            if sel_ids:
                input_valid = True

        if sel_ids == [-1]:
            # Return immediately if no cuda should be used
            return sel_ids

    # Now check if any gpus need to be forced:
    forcable_selected = [idd for idd in sel_ids if idd not in free_gpu_ids]
    free_selected = [idd for idd in sel_ids if idd in free_gpu_ids]

    if forcable_selected and force_usage == False:
        if not collect_input_here:
            print(f"\nGPU id(s) ({','.join([str(sel) for sel in forcable_selected])}) has/have more than " + \
                f"{gpu_util_max}% gpu utilization but forcing is not enabled. " + \
                f"Run again with 'force = True'.")
            sys.exit(0)

        elif forcable_selected and force_usage == False:
            # User passed an top index which should not be used due to gpu utilization limit.

            # Get indices that need to be forced (utilization > max_utilization)

            inp = input(f"Id(s) {','.join([str(sel) for sel in forcable_selected])} has/have more than " + \
                f"{gpu_util_max}% gpu utilization. To force usage type '--force': ")
            force_usage = (inp == "--force")

    if force_usage:
        # Now get all ids of gpus even if they have high utilization
        ids = free_selected + forcable_selected
    else:
        # Only get ids for gpus with utilization <= max_utilization
        ids = free_selected

    return ids if ids else [-1]



def get_cuda_environ_vars(select="*", gpu_util_max=60, force=False):
    """Return recommended environment variable as dict

        Call 'os.environ.update(returned_vars)' to use those vars.

        Args:
            select (str): The top N GPUs will be selected. If N=0 all GPUs will be disabled.
            gpu_util_max (int): Specify max GPU utilization. GPUs above that limit are
                classified as non-recommended.
            force (bool): Use GPUs even if GPU utilization is above limit.
    """

    machine_xml = _get_nvidiasmi_xml()

    if isinstance(select, list):
        select = ' '.join(select)

    if machine_xml:
        used_cuda_ids = select_cuda_ids(machine_xml, gpu_util_max=gpu_util_max, \
            select_str=select, force_usage=force)
    else:
        used_cuda_ids = [-1]
        print("Could not read nvidia-smi on this machine.")

    table = []
    if not used_cuda_ids == [-1]:
        gpu_info = _get_gpu_stats(machine_xml)
        for idx, cuda_id in enumerate(used_cuda_ids):
            entry = next(filter(lambda inf: cuda_id == inf['gpu_id'], gpu_info))
            table.append(
                [cuda_id, entry['card_name'] ,"->", f"cuda:{idx}"]
            )

        print("\nWill apply following mapping")
        print('\n' + tabulate(table, headers=["ID", "Card name", "", "torch"]))

    else:
        print("\nNo CUDA GPU will be mapped, using CPU only.")

    used_cuda_ids = ','.join([str(inte) for inte in used_cuda_ids])

    return {"CUDA_DEVICE_ORDER": "PCI_BUS_ID",
            "CUDA_VISIBLE_DEVICES": used_cuda_ids}



def main():
    parser = argparse.ArgumentParser(description='Run script file with CUDA device selection based on gpu and memory utilization.')
    parser.add_argument('--command', type=str, default="", help="Command to run")
    parser.add_argument('--script', type=str, default="", help="Path to script.py")
    parser.add_argument("--select", type=str, default="select_interactively", nargs='+', help="Sets value for gpus to be selected and runs without additional user input.")
    parser.add_argument("--gpu-util-max", type=int, default=60, help="Set max allowed gpu utilization to filter gpus.")
    parser.add_argument("--force", action='store_true', help="Force selection of gpus even if gpu utilization is too high.")
    parser.add_argument("--dry", action='store_true', help="Only show outputs and disable script execution for testing.")
    parser.add_argument("--verbose", action='store_true', help="Print verbose info.")

    args = parser.parse_args()

    if args.dry:
        pass
    elif args.command:
        print(f"\nWill run command '{args.command}'.")
        command_chain = shlex.split(args.command)

    elif args.script:
        if os.path.exists(args.script):
            # Do not raise exception in dry mode.
            raise Exception(f"Script is not present: '{args.script}'.")
        else:
            print(f"\nWill run python script '{args.script}'.")
            script_file = os.path.abspath(args.script)
            command_chain = ['python', script_file]

    env_vars = get_cuda_environ_vars(select=args.select,
                                     gpu_util_max=args.gpu_util_max,
                                     force=args.force)


    var_str = str(env_vars) if args.verbose else 'vars'
    print()
    print(f"Adding {var_str} to os.environ.")
    os.environ.update(env_vars)

    if not args.dry and args.command:
        subprocess.run(command_chain)
    elif not args.dry and args.script:
        subprocess.run(command_chain, cwd=os.path.dirname(args.script))
    else:
        if args.command:
            print(f"\nWould run command '{args.command}' but --dry switch is set.")
        elif args.script:
            print(f"\nWould run script '{args.script}' but --dry switch is set.")
        else:
            print()
            print("Neither --command or --script is set. Aborting.")



if __name__ == "__main__":
    main()