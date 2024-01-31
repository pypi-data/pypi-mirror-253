"use strict";
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
Object.defineProperty(exports, "__esModule", { value: true });
exports.traceVerbose = exports.traceInfo = exports.traceWarn = exports.traceError = exports.traceLog = exports.registerLogger = void 0;
const util = require("util");
class OutputChannelLogger {
    constructor(channel) {
        this.channel = channel;
    }
    traceLog(...data) {
        this.channel.appendLine(util.format(...data));
    }
    traceError(...data) {
        this.channel.error(util.format(...data));
    }
    traceWarn(...data) {
        this.channel.warn(util.format(...data));
    }
    traceInfo(...data) {
        this.channel.info(util.format(...data));
    }
    traceVerbose(...data) {
        this.channel.debug(util.format(...data));
    }
}
let channel;
function registerLogger(logChannel) {
    channel = new OutputChannelLogger(logChannel);
    return {
        dispose: () => {
            channel = undefined;
        },
    };
}
exports.registerLogger = registerLogger;
function traceLog(...args) {
    channel === null || channel === void 0 ? void 0 : channel.traceLog(...args);
}
exports.traceLog = traceLog;
function traceError(...args) {
    channel === null || channel === void 0 ? void 0 : channel.traceError(...args);
}
exports.traceError = traceError;
function traceWarn(...args) {
    channel === null || channel === void 0 ? void 0 : channel.traceWarn(...args);
}
exports.traceWarn = traceWarn;
function traceInfo(...args) {
    channel === null || channel === void 0 ? void 0 : channel.traceInfo(...args);
}
exports.traceInfo = traceInfo;
function traceVerbose(...args) {
    channel === null || channel === void 0 ? void 0 : channel.traceVerbose(...args);
}
exports.traceVerbose = traceVerbose;
//# sourceMappingURL=logging.js.map