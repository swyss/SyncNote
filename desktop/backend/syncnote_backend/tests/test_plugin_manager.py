# tests/test_plugin_manager.py

from src.core.plugin_manager import load_plugin

def test_load_plugin():
    plugin = load_plugin("src.plugins.example_plugin")
    assert plugin is not None
