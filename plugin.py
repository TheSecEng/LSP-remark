# Packages/LSP-remark/plugin.py

import os

from lsp_utils import NpmClientHandler


class LspRemark(NpmClientHandler):
    package_name = __package__
    server_directory = 'server'
    server_binary_path = os.path.join(
        server_directory, 'node_modules', 'remark-language-server', 'index.js')


def plugin_loaded():
    LspRemark.setup()


def plugin_unloaded():
    LspRemark.cleanup()
