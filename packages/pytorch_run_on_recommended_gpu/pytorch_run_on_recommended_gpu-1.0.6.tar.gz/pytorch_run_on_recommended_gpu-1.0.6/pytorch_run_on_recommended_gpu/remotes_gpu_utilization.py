#!/usr/bin/env python

import argparse
import getpass
from . import run_on_recommended_gpu



def main():
    parser = argparse.ArgumentParser(description='Show CUDA utilization of remote hosts.')
    parser.add_argument('hosts', nargs='+', help="List of ssh hosts for remote queries.")
    parser.add_argument("--user", type=str, default=getpass.getuser(), help="User for remote access. Defaults to current user.")
    parser.add_argument("--gpu-util-max", type=int, default=60, help="Set max allowed gpu utilization to filter gpus.")
    parser.add_argument("--verbose", action='store_true', help="Print verbose info.")

    args = parser.parse_args()

    all_hosts_xmls = run_on_recommended_gpu._get_remotes_nvidiasmi_xml(host_list=args.hosts, user=args.user, verbose=args.verbose)
    if all_hosts_xmls:
        print(f"\n### GPU stats of remote hosts (descending order) ###")
        run_on_recommended_gpu._sort_and_print_machine_stats(all_hosts_xmls, args.gpu_util_max, print_host_name=True)
        print('\n')



if __name__ == "__main__":
    main()
