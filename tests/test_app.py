from app import App
import os

app = App()

def test_app_init():
    assert app

def test_load_plugin():
    assert app.load_plugins() == True
