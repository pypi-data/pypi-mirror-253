# Copyright (C) 2023  The CivRealm project
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
import re
import os
import argparse
import yaml
from importlib_resources import files


def boolean_string(s):
    s = s.lower()
    if s not in {'false', 'true'}:
        raise ValueError(f'{s} is not a valid boolean string')
    return s == 'true'


def load_config(config_file):
    with open(files('civrealm.configs').joinpath(config_file), 'r') as file:
        config = yaml.safe_load(file)
    return config


def parse_args():
    """
    Initialize default arguments with yaml and renew values with input arguments.
    """

    default_config_file = files('civrealm.configs').joinpath(
        'default_settings.yaml')
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', help="configuration file *.yaml", type=str,
                        required=False, default=default_config_file)
    args, remaining_argv = parser.parse_known_args()

    opt = yaml.load(open(args.config_file), Loader=yaml.FullLoader)
    for key in opt.keys():
        # print(opt[key])
        if type(opt[key]) is dict:
            group = parser.add_argument_group(key)
            # print(key)
            for sub_key in opt[key].keys():
                assert type(
                    opt[key][sub_key]) is not dict, "Config only accepts two-level of arguments"
                if type(opt[key][sub_key]) is bool:
                    group.add_argument(
                        '--' + key + '.' + sub_key, default=opt[key][sub_key], type=boolean_string)
                else:
                    group.add_argument(
                        '--' + key + '.' + sub_key, default=opt[key][sub_key],
                        type=type(opt[key][sub_key]))
        else:
            if type(opt[key]) is bool:
                parser.add_argument(
                    '--' + key, default=opt[key], type=boolean_string)
            else:
                parser.add_argument(
                    '--' + key, default=opt[key], type=type(opt[key]))
    args, remaining_argv = parser.parse_known_args(remaining_argv)

    return vars(args)


def parse_fc_web_args(docker_compose_file='docker-compose.yaml'):
    fc_web_args = load_config(docker_compose_file)

    service = fc_args['service']
    image = fc_web_args['services'][service]['image']
    host = fc_web_args['services'][service].get('environment', {}).get('host')
    fc_web_args['container'] = fc_web_args['services'][service]['container_name']

    port_map = {}
    for p_map in fc_web_args['services'][service]['ports']:
        container_port_set, local_port_set = p_map.split(":")
        if "-" in  container_port_set:
            container_start_port, container_end_port = container_port_set.split("-")
            local_start_port, local_end_port = local_port_set.split("-")
            for idx in range(int(container_end_port)-int(container_start_port)+1):
                port_map[int(local_start_port)+idx] = int(container_start_port)+idx
        else:
            port_map[int(local_port_set)] = int(container_port_set)

    server_port = fc_web_args['services'][service]['ports'][0]
    connect_port = int(fc_web_args['services'][service]
                       ['ports'][2].split(":")[1].split("-")[0])

    fc_web_args['tag'] = 'latest'
    fc_web_args['port'] = server_port.split(":")[0]
    fc_web_args['client_port'] = connect_port + 1
    fc_web_args['port_start_index'] = connect_port + 300

    if tag := re.search(r'\:(.*)', image):
        fc_web_args['tag'] = tag[1]
    if host is not None:
        fc_args['host'] = host
    fc_web_args['image'] = image.split('/')[1]
    fc_web_args['port_map'] = port_map
    return fc_web_args


fc_args = parse_args()
fc_web_args = parse_fc_web_args()

# Override server host and port with envirionment variables
# CIVREALM_HOST_URL and CIVREALM_HOST_PORT
if os.environ.get("CIVREALM_HOST_URL"):
    fc_args["host"] = os.environ["CIVREALM_HOST_URL"]
if os.environ.get("CIVREALM_HOST_PORT"):
    fc_web_args["port"] = os.environ["CIVREALM_HOST_PORT"]
