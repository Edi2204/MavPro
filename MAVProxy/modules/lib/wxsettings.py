'''
Graphical editing of mp_settings object
'''
import os, sys
import multiprocessing, threading

class WXSettings(object):
    '''
    a graphical settings dialog for mavproxy
    '''
    def __init__(self, settings):
        self.settings  = settings
        self.parent_pipe,self.child_pipe = multiprocessing.Pipe()
        self.close_event = multiprocessing.Event()
        self.close_event.clear()
        self.child = multiprocessing.Process(target=self.child_task)
        self.child.start()
        t = threading.Thread(target=self.watch_thread)
        t.daemon = True
        t.start()

    def child_task(self):
        '''child process - this holds all the GUI elements'''
        from MAVProxy.modules.lib import mp_util
        from MAVProxy.modules.lib import wx_processguard
        from MAVProxy.modules.lib.wx_loader import wx
        from MAVProxy.modules.lib.wxsettings_ui import SettingsDlg

        mp_util.child_close_fds()
        app = wx.App(False)
        with SettingsDlg(self.settings) as dlg:
            dlg.parent_pipe = self.parent_pipe
            dlg.ShowModal()

    def watch_thread(self):
        '''watch for settings changes from child'''
        from MAVProxy.modules.lib.mp_settings import MPSetting
        while True:
            setting = self.child_pipe.recv()
            if not isinstance(setting, MPSetting):
                break
            try:
                self.settings.set(setting.name, setting.value)
            except Exception:
                print("Unable to set %s to %s" % (setting.name, setting.value))

    def is_alive(self):
        '''check if child is still going'''
        return self.child.is_alive()


if __name__ == "__main__":
    multiprocessing.freeze_support()

    def test_callback(setting):
        '''callback on apply'''
        print("Changing %s to %s" % (setting.name, setting.value))

    # test the settings
    import MAVProxy.modules.lib.mp_settings, time
    from MAVProxy.modules.lib.mp_settings import MPSetting
    settings = MAVProxy.modules.lib.mp_settings.MPSettings(
        [ MPSetting('link', int, 1, tab='TabOne'),
          MPSetting('altreadout', int, 10, range=(-30,1017), increment=1),
          MPSetting('pvalue', float, 0.3, range=(-3.0,1e6), increment=0.1, digits=2),
          MPSetting('enable', bool, True, tab='TabTwo'),
          MPSetting('colour', str, 'Blue', choice=['Red', 'Green', 'Blue']),
          MPSetting('foostr', str, 'blah', label='Foo String') ])
    settings.set_callback(test_callback)
    dlg = WXSettings(settings)
    while dlg.is_alive():
        time.sleep(0.1)
