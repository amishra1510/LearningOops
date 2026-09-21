class SecurityCamera:

    def __init__(self, camera_id, resolution):
        self.camera_id = camera_id
        self.resolution = resolution

    def camera_info(self):
        print(self.camera_id)
        print(self.resolution)


class AlarmSystem:

    def __init__(self, alarm_type, alarm_status):
        self.alarm_type = alarm_type
        self.alarm_status = alarm_status

    def alarm_info(self):
        print(self.alarm_type)
        print(self.alarm_status)


class AccessControl:

    def __init__(self, access_type, authorized_users):
        self.access_type = access_type
        self.authorized_users = authorized_users

    def access_info(self):
        print(self.access_type)
        print(self.authorized_users)


class SmartSecuritySystem(SecurityCamera, AlarmSystem, AccessControl):

    def __init__(self, camera_id, resolution,
                 alarm_type, alarm_status,
                 access_type, authorized_users):

        SecurityCamera.__init__(self, camera_id, resolution)
        AlarmSystem.__init__(self, alarm_type, alarm_status)
        AccessControl.__init__(self, access_type, authorized_users)


obj = SmartSecuritySystem(
    12, "1440p",
    "Fire", "Morning",
    "Personnel", "Guards"
)

obj.camera_info()
obj.alarm_info()
obj.access_info()

print(SmartSecuritySystem.mro())











class SecurityCamera:

    def __init__(self, camera_id, resolution, **kwargs):
        self.camera_id = camera_id
        self.resolution = resolution
        super().__init__(**kwargs)

    def camera_info(self):
        print(self.camera_id)
        print(self.resolution)


class AlarmSystem:

    def __init__(self, alarm_type, alarm_status, **kwargs):
        self.alarm_type = alarm_type
        self.alarm_status = alarm_status
        super().__init__(**kwargs)

    def alarm_info(self):
        print(self.alarm_type)
        print(self.alarm_status)


class AccessControl:

    def __init__(self, access_type, authorized_users, **kwargs):
        self.access_type = access_type
        self.authorized_users = authorized_users
        super().__init__(**kwargs)

    def access_info(self):
        print(self.access_type)
        print(self.authorized_users)


class SmartSecuritySystem(SecurityCamera, AlarmSystem, AccessControl):

    def __init__(self, camera_id, resolution,
                 alarm_type, alarm_status,
                 access_type, authorized_users):

        super().__init__(
            camera_id=camera_id,
            resolution=resolution,
            alarm_type=alarm_type,
            alarm_status=alarm_status,
            access_type=access_type,
            authorized_users=authorized_users
        )


obj = SmartSecuritySystem(
    12, "1440p",
    "Fire", "Morning",
    "Personnel", "Guards"
)

obj.camera_info()
obj.alarm_info()
obj.access_info()

print(SmartSecuritySystem.mro())


    




