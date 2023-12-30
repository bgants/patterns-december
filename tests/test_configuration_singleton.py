from patterns import configuration


def test_singleton():
    config = configuration.Configuration()
    config.set_debug_mode(True)
    assert config.get_debug_mode() == True
