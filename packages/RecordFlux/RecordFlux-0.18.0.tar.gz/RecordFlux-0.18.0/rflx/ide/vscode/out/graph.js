"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.cleanupMessageGraphs = exports.updateMessageGraphs = void 0;
const path = require("path");
const fs_1 = require("fs");
const vscode_1 = require("vscode");
const constants_1 = require("./common/constants");
let graph_list = [];
const directory = path.join(constants_1.CACHE_DIR, "graphs");
function updateMessageGraphs() {
    (0, fs_1.readdir)(directory, (error, files) => {
        if (error)
            throw error;
        files.forEach((file) => {
            if (file.endsWith(".svg") && !graph_list.includes(file)) {
                createGraphWebView(directory, file);
            }
        });
    });
}
exports.updateMessageGraphs = updateMessageGraphs;
function cleanupMessageGraphs() {
    (0, fs_1.readdir)(directory, (error, files) => {
        if (error)
            throw error;
        files.forEach((file) => {
            if (!file.endsWith(".svg"))
                return;
            (0, fs_1.unlink)(path.join(directory, file), (error) => {
                if (error)
                    throw error;
            });
        });
    });
}
exports.cleanupMessageGraphs = cleanupMessageGraphs;
function createGraphWebView(directory, file) {
    graph_list.push(file);
    const imagePath = path.join(directory, file);
    const imageUri = vscode_1.Uri.file(imagePath);
    const messageName = file.slice(0, -4);
    const panel = vscode_1.window.createWebviewPanel(`${messageName}Graph`, `${messageName} graph`, vscode_1.ViewColumn.Two, {
        localResourceRoots: [vscode_1.Uri.file(directory)],
    });
    panel.webview.html = getWebviewContent(panel.webview.asWebviewUri(imageUri));
    panel.onDidDispose(() => {
        graph_list = graph_list.filter((f) => f != file);
        (0, fs_1.unlink)(imagePath, (error) => {
            if (error)
                throw error;
        });
    });
}
function getWebviewContent(imageSource) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test</title>
</head>
<body>
	<img src="${imageSource}" width="100%" />	
</body>
<style>
body {
	display: flex;
	align-items: center;
	height: 100%;
}
html {
	height: 100%;
}
</style>
</html>`;
}
//# sourceMappingURL=graph.js.map