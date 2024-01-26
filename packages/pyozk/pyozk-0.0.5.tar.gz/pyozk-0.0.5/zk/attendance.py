# -*- coding: utf-8 -*-
import json


class Attendance(object):
    def __init__(self, user_id, timestamp, status, punch=0, uid=0):
        self.uid = uid # not really used any more
        self._user_id = user_id
        self._timestamp = timestamp
        self._status = status
        self._punch = punch
        self._device = ''
        self._user_name = ''

    def __str__(self):
        return '<Attendance>: {} : {} ({}, {})'.format(self._user_id, self._timestamp,
                                                       self._status, self._punch)

    def __repr__(self):
        return '<Attendance>: {} : {} ({}, {})'.format(self._user_id, self._timestamp,
                                                       self._status, self._punch)

    def __call__(self):
        return self._user_id, self._timestamp, self._status, self._punch

    @property
    def user_id(self):
        return self._user_id

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def status(self):
        return self._status

    @property
    def punch(self):
        return self._punch
    
    @property
    def device(self):
        return self._device
    @device.setter
    def device(self, value):
        self._device = value

    @property
    def user_name(self):
        return self._user_name
    @user_name.setter
    def user_name(self, value):
        self._user_name = value

class AttendanceEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Attendance):
            return {'time': obj.timestamp.isoformat(), 'userId': obj.user_id, 'status': obj.status, 'punch': obj.punch, 'device': obj.device, 'user_name': obj.user_name}
        return json.JSONEncoder.default(self, obj)