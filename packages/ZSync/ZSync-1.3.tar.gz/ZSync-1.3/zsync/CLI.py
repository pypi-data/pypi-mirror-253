import argparse

class CLI:
    def __init__(self):
        self.parser = self._createArgParser()
    def _createArgParser(self):
        parser = argparse.ArgumentParser(prog='ZSync', description='ZSync')
        subparsers = parser.add_subparsers(required=True, dest='command')

        parserAdd = subparsers.add_parser('add', help='add a record')
        parserAdd.add_argument('-s', '--source', required=True, help='path to source')
        parserAdd.add_argument('-d', '--destination', required=True, help='path to destination')
        parserAdd.add_argument('-m', '--mode', required=False, choices=['two-way', 'src-to-dest', 'dest-to-src'], default='src-to-dest', help='zsync mode')

        parserList = subparsers.add_parser('list', help='list all records')

        parserRemove = subparsers.add_parser('remove', help='remove a record')
        parserRemove.add_argument('-i', '--index', required=True, type=int, help='index of the record to remove')

        parserSync = subparsers.add_parser('sync', help='sync all records')
        syncGroupSelect = parserSync.add_mutually_exclusive_group(required=True)
        syncGroupSelect.add_argument('-i', '--index', type=int, help='index of the record to sync')
        syncGroupSelect.add_argument('-a', '--all', action='store_true', help='sync all records')
        parserSync.add_argument('-dry', '--dry-run', action='store_true', help='dry run')

        return parser
    def parse(self):
        return self.parser.parse_args()