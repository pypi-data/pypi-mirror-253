#  Copyright (C) 2023 Y Hsu <yh202109@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public license as published by
#  the Free software Foundation, either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details
#
#  You should have received a copy of the GNU General Public license
#  along with this program. If not, see <https://www.gnu.org/license/>

import os
from mtbp3.util.lsr import LsrTree
import mtbp3

class Emt:
    """A class representing Emt (Electromagnetic Transmitter).

    This class provides methods to interact with the Emt object,
    including listing files associated with the Emt.

    Attributes:
        folder_name (str): The folder name associated with the Emt.
        lsr (LsrTree): An instance of the LsrTree class for listing files.
    """

    def __init__(self, folder_name=''):
        """
        Initialize a new Emt object.

        Args:
            folder_name (str, optional): The folder name associated with the Emt.
                If not provided, the default folder name will be used.
        """
        if folder_name:
            self.folder_name = folder_name
        else:
            self.folder_name = mtbp3.get_data('emt')
        self.lsr = LsrTree(self.folder_name, outfmt="tree")
    
    def list_files(self):
        """
        List all files associated with the Emt.

        Returns:
            list: A list of file names.
        """
        
        return self.lsr.list_files()

if __name__ == "__main__":
    emt = Emt()
    print("\n".join(emt.list_files()))

