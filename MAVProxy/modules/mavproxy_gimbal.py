#!/usr/bin/env python
'''
gimbal control module
Andrew Tridgell
January 2015
'''

import sys, os, time
from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib import mp_util
from MAVProxy.modules.mavproxy_map import mp_slipmap
from pymavlink import mavutil
from pymavlink.rotmat import Vector3, Matrix3, Plane, Line
from math import radians
if mp_util.has_wxpython:
    from MAVProxy.modules.lib.mp_menu import *

class GimbalModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(GimbalModule, self).__init__(mpstate, "gimbal", "gimbal control module")
        self.add_command('gimbal', self.cmd_gimbal, "gimbal link control",
                         ['<rate|point|roi|mode|status>'])
        if mp_util.has_wxpython:
            self.menu = MPMenuSubMenu('Mount',
                                      items=[MPMenuItem('GPS targeting Mode', 'GPS Mode', '# gimbal mode gps'),
                                             MPMenuItem('MAVLink targeting Mode', 'MAVLink Mode', '# gimbal mode mavlink'),
                                             MPMenuItem('RC targeting Mode', 'RC Mode', '# gimbal mode rc'),
                                             MPMenuItem('Point At', 'Point At', '# gimbal roi')])
            self.menu_added_map = False
        else:
            self.menu = None

    def idle_task(self):
        '''called on idle'''
        if self.menu is not None and self.module('map') is not None and not self.menu_added_map:
            self.menu_added_map = True
            self.module('map').add_menu(self.menu)

    def cmd_gimbal(self, args):
        '''control gimbal'''
        usage = 'Usage: gimbal <rate|status>'
        if len(args) == 0:
            print(usage)
            return
        if args[0] == 'rate':
            self.cmd_gimbal_rate(args[1:])
        elif args[0] == 'point':
            self.cmd_gimbal_point(args[1:])
        elif args[0] == 'roi':
            self.cmd_gimbal_roi(args[1:])
        elif args[0] == 'mode':
            self.cmd_gimbal_mode(args[1:])
        elif args[0] == 'status':
            self.cmd_gimbal_status(args[1:])

    def cmd_gimbal_mode(self, args):
        '''control gimbal mode'''
        if len(args) != 1:
            print("usage: gimbal mode <GPS|MAVLink>")
            return
        if args[0].upper() == 'GPS':
            mode = mavutil.mavlink.MAV_MOUNT_MODE_GPS_POINT
        elif args[0].upper() == 'MAVLINK':
            mode = mavutil.mavlink.MAV_MOUNT_MODE_MAVLINK_TARGETING
        elif args[0].upper() == 'RC':
            mode = mavutil.mavlink.MAV_MOUNT_MODE_RC_TARGETING
        else:
            print("Unsupported mode %s" % args[0])
        self.master.mav.mount_configure_send(self.target_system,
                                             self.target_component,
                                             mode,
                                             1, 1, 1)

    def cmd_gimbal_roi(self, args):
        '''control roi position'''
        latlon = None
        try:
            latlon = self.module('map').click_position
        except Exception:
            print("No map available")
            return
        if latlon is None:
            print("No map click position available")
            return
        self.master.mav.mount_control_send(self.target_system,
                                           self.target_component,
                                           latlon[0]*1e7,
                                           latlon[1]*1e7,
                                           0, # altitude zero for now
                                           0)
        

    def cmd_gimbal_rate(self, args):
        '''control gimbal rate'''
        if len(args) != 3:
            print("usage: gimbal rate ROLL PITCH YAW")
            return
        (roll, pitch, yaw) = (float(args[0]), float(args[1]), float(args[2]))
        self.master.mav.gimbal_control_send(self.target_system,
                                            mavutil.mavlink.MAV_COMP_ID_GIMBAL,
                                            radians(roll),
                                            radians(pitch),
                                            radians(yaw))

    def cmd_gimbal_point(self, args):
        '''control gimbal pointing'''
        if len(args) != 3:
            print("usage: gimbal point ROLL PITCH YAW")
            return
        (roll, pitch, yaw) = (float(args[0]), float(args[1]), float(args[2]))
        self.master.mav.mount_control_send(self.target_system,
                                           self.target_component,
                                           pitch*100,
                                           roll*100,
                                           yaw*100,
                                           0)

    def cmd_gimbal_status(self, args):
        '''show gimbal status'''
        master = self.master
        if 'GIMBAL_REPORT' in master.messages:
            print(master.messages['GIMBAL_REPORT'])
        else:
            print("No GIMBAL_REPORT messages")

    def mavlink_packet(self, m):
        '''handle an incoming mavlink packet'''

        if not self.mpstate.map:
            # don't draw if no map
            return

        if m.get_type() != 'GIMBAL_REPORT':
            return

        needed = ['ATTITUDE', 'GLOBAL_POSITION_INT']
        for n in needed:
            if not n in self.master.messages:
                return

        # clear the camera icon
        self.mpstate.map.add_object(mp_slipmap.SlipClearLayer('GimbalView'))

        gpi = self.master.messages['GLOBAL_POSITION_INT']
        att = self.master.messages['ATTITUDE']
        vehicle_dcm = Matrix3()
        vehicle_dcm.from_euler(att.roll, att.pitch, att.yaw)

        rotmat_copter_gimbal = Matrix3()
        rotmat_copter_gimbal.from_euler312(m.joint_roll, m.joint_el, m.joint_az)
        gimbal_dcm = vehicle_dcm * rotmat_copter_gimbal
        
        lat = gpi.lat * 1.0e-7
        lon = gpi.lon * 1.0e-7
        alt = gpi.relative_alt * 1.0e-3

        # ground plane
        ground_plane = Plane()

        # the position of the camera in the air, remembering its a right
        # hand coordinate system, so +ve z is down
        camera_point = Vector3(0, 0, -alt)

        # get view point of camera when not rotated
        view_point = Vector3(1, 0, 0)
    
        # rotate view_point to form current view vector
        rot_point = gimbal_dcm * view_point

        # a line from the camera to the ground
        line = Line(camera_point, rot_point)

        # find the intersection with the ground
        pt = line.plane_intersection(ground_plane, forward_only=True)
        if pt is None:
	    # its pointing up into the sky
	    return None

        (view_lat, view_lon) = mp_util.gps_offset(lat, lon, pt.y, pt.x)

        icon = self.mpstate.map.icon('camera-small-red.png')
        self.mpstate.map.add_object(mp_slipmap.SlipIcon('gimbalview',
                                                        (view_lat,view_lon),
                                                        icon, layer='GimbalView', rotation=0, follow=False))


def init(mpstate):
    '''initialise module'''
    return GimbalModule(mpstate)
