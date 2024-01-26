import json
import multiprocessing
import os
import sys
from copy import deepcopy
from subprocess import Popen

import networkx as nx
import sax
import websockets.sync.server

NETLIST = {}
SCHEMEDIT_SERVER_PROCESS = None
SCHEMEDIT_WEBSOCKET_THREAD = None
CACHE_DIR = ".saxviz"
CACHE_KEY = "netlist"


def set_netlist(netlist, models):
    global NETLIST
    patched_netlist = patch_netlist(netlist, models)
    NETLIST = patched_netlist


def patch_netlist(netlist, models):
    patched_netlist = deepcopy(netlist)
    patched_netlist["pdk"] = ""
    patched_netlist["routes"] = {}
    patched_netlist["placements"] = {}
    patched_netlist["info"] = {}
    patched_netlist["info"]["schematic"] = {}
    patched_netlist["info"]["schematic"]["implicit_connections"] = {}
    patched_netlist["info"]["schematic"]["component_ports"] = {
        k: sax.get_ports(v) for k, v in models.items()
    }

    graph = nx.Graph()
    edges = {
        *[
            (k.split(",")[0], v.split(",")[0])
            for k, v in patched_netlist["connections"].items()
        ],
        *[(k, v.split(",")[0]) for k, v in patched_netlist["ports"].items()],
    }
    graph.add_edges_from(edges)
    positions_fn = os.path.join(CACHE_DIR, f"{CACHE_KEY}.json")
    positions = {}
    if os.path.exists(positions_fn):
        positions.update(json.load(open(positions_fn, "r")))
    if not all(k in positions for k in graph.nodes):
        generated_positions = {}
        for k, v in nx.kamada_kawai_layout(graph).items():
            xy = 0.9 * 0.5 * (1.0 + v) + 0.1
            generated_positions[k] = {"x": round(400 * xy[0]), "y": round(400 * xy[1])}
        positions = {**generated_positions, **positions}

    os.makedirs(os.path.join(CACHE_DIR), exist_ok=True)
    json.dump(positions, open(positions_fn, "w"))

    patched_netlist["info"]["schematic"]["placements"] = {
        k: positions[k] for k in netlist["instances"]
    }
    patched_netlist["info"]["schematic"]["port_placements"] = {
        k: positions[k] for k in netlist["ports"]
    }
    return patched_netlist


def start_schemedit_server():
    return Popen(
        [
            sys.executable,
            "-m",
            "http.server",
            "8080",
            "--directory",
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "html"),
        ]
    )


def websocket_handler(websocket):
    while True:
        msg = json.loads(websocket.recv())
        if "Loaded" in msg and msg["Loaded"] is True:
            websocket.send(json.dumps({"Netlist": NETLIST}))
        if "Netlist" in msg:
            netlist = msg["Netlist"]
            positions = {
                **netlist["placements"],
                **netlist["info"]["schematic"]["placements"],
                **netlist["info"]["schematic"]["port_placements"],
            }
            positions_fn = os.path.join(CACHE_DIR, f"{CACHE_KEY}.json")
            os.makedirs(os.path.join(CACHE_DIR), exist_ok=True)
            json.dump(positions, open(positions_fn, "w"))


def start_websocket_server():
    with websockets.sync.server.serve(websocket_handler, "localhost", 8765) as server:
        server.serve_forever()


def visualize_netlist(netlist, models, cache_key="netlist"):
    global SCHEMEDIT_SERVER_PROCESS, SCHEMEDIT_WEBSOCKET_THREAD, CACHE_KEY
    from IPython.display import IFrame

    CACHE_KEY = cache_key

    if SCHEMEDIT_SERVER_PROCESS is None:
        SCHEMEDIT_SERVER_PROCESS = start_schemedit_server()

    set_netlist(netlist, models)

    if SCHEMEDIT_WEBSOCKET_THREAD is not None:
        SCHEMEDIT_WEBSOCKET_THREAD.terminate()

    SCHEMEDIT_WEBSOCKET_THREAD = multiprocessing.Process(target=start_websocket_server)
    SCHEMEDIT_WEBSOCKET_THREAD.start()

    return IFrame("http://localhost:8080", "80%", 400)


if __name__ == "__main__":
    netlist: dict = {
        "instances": {
            "lft": "coupler",
            "top": "waveguide",
            "btm": "waveguide",
            "rgt": "coupler",
        },
        "connections": {
            "lft,out0": "btm,in0",
            "btm,out0": "rgt,in0",
            "lft,out1": "top,in0",
            "top,out0": "rgt,in1",
        },
        "ports": {
            "in0": "lft,in0",
            "in1": "lft,in1",
            "out0": "rgt,out0",
            "out1": "rgt,out1",
        },
    }

    models = {
        "coupler": sax.models.coupler,
        "waveguide": sax.models.straight,
    }

    visualize_netlist(netlist, models)
