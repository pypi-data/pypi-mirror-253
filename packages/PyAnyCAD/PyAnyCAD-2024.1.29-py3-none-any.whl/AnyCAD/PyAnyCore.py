
import os
import sys

# Initialize the runtime path
_currentPath = os.path.dirname(__file__)
_runtimePath = os.path.abspath(os.path.join(_currentPath, "."))
if os.path.exists(os.path.join(_runtimePath, "_PyAnyCAD.pyd")) == False:
    print("Failed to find AnyCAD Runtime!")
    sys.exit(1)
    
sys.path.append(_currentPath)
sys.path.append(_runtimePath)

import PyAnyCAD as AnyCAD

class IRenderControl:
    '''
    显示控件接口
    '''
    def __init__(self):
        self.viewer = None

    def RequestDraw(self, flag):
        '''
        更新窗口
        :flag  更新标记类型 :py:class:'EnumUpdateFlags_'
        '''
        self.viewer.GetContext().RequestUpdate(flag)

    def ShowSceneNode(self, node):
        '''
        显示节点对象       
        :node 显示对象 :py:class:'SceneNode'
        '''
        ctx = self.viewer.GetContext()
        ctx.GetScene().AddNode(node)
        ctx.RequestUpdate(AnyCAD.EnumUpdateFlags_Scene)
        
    def ShowTopoShape(self, shape, material):
        '''
        显示几何对象
        :shape  几何对象 :py:class:'TopoShape'
        :material 材质对象 :py:class:'MaterialInstance'
        '''
        node = AnyCAD.BrepSceneNode.Create(shape, material, None, 0.1)
        self.ShowSceneNode(node)
        
    def Viewer(self):
        '''
        获得Viewer对象
        :return: :py:class:'Viewer'
        '''
        return self.viewer
    
    def ViewContext(self):
        '''
        获取显示上下文
        :return: :py:class:'ViewContext'
        '''
        return self.viewer.GetContext()
    def SceneManager(self):
        '''
        获取场景管理器
        :return: :py:class:'SceneManager'
        '''
        return self.viewer.GetContext().GetSceneManager()
    def Scene(self):
        '''
        获取三维主场景
        :return: :py:class:'Scene'
        '''
        return self.viewer.GetContext().GetScene()
    def Scene2D(self):
        '''
        获取二维主场景
        :return: :py:class:'Scene'
        '''
        return self.viewer.GetContext().GetScene2D()
    
    def ZoomAll(self, zoomFactor:float):
        '''
        缩放窗口
        :zoomFactor 缩放系数，比如1，1.1等
        '''
        return self.viewer.GetContext().ZoomToExtend(zoomFactor)

    
class RenderWindow(IRenderControl):
    '''
    渲染窗口
    '''
    def __init__(self, title:str, width:int, height:int):
        super().__init__()
        self.viewer = AnyCAD.Application.Instance().CreateWindow3D(title, width, height, True)

    def Show(self):
        '''
        显示窗口
        '''
        self.viewer.Run(None);
    
    def Destroy(self):
        '''
        释放资源
        '''
        self.viewer.Destroy();   


class GlobalInstance():
    '''
    应用入口实例，全局设置
    '''
    def Initialize():
        '''
        初始化。静态方法
        '''
        AnyCAD.Application.Instance().Initialize(AnyCAD.Path(_runtimePath), False)
        print("Welcome to use AnyCAD Rapid Py!")
        
    def Destroy():
        '''
        释放资源。静态方法
        '''
        AnyCAD.Application.Instance().Destroy()
        
    def RegisterSDK(email, uuid, sn):
        AnyCAD.RenderingEngine.RegiserPythonSdk(email, uuid, sn)

    def SetDpiScaling(scaling:float):
        '''
        设置屏幕缩放系数。静态方法
        '''
        AnyCAD.RenderingEngine.SetDpiScaling(scaling)



