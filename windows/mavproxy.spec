# -*- mode: python -*-
# spec file for pyinstaller to build mavproxy for windows
MAVProxyAny = Analysis(['mavproxy.py'],
             pathex=[os.path.abspath('.')],
             # for some unknown reason these hidden imports don't pull in
             # all the needed pieces, so we also import them in mavproxy.py
             hiddenimports=['cv2', 'wx', 'pylab', 
                            'numpy', 'dateutil', 'matplotlib',
                            'pymavlink.mavwp', 'pymavlink.mavutil', 
                            'pyreadline', 'pymavlink.dialects.v20.ardupilotmega',
                            'pymavlink.dialects.v10.ardupilotmega',
                            'pymavlink.dialects.v20.common', 'pymavlink.dialects.v10.common',
                            'pymavlink.dialects.v20.ASLUAV', 'pymavlink.dialects.v10.ASLUAV',
                            'pymavlink.dialects.v20.autoquad', 'pymavlink.dialects.v10.autoquad',
                            'pymavlink.dialects.v20.matrixpilot', 'pymavlink.dialects.v10.matrixpilot',
                            'pymavlink.dialects.v20.minimal', 'pymavlink.dialects.v10.minimal',
                            'pymavlink.dialects.v20.paparazzi', 'pymavlink.dialects.v10.paparazzi',
                            'pymavlink.dialects.v20.slugs', 'pymavlink.dialects.v10.slugs',
                            'pymavlink.dialects.v20.standard', 'pymavlink.dialects.v10.standard',
                            'pymavlink.dialects.v20.ualberta', 'pymavlink.dialects.v10.ualberta',
                            'pymavlink.dialects.v20.uAvionix', 'pymavlink.dialects.v10.uAvionix', 
                            'HTMLParser', 'wx.grid', 'pygame', 'pygame.base',
                            'pygame.constants', 'pygame.version', 'pygame.rect', 'pygame.compat', 
                            'pygame.rwobject', 'pygame.surflock', 'pygame.color', 'pygame.colordict', 
                            'pygame.cdrom', 'pygame.cursors', 'pygame.display', 'pygame.draw', 
                            'pygame.event', 'pygame.image', 'pygame.joystick', 'pygame.key', 
                            'pygame.mouse', 'pygame.sprite', 'pygame.threads', 'pygame.time', 
                            'pygame.transform', 'pygame.surface', 'pygame.bufferproxy', 'wx._grid',
                            'wx.lib.agw.genericmessagedialog', 'wx.lib.wordwrap', 'wx.lib.buttons',
                            'wx.lib.embeddedimage', 'wx.lib.imageutils', 'wx.lib.agw.aquabutton', 
                            'wx.lib.agw.gradientbutton', 'wxversion', 'UserList', 'UserString'],
             hookspath=None,
             runtime_hooks=None)
MAVExpAny = Analysis(['.\\tools\\MAVExplorer.py'],
             pathex=[os.path.abspath('.')],
             # for some unknown reason these hidden imports don't pull in
             # all the needed pieces, so we also import them in mavproxy.py
             hiddenimports=['cv2', 'wx', 'pylab', 
                            'numpy', 'dateutil', 'matplotlib',
                            'pymavlink.mavwp', 'pymavlink.mavutil', 'pymavlink.dialects.v20.ardupilotmega',
                            'pymavlink.dialects.v10.ardupilotmega',
                            'pymavlink.dialects.v20.common', 'pymavlink.dialects.v10.common',
                            'pymavlink.dialects.v20.ASLUAV', 'pymavlink.dialects.v10.ASLUAV',
                            'pymavlink.dialects.v20.autoquad', 'pymavlink.dialects.v10.autoquad',
                            'pymavlink.dialects.v20.matrixpilot', 'pymavlink.dialects.v10.matrixpilot',
                            'pymavlink.dialects.v20.minimal', 'pymavlink.dialects.v10.minimal',
                            'pymavlink.dialects.v20.paparazzi', 'pymavlink.dialects.v10.paparazzi',
                            'pymavlink.dialects.v20.slugs', 'pymavlink.dialects.v10.slugs',
                            'pymavlink.dialects.v20.standard', 'pymavlink.dialects.v10.standard',
                            'pymavlink.dialects.v20.ualberta', 'pymavlink.dialects.v10.ualberta',
                            'pymavlink.dialects.v20.uAvionix', 'pymavlink.dialects.v10.uAvionix', 
                            'pyreadline', 'HTMLParser', 'wx.grid', 'wx._grid',
                            'wx.lib.agw.genericmessagedialog', 'wx.lib.wordwrap', 'wx.lib.buttons',
                            'wx.lib.embeddedimage', 'wx.lib.imageutils', 'wx.lib.agw.aquabutton', 
                            'wx.lib.agw.gradientbutton', 'FileDialog', 'Dialog', 'UserList', 'UserString'],
             hookspath=None,
             runtime_hooks=None)
MERGE( (MAVProxyAny, 'mavproxy', 'mavproxy'), (MAVExpAny, 'MAVExplorer', 'MAVExplorer') )
MAVProxy_pyz = PYZ(MAVProxyAny.pure)
MAVProxy_exe = EXE(MAVProxy_pyz,
          MAVProxyAny.scripts,
          exclude_binaries=True,
          name='mavproxy.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
MAVProxy_coll = COLLECT(MAVProxy_exe,
               MAVProxyAny.binaries,
               MAVProxyAny.zipfiles,
               MAVProxyAny.datas,
               strip=None,
               upx=True,
               name='mavproxy')

MAVExp_pyz = PYZ(MAVExpAny.pure)
MAVExp_exe = EXE(MAVExp_pyz,
          MAVExpAny.scripts,
          exclude_binaries=True,
          name='MAVExplorer.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
MAVExp_coll = COLLECT(MAVExp_exe,
               MAVExpAny.binaries,
               MAVExpAny.zipfiles,
               MAVExpAny.datas,
               strip=None,
               upx=True,
               name='MAVExplorer')
