from zsync.CLI import CLI
from zsync.Config import Config
from zsync.SyncEngine import SyncEngine
import tqdm
from time import sleep

print = tqdm.tqdm.write

def recordToString(record):
    symbol = '<->' if record[2] == 'two-way' else '->' if record[2] == 'src-to-dest' else '<-' if record[2] == 'dest-to-src' else '??'
    return f'{record[0]} {symbol} {record[1]} ({record[2]})'
def addRecord(config, args):
    config.addRecord(args.source, args.destination, args.mode)
    print(f'Successfully added record: {recordToString(config.getRecords()[-1])}')


def listRecords(config, args):
    for i, record in enumerate(config.getRecords()):
        print(f'{i}: {recordToString(record)}')

def removeRecord(config, args):
    config.removeRecord(args.index)
    print(f'Successfully removed record {args.index}')

def sync(engine, config, args):
    index = args.index if args.index else list(range(len(config.getRecords())))
    for i in tqdm.tqdm(index):
        print(f'Syncing record {i}: {recordToString(config.getRecords()[i])}')
        record = config.getRecords()[i]
        engine.sync(record[0], record[1], record[2], args.dry_run)

def main():
    config = Config()
    cli = CLI()
    args = cli.parse()
    engine = SyncEngine()
    if args.command == 'add':
        addRecord(config, args)
    elif args.command == 'list':
        listRecords(config, args)
    elif args.command == 'remove':
        removeRecord(config, args)
    elif args.command == 'sync':
        sync(engine, config, args)



if __name__ == '__main__':
    main()
