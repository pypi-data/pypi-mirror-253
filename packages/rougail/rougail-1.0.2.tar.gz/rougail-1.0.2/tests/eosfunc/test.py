from tiramisu import valid_not_equal, valid_ip_netmask, calc_value, valid_in_network, calc_value_property_help


def trange(start, stop):
    return list(range(start, stop))


def calc_val(*args, **kwargs):
    if len(args) > 0:
        return args[0]


def concat(*args, **kwargs):
    pass


def calc_multi_condition(*args, **kwargs):
    pass


def get_zone_name_bridge(*args, **kwargs):
    pass


def get_devices(*args, **kwargs):
    pass


def get_mount_point_device(*args, **kwargs):
    pass


def valid_differ(*args, **kwargs):
    pass


def valid_ipnetmask(*args, **kwargs):
    pass


def valid_enum(*args, **kwargs):
    pass


def valid_lower(*args, **kwargs):
    pass


def list_files(*args, **kwargs):
    # FIXME ?
    return kwargs['default']


def calc_multi_val(*args, **kwargs):
    return args[0]


def cdrom_minormajor(*args, **kwargs):
    pass


def device_type(*args, **kwargs):
    pass


def calc_list(*args, **kwargs):
    return list(args)


def test_index(index):
    return index


def return_no():
    return 'no'


def return_yes():
    return 'yes'
