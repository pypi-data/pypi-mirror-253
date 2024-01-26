'''
Test class 
'''
from .helper import *
from src.biosequtils import Dir

@ddt
class TestDir(TestCase):

    def setUp(self):
        self.endpoint = 'ftp.ncbi.nlm.nih.gov'

    @data(
        ['a', True],
        [os.path.join('a', 'b', 'c'), True],
    )
    @unpack
    def test_init_dir(self, path, expect):
        indir = os.path.join(DIR_TMP, path)
        res = Dir(indir).init_dir()
        assert res == expect


    @data(
        ['a', '1', 3, 'a'],
        ['a', '12345', 2, os.path.join('a', '12', '34')],
        ['', '12345', 2, os.path.join('12', '34')],
    )
    @unpack
    def test_cascade_dir(self, parent_path, id_str, num, expect):
        res = Dir.cascade_dir(parent_path, id_str, num)
        assert res == expect