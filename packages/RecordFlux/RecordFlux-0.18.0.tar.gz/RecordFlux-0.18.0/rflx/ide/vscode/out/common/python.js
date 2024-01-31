"use strict";
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
Object.defineProperty(exports, "__esModule", { value: true });
exports.checkVersion = exports.runPythonExtensionCommand = exports.getDebuggerPath = exports.getInterpreterDetails = exports.resolveInterpreter = exports.initializePython = exports.onDidChangePythonInterpreter = void 0;
/* eslint-disable @typescript-eslint/naming-convention */
const vscode_1 = require("vscode");
const logging_1 = require("./log/logging");
const onDidChangePythonInterpreterEvent = new vscode_1.EventEmitter();
exports.onDidChangePythonInterpreter = onDidChangePythonInterpreterEvent.event;
async function activateExtension() {
    const extension = vscode_1.extensions.getExtension("ms-python.python");
    if (extension) {
        if (!extension.isActive) {
            await extension.activate();
        }
    }
    return extension;
}
async function getPythonExtensionAPI() {
    const extension = await activateExtension();
    return extension === null || extension === void 0 ? void 0 : extension.exports;
}
async function initializePython(disposables) {
    try {
        const api = await getPythonExtensionAPI();
        if (api) {
            disposables.push(api.environments.onDidChangeActiveEnvironmentPath((e) => {
                var _a;
                onDidChangePythonInterpreterEvent.fire({
                    path: [e.path],
                    resource: (_a = e.resource) === null || _a === void 0 ? void 0 : _a.uri,
                });
            }));
            (0, logging_1.traceLog)("Waiting for interpreter from python extension.");
            onDidChangePythonInterpreterEvent.fire(await getInterpreterDetails());
        }
    }
    catch (error) {
        (0, logging_1.traceError)("Error initializing python: ", error);
    }
}
exports.initializePython = initializePython;
async function resolveInterpreter(interpreter) {
    const api = await getPythonExtensionAPI();
    return api === null || api === void 0 ? void 0 : api.environments.resolveEnvironment(interpreter[0]);
}
exports.resolveInterpreter = resolveInterpreter;
async function getInterpreterDetails(resource) {
    const api = await getPythonExtensionAPI();
    const environment = await (api === null || api === void 0 ? void 0 : api.environments.resolveEnvironment(api === null || api === void 0 ? void 0 : api.environments.getActiveEnvironmentPath(resource)));
    if ((environment === null || environment === void 0 ? void 0 : environment.executable.uri) && checkVersion(environment)) {
        return { path: [environment === null || environment === void 0 ? void 0 : environment.executable.uri.fsPath], resource };
    }
    return { path: undefined, resource };
}
exports.getInterpreterDetails = getInterpreterDetails;
async function getDebuggerPath() {
    const api = await getPythonExtensionAPI();
    return api === null || api === void 0 ? void 0 : api.debug.getDebuggerPackagePath();
}
exports.getDebuggerPath = getDebuggerPath;
async function runPythonExtensionCommand(command, ...rest) {
    await activateExtension();
    return await vscode_1.commands.executeCommand(command, ...rest);
}
exports.runPythonExtensionCommand = runPythonExtensionCommand;
function checkVersion(resolved) {
    var _a;
    const version = resolved === null || resolved === void 0 ? void 0 : resolved.version;
    if ((version === null || version === void 0 ? void 0 : version.major) === 3 && (version === null || version === void 0 ? void 0 : version.minor) >= 8) {
        return true;
    }
    (0, logging_1.traceError)(`Python version ${version === null || version === void 0 ? void 0 : version.major}.${version === null || version === void 0 ? void 0 : version.minor} is not supported.`);
    (0, logging_1.traceError)(`Selected python path: ${(_a = resolved === null || resolved === void 0 ? void 0 : resolved.executable.uri) === null || _a === void 0 ? void 0 : _a.fsPath}`);
    (0, logging_1.traceError)("Supported versions are 3.8 and above.");
    return false;
}
exports.checkVersion = checkVersion;
//# sourceMappingURL=python.js.map