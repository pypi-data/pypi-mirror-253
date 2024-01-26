
'''
The tests in this file are samples drawn from
https://lwn.net/Articles/806002/.
'''

import pytest

from xbc import loads_xbc

def test_01():
    'Key/value example.'
    i = '''feature.option.foo = 1
feature.option.bar = 2'''
    d = {
        'feature.option': False,
        'feature': False,
        'feature.option.foo': '1',
        'feature.option.bar': '2'
    }
    assert loads_xbc(i) == d

def test_02():
    'Block example.'
    i = '''feature.option {
    foo = 1
    bar = 2
}'''
    d = {
        'feature.option': False,
        'feature': False,
        'feature.option.foo': '1',
        'feature.option.bar': '2'
    }
    assert loads_xbc(i) == d

def test_03():
    'Array example.'
    i = 'feature.options = "foo", "bar"'
    d = {
        'feature': False,
        'feature.options': ['foo', 'bar']
    }
    assert loads_xbc(i) == d

def test_10():
    'Compact example.'
    i = 'feature.option{foo=1;bar=2}'
    d = {
        'feature.option': False,
        'feature': False,
        'feature.option.foo': '1',
        'feature.option.bar': '2'
    }
    assert loads_xbc(i) == d

def test_11():
    'Example of a possible configuration.'
    i = '''ftrace.event {
    task.task_newtask {
        filter = "pid < 128"
        enable
    }
    kprobes.vfs_read {
        probes = "vfs_read $arg1 $arg2"
        filter = "common_pid < 200"
        enable
    }
    synthetic.initcall_latency {
        fields = "unsigned long func", "u64 lat"
        actions = "hist:keys=func.sym,lat:vals=lat:sort=lat"
    }
    initcall.initcall_start {
        actions = "hist:keys=func:ts0=common_timestamp.usecs"
    }
    initcall.initcall_finish {
        actions = "hist:keys=func:lat=common_timestamp.usecs-$ts0:onmatch(initcall.initcall_start).initcall_latency(func,$lat)"
    }
}'''
    d = {
        'ftrace': False,
        'ftrace.event': False,
        'ftrace.event.task': False,
        'ftrace.event.task.task_newtask': False,
        'ftrace.event.task.task_newtask.filter': "pid < 128",
        'ftrace.event.task.task_newtask.enable': True,
        'ftrace.event.kprobes': False,
        'ftrace.event.kprobes.vfs_read': False,
        'ftrace.event.kprobes.vfs_read.probes': "vfs_read $arg1 $arg2",
        'ftrace.event.kprobes.vfs_read.filter': "common_pid < 200",
        'ftrace.event.kprobes.vfs_read.enable': True,
        'ftrace.event.synthetic': False,
        'ftrace.event.synthetic.initcall_latency': False,
        'ftrace.event.synthetic.initcall_latency.fields': ["unsigned long func", "u64 lat"],
        'ftrace.event.synthetic.initcall_latency.actions':
        "hist:keys=func.sym,lat:vals=lat:sort=lat",
        'ftrace.event.initcall': False,
        'ftrace.event.initcall.initcall_start': False,
        'ftrace.event.initcall.initcall_start.actions':
        "hist:keys=func:ts0=common_timestamp.usecs",
        'ftrace.event.initcall.initcall_finish': False,
        'ftrace.event.initcall.initcall_finish.actions':
        "hist:keys=func:lat=common_timestamp.usecs-$ts0:onmatch(" +
        "initcall.initcall_start).initcall_latency(func,$lat)"
    }
    assert loads_xbc(i) == d

def test_12():
    'Another example of a possible configuration.'
    i = '''ftrace.event.synthetic.initcall_latency {
    fields = "unsigned long func", "u64 lat"
    hist {
        from {
            event = initcall.initcall_start
            key = func
            assigns = "ts0=common_timestamp.usecs"
        }
        to {
            event = initcall.initcall_finish
            key = func
            assigns = "lat=common_timestamp.usecs-$ts0"
            onmatch = func, $lat
        }
        keys = func.sym, lat
        vals = lat
        sort = lat
    }
}'''
    d = {
        'ftrace': False,
        'ftrace.event': False,
        'ftrace.event.synthetic': False,
        'ftrace.event.synthetic.initcall_latency': False,
        'ftrace.event.synthetic.initcall_latency.fields': ["unsigned long func", "u64 lat"],
        'ftrace.event.synthetic.initcall_latency.hist': False,
        'ftrace.event.synthetic.initcall_latency.hist.from': False,
        'ftrace.event.synthetic.initcall_latency.hist.from.event': 'initcall.initcall_start',
        'ftrace.event.synthetic.initcall_latency.hist.from.key': 'func',
        'ftrace.event.synthetic.initcall_latency.hist.from.assigns': "ts0=common_timestamp.usecs",
        'ftrace.event.synthetic.initcall_latency.hist.to': False,
        'ftrace.event.synthetic.initcall_latency.hist.to.event': 'initcall.initcall_finish',
        'ftrace.event.synthetic.initcall_latency.hist.to.key': 'func',
        'ftrace.event.synthetic.initcall_latency.hist.to.assigns':
        "lat=common_timestamp.usecs-$ts0",
        'ftrace.event.synthetic.initcall_latency.hist.to.onmatch': ['func', '$lat'],
        'ftrace.event.synthetic.initcall_latency.hist.keys': ['func.sym', 'lat'],
        'ftrace.event.synthetic.initcall_latency.hist.vals': 'lat',
        'ftrace.event.synthetic.initcall_latency.hist.sort': 'lat'
    }
    assert loads_xbc(i) == d
