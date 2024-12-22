# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# This file is generated by wxPython's PI generator.  Do not edit by hand.
#
# The *.pyi files are used by PyCharm and other development tools to provide
# more information, such as PEP 484 type hints, than it is able to glean from
# introspection of extension types and methods.  They are not intended to be
# imported, executed or used for any other purpose other than providing info
# to the tools. If you don't use use a tool that makes use of .pyi files then
# you can safely ignore this file.
#
# See: https://www.python.org/dev/peps/pep-0484/
#      https://www.jetbrains.com/help/pycharm/2016.1/type-hinting-in-pycharm.html
#
# Copyright: (c) 2020 by Total Control Software
# License:   wxWindows License
#---------------------------------------------------------------------------


"""
These classes enable viewing and interacting with an OpenGL context in a wx.Window.
"""
#-- begin-_glcanvas --#

import wx
WX_GL_RGBA = 0
WX_GL_BUFFER_SIZE = 0
WX_GL_LEVEL = 0
WX_GL_DOUBLEBUFFER = 0
WX_GL_STEREO = 0
WX_GL_AUX_BUFFERS = 0
WX_GL_MIN_RED = 0
WX_GL_MIN_GREEN = 0
WX_GL_MIN_BLUE = 0
WX_GL_MIN_ALPHA = 0
WX_GL_DEPTH_SIZE = 0
WX_GL_STENCIL_SIZE = 0
WX_GL_MIN_ACCUM_RED = 0
WX_GL_MIN_ACCUM_GREEN = 0
WX_GL_MIN_ACCUM_BLUE = 0
WX_GL_MIN_ACCUM_ALPHA = 0
WX_GL_SAMPLE_BUFFERS = 0
WX_GL_SAMPLES = 0
WX_GL_FRAMEBUFFER_SRGB = 0
WX_GL_MAJOR_VERSION = 0
WX_GL_MINOR_VERSION = 0
WX_GL_CORE_PROFILE = 0
_GL_COMPAT_PROFILE = 0
WX_GL_FORWARD_COMPAT = 0
WX_GL_ES2 = 0
WX_GL_DEBUG = 0
WX_GL_ROBUST_ACCESS = 0
WX_GL_NO_RESET_NOTIFY = 0
WX_GL_LOSE_ON_RESET = 0
WX_GL_RESET_ISOLATION = 0
WX_GL_RELEASE_FLUSH = 0
WX_GL_RELEASE_NONE = 0

class GLAttribsBase(object):
    """
    GLAttribsBase()
    
    This is the base class for wxGLAttributes and wxGLContextAttrs.
    """

    def __init__(self):
        """
        GLAttribsBase()
        
        This is the base class for wxGLAttributes and wxGLContextAttrs.
        """

    def AddAttribute(self, attribute):
        """
        AddAttribute(attribute)
        
        Adds an integer value to the list of attributes.
        """

    def AddAttribBits(self, searchVal, combineVal):
        """
        AddAttribBits(searchVal, combineVal)
        
        Combine (bitwise OR) a given value with the existing one, if any.
        """

    def SetNeedsARB(self, needsARB=True):
        """
        SetNeedsARB(needsARB=True)
        
        Sets the necessity of using special ARB-functions (e.g.
        """

    def Reset(self):
        """
        Reset()
        
        Delete contents and sets ARB-flag to false.
        """

    def GetSize(self):
        """
        GetSize() -> int
        
        Returns the size of the internal list of attributes.
        """

    def NeedsARB(self):
        """
        NeedsARB() -> bool
        
        Returns the current value of the ARB-flag.
        """
    Size = property(None, None)
# end of class GLAttribsBase


