import sys
sys.path.append('.')

from logstash_index_cleaner import get_index_epoch, find_expired_indices, find_overusage_indices

def test_get_index_epoch():
    """ This guy isn't very flexible :( """
    unprefixed_index_name = '013.12.16'
    assert get_index_epoch(unprefixed_index_name) == 1387191600.0
