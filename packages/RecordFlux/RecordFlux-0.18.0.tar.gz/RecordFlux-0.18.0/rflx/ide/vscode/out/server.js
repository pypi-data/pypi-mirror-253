"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.restartServer = exports.isServerInstalled = exports.installServer = void 0;
const child_process_1 = require("child_process");
const path = require("path");
const fsapi = require("fs-extra");
const vscode_1 = require("vscode");
const vscode_languageclient_1 = require("vscode-languageclient");
const node_1 = require("vscode-languageclient/node");
const constants_1 = require("./common/constants");
const logging_1 = require("./common/log/logging");
const settings_1 = require("./common/settings");
const utilities_1 = require("./common/utilities");
const vscodeapi_1 = require("./common/vscodeapi");
async function installServer(workspaceSetting) {
    const installLogFile = "install.log";
    const installLogPath = path.join(constants_1.CACHE_DIR, installLogFile);
    const truncateString = (string = "", maxLength) => {
        return string.length > maxLength
            ? `${string.substring(0, maxLength)}…`
            : string;
    };
    await fsapi.remove(installLogPath);
    await fsapi.createFile(installLogPath);
    return await vscode_1.window.withProgress({
        location: vscode_1.ProgressLocation.Notification,
        title: "RecordFlux language server installation ([details](" +
            vscode_1.Uri.file(installLogPath) +
            "))",
        cancellable: true,
    }, (progress, token) => {
        const promise = new Promise((resolve) => {
            const logging = fsapi.createWriteStream(installLogPath, {
                flags: "a",
            });
            const process = (0, child_process_1.spawn)(workspaceSetting.interpreter[0], [
                "-m",
                "pip",
                "install",
                "RecordFlux",
            ]);
            process.stdout.pipe(logging);
            process.stderr.pipe(logging);
            process.stdout.on("data", (data) => progress.report({
                message: truncateString(`${data}`, 70),
            }));
            process.on("close", async (code, _signal) => {
                if (code == 0) {
                    resolve(true);
                    return;
                }
                vscode_1.window.showErrorMessage("Failed to install the server ([details](" +
                    vscode_1.Uri.file(installLogPath) +
                    "))\n");
                resolve(false);
            });
            token.onCancellationRequested((_e) => process.kill());
        });
        return promise;
    });
}
exports.installServer = installServer;
async function isServerInstalled(serverId) {
    const projectRoot = await (0, utilities_1.getProjectRoot)();
    const workspaceSetting = await (0, settings_1.getWorkspaceSettings)(serverId, projectRoot, true);
    try {
        (0, child_process_1.execSync)(`${workspaceSetting.interpreter[0]} -m rflx --version`);
    }
    catch (_error) {
        return false;
    }
    return true;
}
exports.isServerInstalled = isServerInstalled;
async function createServer(settings, serverId, serverName, outputChannel, initializationOptions) {
    const command = settings.interpreter[0];
    const cwd = settings.cwd;
    const newEnv = { ...process.env };
    newEnv.USE_DEBUGPY = "False";
    newEnv.LS_IMPORT_STRATEGY = settings.importStrategy;
    newEnv.LS_SHOW_NOTIFICATION = settings.showNotifications;
    const args = settings.interpreter.slice(1).concat(["-m", "rflx", "run_ls"]);
    (0, logging_1.traceInfo)(`Server run command: ${[command, ...args].join(" ")}`);
    const serverOptions = {
        command,
        args,
        options: { cwd, env: newEnv },
    };
    const clientOptions = {
        // Register the server for recordflux documents
        documentSelector: (0, vscodeapi_1.isVirtualWorkspace)()
            ? [{ language: "recordflux" }]
            : [
                { scheme: "file", language: "recordflux" },
                { scheme: "untitled", language: "recordflux" },
            ],
        synchronize: {
            fileEvents: vscode_1.workspace.createFileSystemWatcher("**/.clientrc"),
        },
        outputChannel: outputChannel,
        traceOutputChannel: outputChannel,
        revealOutputChannelOn: node_1.RevealOutputChannelOn.Never,
        initializationOptions,
    };
    return new node_1.LanguageClient(serverId, serverName, serverOptions, clientOptions);
}
let _disposables = [];
async function restartServer(serverId, serverName, outputChannel, lsClient) {
    if (lsClient) {
        (0, logging_1.traceInfo)(`Server: Stop requested`);
        await lsClient.stop();
        _disposables.forEach((d) => d.dispose());
        _disposables = [];
    }
    const projectRoot = await (0, utilities_1.getProjectRoot)();
    const workspaceSetting = await (0, settings_1.getWorkspaceSettings)(serverId, projectRoot, true);
    const newLSClient = await createServer(workspaceSetting, serverId, serverName, outputChannel, {
        settings: await (0, settings_1.getExtensionSettings)(serverId, true),
        globalSettings: await (0, settings_1.getGlobalSettings)(serverId, false),
    });
    (0, logging_1.traceInfo)(`Server: Start requested.`);
    _disposables.push(newLSClient.onDidChangeState((e) => {
        switch (e.newState) {
            case vscode_languageclient_1.State.Stopped:
                (0, logging_1.traceVerbose)(`Server State: Stopped`);
                break;
            case vscode_languageclient_1.State.Starting:
                (0, logging_1.traceVerbose)(`Server State: Starting`);
                break;
            case vscode_languageclient_1.State.Running:
                (0, logging_1.traceVerbose)(`Server State: Running`);
                break;
        }
    }));
    try {
        await newLSClient.start();
    }
    catch (ex) {
        (0, logging_1.traceError)(`Server: Start failed: ${ex}`);
        return undefined;
    }
    const level = (0, utilities_1.getLSClientTraceLevel)(outputChannel.logLevel, vscode_1.env.logLevel);
    await newLSClient.setTrace(level);
    return newLSClient;
}
exports.restartServer = restartServer;
//# sourceMappingURL=server.js.map