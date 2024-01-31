"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = require("vscode");
const server_1 = require("./server");
const graph_1 = require("./graph");
const python_1 = require("./common/python");
const settings_1 = require("./common/settings");
const logging_1 = require("./common/log/logging");
const utilities_1 = require("./common/utilities");
const vscodeapi_1 = require("./common/vscodeapi");
const setup_1 = require("./common/setup");
let client;
async function activate(context) {
    const serverInfo = (0, setup_1.loadServerDefaults)();
    const outputChannel = setupLogging(context, serverInfo);
    (0, logging_1.traceLog)(`Name: ${serverInfo.name}`);
    (0, logging_1.traceLog)(`Module: ${serverInfo.module}`);
    context.subscriptions.push((0, python_1.onDidChangePythonInterpreter)(async () => {
        await runServer(serverInfo, outputChannel);
    }), (0, vscodeapi_1.onDidChangeConfiguration)(async (e) => {
        if ((0, settings_1.checkIfConfigurationChanged)(e, serverInfo.module)) {
            await runServer(serverInfo, outputChannel);
        }
    }), (0, vscodeapi_1.registerCommand)(`${serverInfo.module}.restart`, async () => {
        await runServer(serverInfo, outputChannel);
    }));
    setInterval(() => (0, graph_1.updateMessageGraphs)(), 500);
    setImmediate(async () => {
        const interpreter = (0, settings_1.getInterpreterFromSetting)(serverInfo.module);
        if (interpreter === undefined || interpreter.length === 0) {
            (0, logging_1.traceLog)(`Python extension loading`);
            await (0, python_1.initializePython)(context.subscriptions);
            (0, logging_1.traceLog)(`Python extension loaded`);
        }
        else {
            await runServer(serverInfo, outputChannel);
        }
    });
}
exports.activate = activate;
function deactivate() {
    (0, graph_1.cleanupMessageGraphs)();
    if (!client) {
        return undefined;
    }
    return client.stop();
}
exports.deactivate = deactivate;
function setupLogging(context, serverInfo) {
    const outputChannel = (0, vscodeapi_1.createOutputChannel)(serverInfo.name);
    context.subscriptions.push(outputChannel, (0, logging_1.registerLogger)(outputChannel));
    const changeLogLevel = async (c, g) => {
        const level = (0, utilities_1.getLSClientTraceLevel)(c, g);
        await (client === null || client === void 0 ? void 0 : client.setTrace(level));
    };
    context.subscriptions.push(outputChannel.onDidChangeLogLevel(async (e) => {
        await changeLogLevel(e, vscode.env.logLevel);
    }), vscode.env.onDidChangeLogLevel(async (e) => {
        await changeLogLevel(outputChannel.logLevel, e);
    }));
    return outputChannel;
}
async function runServer(serverInfo, outputChannel) {
    const interpreter = (0, settings_1.getInterpreterFromSetting)(serverInfo.module);
    if (interpreter &&
        interpreter.length > 0 &&
        (0, python_1.checkVersion)(await (0, python_1.resolveInterpreter)(interpreter))) {
        (0, logging_1.traceVerbose)(`Using interpreter from ${serverInfo.module}.interpreter: ${interpreter.join(" ")}`);
    }
    else {
        const interpreterDetails = await (0, python_1.getInterpreterDetails)();
        if (interpreterDetails.path) {
            (0, logging_1.traceVerbose)(`Using interpreter from Python extension: ${interpreterDetails.path.join(" ")}`);
        }
        else {
            (0, logging_1.traceError)("Python interpreter missing:\r\n" +
                "[Option 1] Select python interpreter using the ms-python.python.\r\n" +
                `[Option 2] Set an interpreter using "${serverInfo.module}.interpreter" setting.\r\n` +
                "Please use Python 3.8 or greater.");
            return;
        }
    }
    if (!(await (0, server_1.isServerInstalled)(serverInfo.module))) {
        const projectRoot = await (0, utilities_1.getProjectRoot)();
        const workspaceSetting = await (0, settings_1.getWorkspaceSettings)(serverInfo.module, projectRoot, true);
        const result = await vscode.window.showWarningMessage("RecordFlux language server is not installed in the selected environment", "Install", "Select Environment");
        switch (result) {
            case "Install":
                if (!(await (0, server_1.installServer)(workspaceSetting))) {
                    return await runServer(serverInfo, outputChannel);
                }
                break;
            case "Select Environment":
                await vscode.commands.executeCommand("python.setInterpreter");
                return await runServer(serverInfo, outputChannel);
        }
    }
    client = await (0, server_1.restartServer)(serverInfo.module, serverInfo.name, outputChannel, client);
}
//# sourceMappingURL=extension.js.map