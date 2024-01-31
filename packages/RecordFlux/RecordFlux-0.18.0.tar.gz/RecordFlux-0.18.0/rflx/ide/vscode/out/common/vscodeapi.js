"use strict";
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
Object.defineProperty(exports, "__esModule", { value: true });
exports.getWorkspaceFolder = exports.getWorkspaceFolders = exports.isVirtualWorkspace = exports.onDidChangeConfiguration = exports.registerCommand = exports.getConfiguration = exports.createOutputChannel = void 0;
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable @typescript-eslint/no-explicit-any */
const vscode_1 = require("vscode");
function createOutputChannel(name) {
    return vscode_1.window.createOutputChannel(name, { log: true });
}
exports.createOutputChannel = createOutputChannel;
function getConfiguration(config, scope) {
    return vscode_1.workspace.getConfiguration(config, scope);
}
exports.getConfiguration = getConfiguration;
function registerCommand(command, callback, thisArg) {
    return vscode_1.commands.registerCommand(command, callback, thisArg);
}
exports.registerCommand = registerCommand;
exports.onDidChangeConfiguration = vscode_1.workspace.onDidChangeConfiguration;
function isVirtualWorkspace() {
    const isVirtual = vscode_1.workspace.workspaceFolders &&
        vscode_1.workspace.workspaceFolders.every((f) => f.uri.scheme !== "file");
    return !!isVirtual;
}
exports.isVirtualWorkspace = isVirtualWorkspace;
function getWorkspaceFolders() {
    var _a;
    return (_a = vscode_1.workspace.workspaceFolders) !== null && _a !== void 0 ? _a : [];
}
exports.getWorkspaceFolders = getWorkspaceFolders;
function getWorkspaceFolder(uri) {
    return vscode_1.workspace.getWorkspaceFolder(uri);
}
exports.getWorkspaceFolder = getWorkspaceFolder;
//# sourceMappingURL=vscodeapi.js.map