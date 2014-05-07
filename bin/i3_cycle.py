#!/usr/bin/env python

import i3
import json


def get_windows():
    windows = i3.filter(nodes=[], focused=False)
    window_options = []
    for window in windows:
        name = window['name']
        id_ = window['window']
        if id_ is None:
            continue
        if 'i3bar for output' in name:
            continue
        window_options.append(window['id'])
    return window_options


def alt_tab():
    window_options = get_windows()
    i3.focus(con_id=window_options[0])


def get_num(node):
    return node['num']


def get_id(win):
    return win['id']


def get_nodes(nodes):
    return nodes['nodes']


def flatten_lists(lists):
    new_list = []
    for list_ in lists:
        new_list.extend(list_)
    return new_list

def copied_alt_tab():

    num = i3.filter(i3.get_workspaces(), focused=True)[0]['num']
    all_nodes = flatten_lists(list(map(get_nodes, i3.filter())))
    curr = i3.filter(all_nodes, focused=True)[0]
    print(get_id(curr))

    ids = list(map(get_id, all_nodes)) + [get_id(curr)]
    print(ids)

    next_id = ids[(ids.index(curr['id']) + 2) % len(ids)]
    print(next_id)

    i3.focus(con_id=next_id)


def all_windows():
    print(json.dumps(i3.filter(nodes=[], focused=False), indent=4))
    #print(json.dumps(i3.get_workspaces(), indent=4))
    #print(json.dumps(flatten_lists(list(map(get_nodes, i3.filter()))), indent=4))


if __name__ == '__main__':
    alt_tab()
