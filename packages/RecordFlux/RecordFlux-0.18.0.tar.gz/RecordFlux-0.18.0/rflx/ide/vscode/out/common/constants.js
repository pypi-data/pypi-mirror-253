"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CACHE_DIR = exports.EXTENSION_ROOT_DIR = void 0;
const path = require("path");
const os_1 = require("os");
const folderName = path.basename(__dirname);
exports.EXTENSION_ROOT_DIR = folderName === "common"
    ? path.dirname(path.dirname(__dirname))
    : path.dirname(__dirname);
exports.CACHE_DIR = path.join((0, os_1.homedir)(), ".cache", "RecordFlux");
//# sourceMappingURL=constants.js.map