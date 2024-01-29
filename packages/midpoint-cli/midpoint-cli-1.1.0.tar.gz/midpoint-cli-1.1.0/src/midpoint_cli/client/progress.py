class AsciiProgressMonitor:
    def __init__(self, width=80, icon='.'):
        self._progress = 0
        self._width = width
        self._icon = icon

    def update(self, progress: int) -> None:
        while self._progress < progress:
            self.advance()

    def advance(self):
        if self._progress % self._width == 0:
            if self._progress > 0:
                print(' %7d' % (self._progress))

            print('Progress: ', end='', flush=True)

        print(self._icon, end='', flush=True)
        self._progress += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print()
        print('Total progress:', self._progress)
