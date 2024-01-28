from wizlib.parser import WizParser

from filez4eva.command import Filez4EvaCommand
from filez4eva.directory_scanner import DirectoryScanner
from filez4eva.file_mover import FileMover


class ScanCommand(Filez4EvaCommand):
    """Handle files from a directory"""

    name = 'scan'

    @Filez4EvaCommand.wrap
    def execute(self):
        sourcedir = self.config.get('filez4eva-source')
        targetdir = self.config.get('filez4eva-target')
        scanner = DirectoryScanner(sourcedir)
        mover = FileMover(targetdir)
        scanner.loop_directory(mover)
        self.status = 'Done'
