import sys
sys.path.append('.')

import logstash_index_cleaner as lic

def test_get_index_epoch():
    """ This guy isn't very flexible :( """
    unprefixed_index_name = '013.12.16'
    assert lic.get_index_epoch(unprefixed_index_name) == 1387191600.0

def test_make_parser_dry_run_debug_log():
    """ Test parser instance """
    parser = lic.make_parser()
    arguments = parser.parse_args(['-n', '-l', 'debug'])
    assert arguments.level == 'debug'
    assert arguments.dry_run == True
