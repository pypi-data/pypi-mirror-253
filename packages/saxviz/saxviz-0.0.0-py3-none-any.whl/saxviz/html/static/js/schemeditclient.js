require.config({ paths: { vs: "node_modules/monaco-editor/min/vs" } });

var editor;
var schemedit_ready = false;
var monaco_ready = false;
var initialized = false;
var schemedit = document.getElementById("schemedit");
require(["vs/editor/editor.main"], function () {
  editor = monaco.editor.create(document.getElementById("monaco"), {
    value: INITIAL_EDITOR_CONTENT,
    language: "yaml",
    minimap: { enabled: false },
    automaticLayout: false,
    scrollBeyondLastLine: false,
  });
  setEditorSize();
});
window.addEventListener("resize", (ev) => {
  setEditorSize();
});

function setEditorSize() {
  let width = document.getElementById("monacoColumn").clientWidth;
  editor.layout({ width: width, height: 0.8 * window.innerHeight });
  let schemedit = document.getElementById("schemedit");
  schemedit.width = width;
  schemedit.height = 0.8 * window.innerHeight;
}

window.addEventListener("message", (ev) => {
  if (typeof ev.data === "string") {
    let data = JSON.parse(ev.data);
    if (data["Loaded"] === true) {
      schemedit_ready = true;
      initialize();
    } else if (data["Netlist"] != undefined) {
      let yaml = jsyaml.dump(data["Netlist"]);
      updateEditor(yaml);
      buildPics(updatePanel);
    } else if (data["NetlistNoReload"] != undefined) {
      let yaml = jsyaml.dump(data["NetlistNoReload"]);
      updateEditor(yaml);
      buildPics(updateGds);
    }
  } else {
    if (ev.data.vscodeScheduleAsyncWork) {
      monaco_ready = true;
      initialize();
    }
  }
});

function initialize() {
  if (!initialized & schemedit_ready & monaco_ready) {
    buildPics(updatePanel);
    let yaml = editor.getValue();
    updatePanel();
    initialized = true;
  }
}
function updatePanel() {
  updateSchematic();
  updateGds();
}

function updateSchematic() {
  var netlist = getNetlist();
  patchNetlistWithPortInfo(netlist, () => {
    patchNetlistWithConnectionInfo(netlist, () => {
      schemedit.contentWindow.postMessage(JSON.stringify({ Netlist: netlist }));
    });
  });
}

function updateGds() {
  schemedit.contentWindow.postMessage(JSON.stringify({ Gds: "pic.gds" }));
}

function getNetlist() {
  let yaml = editor.getValue();
  var netlist = jsyaml.load(yaml);
  return netlist;
}

function updateEditor(content) {
  editor.setValue(content);
}

function patchNetlistWithConnectionInfo(netlist, callback) {
  let pdk = netlist.pdk || "";
  let url = "/connections?pdk=" + pdk + "&name=pic";
  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Assuming the response is JSON
    })
    .then((connections) => {
      netlist.connections = netlist.connections || {};
      netlist.info = netlist.info || {};
      netlist.info.schematic = netlist.info.schematic || {};
      netlist.info.schematic.implicit_connections = {};
      for (let [ip1, ip2] of Object.entries(connections)) {
        if (
          _isImplicitConnection(
            ip1,
            ip2,
            netlist.instances,
            netlist.connections,
          )
        ) {
          netlist.info.schematic.implicit_connections[ip1] = ip2;
        }
      }
      if (callback) {
        callback();
      }
    })
    .catch((error) => {
      console.error("Error during fetch:", error);
    });
}

function patchNetlistWithPortInfo(netlist, callback) {
  if (!netlist.info) {
    netlist.info = {};
  }
  if (!netlist.info.schematic) {
    netlist.info.schematic = {};
  }
  if (!netlist.info.schematic.component_ports) {
    netlist.info.schematic.component_ports = {};
  }
  if (!netlist.info.schematic.placements) {
    netlist.info.schematic.placements = {};
  }
  var components = {};
  for (const key in netlist.instances) {
    components[netlist.instances[key].component] = null;
  }
  for (const component in netlist.info.schematic.component_ports) {
    delete components[component];
  }
  let component_list = [];
  for (const component in components) {
    component_list.push(component);
  }
  if (component_list.length > 0) {
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json(); // Assuming the response is JSON
      })
      .then((data) => {
        for (const key in data) {
          netlist.info.schematic.component_ports[key] = data[key];
        }
        if (callback) {
          callback();
        }
      })
      .catch((error) => {
        console.error("Error during fetch:", error);
      });
  } else {
    if (callback) {
      callback();
    }
  }
}

function buildPics(callback) {
  const netlist = getNetlist();
  const pdk = netlist.pdk;
  let data = {
    yaml_netlist: editor.getValue(),
    pdk: pdk,
  };
  fetch("/build", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Assuming the response is JSON
    })
    .then((data) => {
      if (callback) {
        callback();
      }
    })
    .catch((error) => {
      console.error("Error during fetch:", error);
    });
}

function _isImplicitConnection(ip1, ip2, instances, connections) {
  let [i1, p1] = ip1.split(",", 2);
  let [i2, p2] = ip2.split(",", 2);
  if (instances[i1] === undefined) {
    return false;
  }
  if (instances[i2] === undefined) {
    return false;
  }
  if (connections[ip1] === ip2 || connections[ip2] === ip1) {
    return false;
  }
  return true;
}

document.addEventListener("keydown", function (event) {
  if (event.key === "s" && (event.ctrlKey || event.metaKey)) {
    event.preventDefault();
    updateSchematic();
    buildPics(updatePanel);
  }
});
