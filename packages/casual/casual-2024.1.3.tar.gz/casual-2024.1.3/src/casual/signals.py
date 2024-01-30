from blinker import Namespace

casual_log = Namespace()

log_signal = casual_log.signal("log_signal")
