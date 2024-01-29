from casual_basis.signals import app_installed, app_removed


@app_installed.connect
def app_installed_hook(sender, **extras):
    ...


@app_removed.connect
def app_removed_hook(sender, **extras):
    ...
