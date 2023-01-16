from scribes.terminalScribe import TerminalScribe

class PlotScribe(TerminalScribe):

    def __init__(self, domain, **kwargs):
        self.x = domain[0]
        self.domain = domain
        super().__init__(**kwargs)

    def toDict(self):
        data = super().toDict()
        data['x'] = self.x 
        data['domain'] = self.domain
        return data

    def fromDict(self, g):
        scribe = g[self.get('classname')](
            color=self.get('color'),
            mark=self.get('mark'),
            trail=self.get('trail'),
            pos=self.get('pos'),
            domain=self.get('domain'),
        )
        scribe.x = self.get('x')
        return scribe

    def _plotX(self, function, canvas):
        pos = [self.x, function(self.x)]
        if not canvas.hitsWall(pos):
            self.draw(pos, canvas)
        self.x = self.x + 1

    def plotX(self, function):
        self.x = self.domain[0]
        for _ in range(self.domain[0], self.domain[1]):
            self.moves.append((self._plotX, [function]))