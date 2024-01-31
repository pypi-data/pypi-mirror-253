"use strict";
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
Object.defineProperty(exports, "__esModule", { value: true });
exports.checkIfConfigurationChanged = exports.getGlobalSettings = exports.getWorkspaceSettings = exports.getInterpreterFromSetting = exports.getExtensionSettings = void 0;
const python_1 = require("./python");
const vscodeapi_1 = require("./vscodeapi");
function getExtensionSettings(namespace, includeInterpreter) {
    return Promise.all((0, vscodeapi_1.getWorkspaceFolders)().map((w) => getWorkspaceSettings(namespace, w, includeInterpreter)));
}
exports.getExtensionSettings = getExtensionSettings;
function resolveVariables(value, workspace) {
    const substitutions = new Map();
    const home = process.env.HOME || process.env.USERPROFILE;
    if (home) {
        substitutions.set("${userHome}", home);
    }
    if (workspace) {
        substitutions.set("${workspaceFolder}", workspace.uri.fsPath);
    }
    substitutions.set("${cwd}", process.cwd());
    (0, vscodeapi_1.getWorkspaceFolders)().forEach((w) => {
        substitutions.set("${workspaceFolder:" + w.name + "}", w.uri.fsPath);
    });
    return value.map((s) => {
        for (const [key, value] of substitutions) {
            s = s.replace(key, value);
        }
        return s;
    });
}
function getInterpreterFromSetting(namespace, scope) {
    const config = (0, vscodeapi_1.getConfiguration)(namespace, scope);
    return config.get("interpreter");
}
exports.getInterpreterFromSetting = getInterpreterFromSetting;
async function getWorkspaceSettings(namespace, workspace, includeInterpreter) {
    var _a, _b, _c, _d, _e, _f;
    const config = (0, vscodeapi_1.getConfiguration)(namespace, workspace.uri);
    let interpreter = [];
    if (includeInterpreter) {
        interpreter = (_a = getInterpreterFromSetting(namespace, workspace)) !== null && _a !== void 0 ? _a : [];
        if (interpreter.length === 0) {
            interpreter =
                (_b = (await (0, python_1.getInterpreterDetails)(workspace.uri)).path) !== null && _b !== void 0 ? _b : [];
        }
    }
    const workspaceSetting = {
        cwd: workspace.uri.fsPath,
        workspace: workspace.uri.toString(),
        args: resolveVariables((_c = config.get(`args`)) !== null && _c !== void 0 ? _c : [], workspace),
        path: resolveVariables((_d = config.get(`path`)) !== null && _d !== void 0 ? _d : [], workspace),
        interpreter: resolveVariables(interpreter, workspace),
        importStrategy: (_e = config.get(`importStrategy`)) !== null && _e !== void 0 ? _e : "fromEnvironment",
        showNotifications: (_f = config.get(`showNotifications`)) !== null && _f !== void 0 ? _f : "off",
    };
    return workspaceSetting;
}
exports.getWorkspaceSettings = getWorkspaceSettings;
function getGlobalValue(config, key, defaultValue) {
    var _a, _b;
    const inspect = config.inspect(key);
    return (_b = (_a = inspect === null || inspect === void 0 ? void 0 : inspect.globalValue) !== null && _a !== void 0 ? _a : inspect === null || inspect === void 0 ? void 0 : inspect.defaultValue) !== null && _b !== void 0 ? _b : defaultValue;
}
async function getGlobalSettings(namespace, includeInterpreter) {
    var _a;
    const config = (0, vscodeapi_1.getConfiguration)(namespace);
    let interpreter = [];
    if (includeInterpreter) {
        interpreter = getGlobalValue(config, "interpreter", []);
        if (interpreter === undefined || interpreter.length === 0) {
            interpreter = (_a = (await (0, python_1.getInterpreterDetails)()).path) !== null && _a !== void 0 ? _a : [];
        }
    }
    const setting = {
        cwd: process.cwd(),
        workspace: process.cwd(),
        args: getGlobalValue(config, "args", []),
        path: getGlobalValue(config, "path", []),
        interpreter: interpreter,
        importStrategy: getGlobalValue(config, "importStrategy", "fromEnvironment"),
        showNotifications: getGlobalValue(config, "showNotifications", "off"),
    };
    return setting;
}
exports.getGlobalSettings = getGlobalSettings;
function checkIfConfigurationChanged(e, namespace) {
    const settings = [
        `${namespace}.args`,
        `${namespace}.path`,
        `${namespace}.interpreter`,
        `${namespace}.importStrategy`,
        `${namespace}.showNotifications`,
    ];
    const changed = settings.map((s) => e.affectsConfiguration(s));
    return changed.includes(true);
}
exports.checkIfConfigurationChanged = checkIfConfigurationChanged;
//# sourceMappingURL=settings.js.map