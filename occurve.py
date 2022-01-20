import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import sys

def occurve(n,c,p):
    res = stats.poisson.cdf(k=c, mu=n*p)
    return res

class SnappingCursor:
    """
    A cross hair cursor that snaps to the data point of a line, which is
    closest to the *x* position of the cursor.

    For simplicity, this assumes that *x* values of the data are sorted.
    """
    def __init__(self, ax, line):
        self.ax = ax
        self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
        self.x, self.y = line.get_data()
        self._last_index = None
        # text location in axes coords
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)

    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw

    def on_mouse_move(self, event):
        if not event.inaxes:
            self._last_index = None
            need_redraw = self.set_cross_hair_visible(False)
            if need_redraw:
                self.ax.figure.canvas.draw()
        else:
            self.set_cross_hair_visible(True)
            x, y = event.xdata, event.ydata
            index = min(np.searchsorted(self.x, x), len(self.x) - 1)
            if index == self._last_index:
                return  # still on the same data point. Nothing to do.
            self._last_index = index
            x = self.x[index]
            y = self.y[index]
            # update the line positions
            self.horizontal_line.set_ydata(y)
            self.vertical_line.set_xdata(x)
            self.text.set_text('x=%1.3f, y=%1.3f' % (x, y))
            self.ax.figure.canvas.draw()

def main():
    # plot occurve for p in range (0,0.1,0.002)
    n = int(sys.argv[1])
    c = int(sys.argv[2])
    p = np.arange(0,0.2,0.002)
    res = []
    for i in p:
        res.append(occurve(n,c,i))
    fig, ax = plt.subplots()
    ax.set_title('Snapping cursor')
    line1, = ax.plot(p, res, 'o-')
    ax.set(xlabel='p', ylabel='Pa', title='OC curve for n=%d, c=%d' % (n,c))
    ax.grid()
    snap_cursor = SnappingCursor(ax, line1)
    fig.canvas.mpl_connect('motion_notify_event', snap_cursor.on_mouse_move)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main()
    else:
        print("Usage: $ py occurve.py <n> <c>")