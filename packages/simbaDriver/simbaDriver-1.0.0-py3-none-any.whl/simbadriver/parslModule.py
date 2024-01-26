# BEGIN: Copyright 
# Copyright (C) 2024 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

from parsl.config import Config
from parsl.launchers import SingleNodeLauncher
from parsl.launchers import SrunLauncher
from parsl.channels import LocalChannel
from parsl.providers import SlurmProvider
from parsl.providers import LocalProvider
from parsl.executors import HighThroughputExecutor
from parsl.addresses import address_by_hostname
from parsl.data_provider.globus import GlobusStaging
from parsl.app.app import bash_app

import parsl

from simbadriver.module import Module

@bash_app
def srunCommand(command, config, stdout = 'module.stdout', stderr = 'module.stderr'):
    return command + ' ' + config

class ParslModule(Module):
    def _init(self, data):
        self.launcher = SingleNodeLauncher
        self.launcherData = {
            'debug': True,
            'fail_on_any': False
            }

        if 'launcher' in data:
            if data['launcher']['type'] == 'SrunLauncher':
                self.launcher = SrunLauncher
                self.launcherData = {
                    'debug': True,
                    'overrides': ''
                    }    
                            
                if 'debug' in data['launcher']:
                    self.launcherData['debug'] = data['launcher']['debug']
                if 'overrides' in data['launcher']:
                    self.launcherData['overrides'] = data['launcher']['overrides']
                    
            else:
                if data['launcher']['type'] == 'SingleNodeLauncher':
                    if 'debug' in data['launcher']:
                        self.launcherData['debug'] = data['launcher']['debug']
                    if 'fail_on_any' in data['launcher']:
                        self.launcherData['fail_on_any'] = data['launcher']['fail_on_any']
                else:
                    raise Exception('Unsupported launcher: ' + data['launcher']['type'])
                
        self.provider = LocalProvider
        self.providerData = {
            'channel': LocalChannel(),
            'nodes_per_block': 1,
            'init_blocks': 1 ,
            'min_blocks': 0,
            'max_blocks': 1,
            'parallelism': 1.0,
            'worker_init': '',
            'move_files': True
            }

        if 'provider' in data:
            if data['provider']['type'] == 'SlurmProvider':
                self.provider = SlurmProvider
                self.providerData = {
                    'partition': None,
                    'account': None,
                    'qos': None,
                    'constraint': None,
                    'channel': LocalChannel(),
                    'nodes_per_block': 1,
                    'cores_per_node': None,
                    'mem_per_node': None,
                    'init_blocks': 1 ,
                    'min_blocks': 0,
                    'max_blocks': 1,
                    'parallelism': 1.0,
                    'walltime': '00:10:00',
                    'scheduler_options': '',
                    'regex_job_id': 'Submitted batch job (?P<id>\\S*)',
                    'worker_init': '',
                    'exclusive': True,
                    'move_files': True
                    }
            
                if 'partition' in data['provider']:
                    self.providerData['partition'] = data['provider']['partition']
                if 'account' in data['provider']:
                    self.providerData['account'] = data['provider']['account']
                if 'qos' in data['provider']:
                    self.providerData['qos'] = data['provider']['qos']
                if 'constraint' in data['provider']:
                    self.providerData['constraint'] = data['provider']['constraint']
                if 'channel' in data['provider']:
                    self.providerData['channel'] = data['provider']['channel']
                if 'nodes_per_block' in data['provider']:
                    self.providerData['nodes_per_block'] = data['provider']['nodes_per_block']
                if 'cores_per_node' in data['provider']:
                    self.providerData['cores_per_node'] = data['provider']['cores_per_node']
                if 'mem_per_node' in data['provider']:
                    self.providerData['mem_per_node'] = data['provider']['mem_per_node']
                if 'init_blocks' in data['provider']:
                    self.providerData['init_blocks'] = data['provider']['init_blocks']
                if 'min_blocks' in data['provider']:
                    self.providerData['min_blocks'] = data['provider']['min_blocks']
                if 'max_blocks' in data['provider']:
                    self.providerData['max_blocks'] = data['provider']['max_blocks']
                if 'parallelism' in data['provider']:
                    self.providerData['parallelism'] = data['provider']['parallelism']
                if 'walltime' in data['provider']:
                    self.providerData['walltime'] = data['provider']['walltime']
                if 'scheduler_options' in data['provider']:
                    self.providerData['scheduler_options'] = data['provider']['scheduler_options']
                if 'regex_job_id' in data['provider']:
                    self.providerData['regex_job_id'] = data['provider']['regex_job_id']
                if 'worker_init' in data['provider']:
                    self.providerData['worker_init'] = data['provider']['worker_init']
                if 'exclusive' in data['provider']:
                    self.providerData['exclusive'] = data['provider']['exclusive']
                if 'move_files' in data['provider']:
                    self.providerData['move_files'] = data['provider']['move_files']
            else:
                if data['provider']['type'] == 'LocalProvider':
                    if 'channel' in data['provider']:
                        self.providerData['channel'] = data['provider']['channel']
                    if 'nodes_per_block' in data['provider']:
                        self.providerData['nodes_per_block'] = data['provider']['nodes_per_block']
                    if 'init_blocks' in data['provider']:
                        self.providerData['init_blocks'] = data['provider']['init_blocks']
                    if 'min_blocks' in data['provider']:
                        self.providerData['min_blocks'] = data['provider']['min_blocks']
                    if 'max_blocks' in data['provider']:
                        self.providerData['max_blocks'] = data['provider']['max_blocks']
                    if 'parallelism' in data['provider']:
                        self.providerData['parallelism'] = data['provider']['parallelism']
                    if 'worker_init' in data['provider']:
                        self.providerData['worker_init'] = data['provider']['worker_init']
                    if 'move_files' in data['provider']:
                        self.providerData['move_files'] = data['provider']['move_files']
                else:
                    raise Exception('Unsupported provider: ' + data['provider']['type'])
                        
        self.executor = HighThroughputExecutor
        self.executorData = {
            'label': 'HighThroughputExecutor',
            'launch_cmd': None,
            'address': None,
            'worker_ports': None,
            'worker_port_range': (54000, 55000),
            'interchange_port_range': (55000, 56000),
            'storage_access': None,
            'working_dir': None,
            'worker_debug': False,
            'cores_per_worker': 1.0,
            'mem_per_worker': None,
            'max_workers': float('inf'),
            'cpu_affinity': 'none',
            'available_accelerators': [],
            'prefetch_capacity': 0,
            'heartbeat_threshold': 120,
            'heartbeat_period': 30,
            'poll_period': 10,
            'address_probe_timeout': None,
            'worker_logdir_root': None
            }
        
        if 'executor' in data:
            if data['executor']['type'] != 'HighThroughputExecutor':
                raise Exception('Unsupported executor: ' + data['executor']['type'])
            
            if 'label' in data['executor']:
                self.executorData['label'] = data['executor']['label']
            if 'launch_cmd' in data['executor']:
                self.executorData['launch_cmd'] = data['executor']['launch_cmd']
            if 'address' in data['executor']:
                self.executorData['address'] = data['executor']['address']
            if 'worker_ports' in data['executor']:
                self.executorData['worker_ports'] = data['executor']['worker_ports']
            if 'worker_port_range' in data['executor']:
                self.executorData['worker_port_range'] = (data['executor']['worker_port_range'][0], data['executor']['worker_port_range'][1])
            if 'interchange_port_range' in data['executor']:
                self.executorData['interchange_port_range'] = (data['executor']['interchange_port_range'][0], data['executor']['interchange_port_range'][1])
            if 'storage_access' in data['executor']:
                self.executorData['storage_access'] = data['executor']['storage_access']
            if 'working_dir' in data['executor']:
                self.executorData['working_dir'] = data['executor']['working_dir']
            if 'worker_debug' in data['executor']:
                self.executorData['worker_debug'] = data['executor']['worker_debug']
            if 'cores_per_worker' in data['executor']:
                self.executorData['cores_per_worker'] = data['executor']['cores_per_worker']
            if 'mem_per_worker' in data['executor']:
                self.executorData['mem_per_worker'] = data['executor']['mem_per_worker']
            if 'max_workers' in data['executor']:
                self.executorData['max_workers'] = data['executor']['max_workers']
            if 'cpu_affinity' in data['executor']:
                self.executorData['cpu_affinity'] = data['executor']['cpu_affinity']
            if 'available_accelerators' in data['executor']:
                self.executorData['available_accelerators'] = data['executor']['available_accelerators']
            if 'prefetch_capacity' in data['executor']:
                self.executorData['prefetch_capacity'] = data['executor']['prefetch_capacity']
            if 'heartbeat_threshold' in data['executor']:
                self.executorData['heartbeat_threshold'] = data['executor']['heartbeat_threshold']
            if 'heartbeat_period' in data['executor']:
                self.executorData['heartbeat_period'] = data['executor']['heartbeat_period']
            if 'poll_period' in data['executor']:
                self.executorData['poll_period'] = data['executor']['poll_period']
            if 'address_probe_timeout' in data['executor']:
                self.executorData['address_probe_timeout'] = data['executor']['address_probe_timeout']
            if 'worker_logdir_root' in data['executor']:
                self.executorData['worker_logdir_root'] = data['executor']['worker_logdir_root']

        return

    def execute(self):
        
        parsl.load(Config(executors = [
            self.executor(
                **self.executorData,
                provider =  self.provider(
                    **self.providerData, 
                    launcher = self.launcher(
                        **self.launcherData
                        )
                    )
                )
            ]))
                   
        srunCommand(self.command, str(self.config)).result()
        parsl.clear()
    
    def _start(self, startTick, startTime):
        self.execute()
        return True

        
    def _step(self, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        self.execute()
        return True
        
    def _end(self, lastRunTick, lastRunTime, endTick, endTime):
        self.execute()
        return True