class GLAttributes(GLAttribsBase):
    """
    This class is used for setting display attributes when drawing through
    OpenGL ("Pixel format" in MSW and OSX parlance, "Configs" in X11).
    """

    def RGBA(self):
        """
        RGBA() -> GLAttributes
        
        Use true colour instead of colour index rendering for each pixel.
        """

    def BufferSize(self, val):
        """
        BufferSize(val) -> GLAttributes
        
        Specifies the number of bits for colour buffer.
        """

    def Level(self, val):
        """
        Level(val) -> GLAttributes
        
        Specifies the framebuffer level.
        """

    def DoubleBuffer(self):
        """
        DoubleBuffer() -> GLAttributes
        
        Requests using double buffering.
        """

    def Stereo(self):
        """
        Stereo() -> GLAttributes
        
        Use stereoscopic display.
        """

    def AuxBuffers(self, val):
        """
        AuxBuffers(val) -> GLAttributes
        
        Specifies the number of auxiliary buffers.
        """

    def MinRGBA(self, mRed, mGreen, mBlue, mAlpha):
        """
        MinRGBA(mRed, mGreen, mBlue, mAlpha) -> GLAttributes
        
        Specifies the minimal number of bits for each colour and alpha.
        """

    def Depth(self, val):
        """
        Depth(val) -> GLAttributes
        
        Specifies number of bits for Z-buffer.
        """

    def Stencil(self, val):
        """
        Stencil(val) -> GLAttributes
        
        Specifies number of bits for stencil buffer.
        """

    def MinAcumRGBA(self, mRed, mGreen, mBlue, mAlpha):
        """
        MinAcumRGBA(mRed, mGreen, mBlue, mAlpha) -> GLAttributes
        
        Specifies the minimal number of bits for each accumulator channel.
        """

    def SampleBuffers(self, val):
        """
        SampleBuffers(val) -> GLAttributes
        
        Use multi-sampling support (antialiasing).
        """

    def Samplers(self, val):
        """
        Samplers(val) -> GLAttributes
        
        Specifies the number of samplers per pixel.
        """

    def FrameBuffersRGB(self):
        """
        FrameBuffersRGB() -> GLAttributes
        
        Used to request a frame buffer sRGB capable.
        """

    def PlatformDefaults(self):
        """
        PlatformDefaults() -> GLAttributes
        
        Set some typically needed attributes.
        """

    def Defaults(self):
        """
        Defaults() -> GLAttributes
        
        wxWidgets defaults: RGBA, Z-depth 16 bits, double buffering, 1 sample
        buffer, 4 samplers.
        """

    def EndList(self):
        """
        EndList()
        
        The set of attributes must end with this one; otherwise, the GPU may
        display nothing at all.
        """
# end of class GLAttributes


class GLContextAttrs(GLAttribsBase):
    """
    This class is used for setting context attributes.
    """

    def CoreProfile(self):
        """
        CoreProfile() -> GLContextAttrs
        
        Request an OpenGL core profile for the context.
        """

    def MajorVersion(self, val):
        """
        MajorVersion(val) -> GLContextAttrs
        
        Request specific OpenGL core major version number (>= 3).
        """

    def MinorVersion(self, val):
        """
        MinorVersion(val) -> GLContextAttrs
        
        Request specific OpenGL core minor version number.
        """

    def OGLVersion(self, vmayor, vminor):
        """
        OGLVersion(vmayor, vminor) -> GLContextAttrs
        
        An easy way of requesting an OpenGL version.
        """

    def CompatibilityProfile(self):
        """
        CompatibilityProfile() -> GLContextAttrs
        
        Request a type of context with all OpenGL features from version 1.0 to
        the newest available by the GPU driver.
        """

    def ForwardCompatible(self):
        """
        ForwardCompatible() -> GLContextAttrs
        
        Request a forward-compatible context.
        """

    def ES2(self):
        """
        ES2() -> GLContextAttrs
        
        Request an ES or ES2 ("Embedded Subsystem") context.
        """

    def DebugCtx(self):
        """
        DebugCtx() -> GLContextAttrs
        
        Request debugging functionality.
        """

    def Robust(self):
        """
        Robust() -> GLContextAttrs
        
        Request robustness, or how OpenGL handles out-of-bounds buffer object
        accesses and graphics reset notification behaviours.
        """

    def NoResetNotify(self):
        """
        NoResetNotify() -> GLContextAttrs
        
        With robustness enabled, never deliver notification of reset events.
        """

    def LoseOnReset(self):
        """
        LoseOnReset() -> GLContextAttrs
        
        With robustness enabled, if graphics reset happens, all context state
        is lost.
        """

    def ResetIsolation(self):
        """
        ResetIsolation() -> GLContextAttrs
        
        Request OpenGL to protect other applications or shared contexts from
        reset side-effects.
        """

    def ReleaseFlush(self, val=1):
        """
        ReleaseFlush(val=1) -> GLContextAttrs
        
        Request OpenGL to avoid or not flushing pending commands when the
        context is made no longer current (released).
        """

    def PlatformDefaults(self):
        """
        PlatformDefaults() -> GLContextAttrs
        
        Set platform specific defaults.
        """

    def EndList(self):
        """
        EndList()
        
        The set of attributes must end with this one; otherwise, the GPU may
        display nothing at all.
        """
