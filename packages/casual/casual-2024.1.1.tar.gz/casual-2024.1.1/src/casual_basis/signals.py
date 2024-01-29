from blinker import Namespace

basis = Namespace()

app_installed = basis.signal('app_installed')
app_removed = basis.signal('app_removed')
