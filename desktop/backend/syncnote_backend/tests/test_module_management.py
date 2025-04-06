# tests/test_module_management.py

import pytest
from src.core.module_controller import start_module, stop_module, list_modules

def test_start_module():
    start_module("SyncService")
    assert "SyncService" in list_modules()

def test_stop_module():
    stop_module("SyncService")
    assert "SyncService" not in list_modules()