# end of class GLContextAttrs


class GLContext(Object):
    """
    GLContext(win, other=None, ctxAttrs=None)
    
    An instance of a wxGLContext represents the state of an OpenGL state
    machine and the connection between OpenGL and the system.
    """

    def __init__(self, win, other=None, ctxAttrs=None):
        """
        GLContext(win, other=None, ctxAttrs=None)
        
        An instance of a wxGLContext represents the state of an OpenGL state
        machine and the connection between OpenGL and the system.
        """

    def IsOK(self):
        """
        IsOK() -> bool
        
        Checks if the underlying OpenGL rendering context was correctly
        created by the system with the requested attributes.
        """

    def SetCurrent(self, win):
        """
        SetCurrent(win) -> bool
        
        Makes the OpenGL state that is represented by this rendering context
        current with the wxGLCanvas win.
        """
# end of class GLContext


class GLCanvas(Window):
    """
    GLCanvas(parent, dispAttrs, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=GLCanvasName, palette=NullPalette)
    GLCanvas(parent, id=wx.ID_ANY, attribList=None, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name='GLCanvas', palette=wx.NullPalette)
    
    wxGLCanvas is a class for displaying OpenGL graphics.
    """

    def __init__(self, *args, **kw):
        """
        GLCanvas(parent, dispAttrs, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=GLCanvasName, palette=NullPalette)
        GLCanvas(parent, id=wx.ID_ANY, attribList=None, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name='GLCanvas', palette=wx.NullPalette)
        
        wxGLCanvas is a class for displaying OpenGL graphics.
        """

    def CreateSurface(self):
        """
        CreateSurface() -> bool
        
        Re-creates EGLSurface.
        """

    def SetColour(self, colour):
        """
        SetColour(colour) -> bool
        
        Sets the current colour for this window (using glcolor3f()), using the
        wxWidgets colour database to find a named colour.
        """

    def SetCurrent(self, context):
        """
        SetCurrent(context) -> bool
        
        Makes the OpenGL state that is represented by the OpenGL rendering
        context context current, i.e.
        """

    def SwapBuffers(self):
        """
        SwapBuffers() -> bool
        
        Swaps the double-buffer of this window, making the back-buffer the
        front-buffer and vice versa, so that the output of the previous OpenGL
        commands is displayed on the window.
        """

    @staticmethod
    def IsDisplaySupported(*args, **kw):
        """
        IsDisplaySupported(dispAttrs) -> bool
        IsDisplaySupported(attribList) -> bool
        
        Determines if a canvas having the specified attributes is available.
        """

    @staticmethod
    def IsExtensionSupported(extension):
        """
        IsExtensionSupported(extension) -> bool
        
        Returns true if the extension with given name is supported.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL):
        """
        GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes
        """
# end of class GLCanvas

USE_GLCANVAS = 0
#-- end-_glcanvas --#
