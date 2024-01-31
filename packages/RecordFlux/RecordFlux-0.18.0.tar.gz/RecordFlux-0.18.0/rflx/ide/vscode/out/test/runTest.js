"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const path = require("path");
const cp = require("child_process");
const test_electron_1 = require("@vscode/test-electron");
async function main() {
    try {
        // The folder containing the Extension Manifest package.json
        // Passed to `--extensionDevelopmentPath`
        const extensionDevelopmentPath = path.resolve(__dirname, "../../");
        // The path to the extension test script
        // Passed to --extensionTestsPath
        const extensionTestsPath = path.resolve(__dirname, "./index");
        const vscodeExecutablePath = await (0, test_electron_1.downloadAndUnzipVSCode)("1.77.0");
        const [cliPath, ...args] = (0, test_electron_1.resolveCliArgsFromVSCodeExecutablePath)(vscodeExecutablePath);
        cp.spawnSync(cliPath, [...args, "--install-extension", "ms-python.python"], {
            encoding: "utf-8",
            stdio: "inherit",
        });
        // Run the extension test
        await (0, test_electron_1.runTests)({
            // Use the specified `code` executable
            vscodeExecutablePath,
            extensionDevelopmentPath,
            extensionTestsPath,
        });
    }
    catch (err) {
        console.error("Failed to run tests");
        process.exit(1);
    }
}
main();
//# sourceMappingURL=runTest.js.map