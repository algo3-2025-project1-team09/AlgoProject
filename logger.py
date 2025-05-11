import threading
import queue

class Logger:
    def __init__(self, log_file="battle_log.txt"):
        self.log_file = log_file
        self.log_queue = queue.Queue()
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.running = False

    def start(self):
        self.running = True
        self.thread.start()

    def log_event(self, message):
        self.log_queue.put(message)

    def _run(self):
        with open(self.log_file, "w") as f:
            while self.running or not self.log_queue.empty():
                try:
                    message = self.log_queue.get(timeout=1)
                    print(message)
                    f.write(message + "\n")
                    f.flush()
                except queue.Empty:
                    continue

    def stop(self):
        self.running = False
        self.thread.join()