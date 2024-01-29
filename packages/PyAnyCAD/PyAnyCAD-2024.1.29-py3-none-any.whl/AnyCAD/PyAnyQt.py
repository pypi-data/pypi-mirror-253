from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer, QAbstractEventDispatcher

from AnyCAD import PyAnyCAD as AnyCAD
from AnyCAD.PyAnyCore import IRenderControl

class QtRenderControl(QWidget, IRenderControl):
    '''
    Qt三维控件
    '''
    def __init__(self, par):
        super().__init__(par)

        sz = self.size()
        self.Viewer = AnyCAD.RenderingEngine.CreateView(int(self.winId()), sz.width(), sz.height())
        self.Viewer.InstallEventHandlers()
        QAbstractEventDispatcher.instance().awake.connect(self.Redraw)
        self.timer = QTimer(self)
        self.timer.setInterval(33)
        self.timer.timeout.connect(self._RenderOneFrame)     
    
    def Redraw(self):
        '''
        绘制
        '''
        self.timer.stop()
        hit = self._RenderOneFrame()
        if hit == AnyCAD.EnumRedrawResult_Idle:
            return
        elif hit == AnyCAD.EnumRedrawResult_Animation or hit == AnyCAD.EnumRedrawResult_Partial:
            self.timer.start()
        else:
            return

    def _RenderOneFrame(self):
        '''
        内部方法
        '''
        tick = self.Viewer.GetTimeTicks()
        self.Viewer.OnTime(tick)
        return self.Viewer.Redraw(tick)

    def resizeEvent(self, evt):
        sz = self.size()
        self.Viewer.OnResized(int(sz.width()), int(sz.height()))        
    def paintEngine(self):
        return None
    def paintEvent(self, event):
        self.Viewer.RequestUpdate(AnyCAD.EnumUpdateFlags_Dynamic)