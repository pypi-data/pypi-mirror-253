from pathlib import Path
import shutil
import filecmp
import os

class SyncEngine:
    def __init__(self):
        pass

    # filter out items in src different from dest
    # items are composed of different files and src only dirs
    def _filter(self, src, dest, update=True):
        src = Path(src)
        dest = Path(dest)
        assert src.exists() and dest.exists()
        assert src.is_dir() and dest.is_dir()
        assert src.is_absolute() and dest.is_absolute()

        srcFiles = set([(dirPath / file).relative_to(src) for dirPath, _, files in src.walk() for file in files])
        destFiles = set([(dirPath / file).relative_to(dest) for dirPath, _, files in dest.walk() for file in files])
        srcDirs = set([(dirPath / dir).relative_to(src) for dirPath, dirs, _ in src.walk() for dir in dirs])
        destDirs = set([(dirPath / dir).relative_to(dest) for dirPath, dirs, _ in dest.walk() for dir in dirs])
        diffItems = dict()
        diffItems["DiffFiles"] = srcFiles - destFiles
        diffItems["dirs"] = srcDirs - destDirs
        diffItems["CommonFiles"] = set()
        commonItems = srcFiles & destFiles
        if update:
            for item in commonItems:
                if not filecmp.cmp(src/item, dest/item):
                    diffItems["CommonFiles"].add(item)
        return diffItems

    def getDiffItems(self, src, dest, mode):
        assert mode in ['two-way', 'src-to-dest', 'dest-to-src']
        if mode == 'two-way':
            return {"src-to-dest": self._filter(src, dest, False), "dest-to-src": self._filter(dest, src, False)}
        elif mode == 'src-to-dest':
            return {"src-to-dest": self._filter(src, dest)}
        elif mode == 'dest-to-src':
            return {"dest-to-src": self._filter(dest, src)}

    def sync(self, src, dest, mode, dryRun=False):
        assert mode in ['two-way', 'src-to-dest', 'dest-to-src']
        diffItems = self.getDiffItems(src, dest, mode)
        for key, items in diffItems.items():
            srcLabel = key.split('-')[0]
            destLabel = key.split('-')[2]
            srcPath = src if srcLabel == 'src' else dest
            destPath = dest if destLabel == 'dest' else src
            for dir in items["dirs"]:
                print(f"{srcLabel}->{destLabel} CREATE DIR: ${destLabel}{os.sep}{dir}")
                if not dryRun:
                    (destPath/dir).mkdir(parents=True, exist_ok=True)
            for file in items["DiffFiles"]:
                print(f"{srcLabel}->{destLabel} CREATE FILE: ${destLabel}{os.sep}{file}")
                if not dryRun:
                    shutil.copy2(srcPath/file, destPath/file)
            for file in items["CommonFiles"]:
                print(f"{srcLabel}->{destLabel} UPDATE FILE: ${destLabel}{os.sep}{file}")
                if not dryRun:
                    shutil.copy2(srcPath/file, destPath/file)