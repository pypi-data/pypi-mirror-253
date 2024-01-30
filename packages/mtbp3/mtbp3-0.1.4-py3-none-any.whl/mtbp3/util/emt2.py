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
import shutil

def generate_meddra(folder_path):
    """
    Create a mock MedDRA data folder with sample files.

    Args:
        folder_path (str): The path to the folder where the mock MedDRA data folder will be created.
    """
    # Create the main MedDRA data folder
    meddra_folder = os.path.join(folder_path, "MedDRA")
    os.makedirs(meddra_folder)

    # Create subfolders for different versions
    version_folders = ["26.0", "26.1"]
    for version in version_folders:
        version_folder = os.path.join(meddra_folder, version)
        os.makedirs(version_folder)

        # Create sample files in each version folder
        sample_files = ["PT.csv", "LLT.csv", "HLT.csv", "HLGT.csv"]
        for file in sample_files:
            file_path = os.path.join(version_folder, file)
            with open(file_path, "w") as f:
                f.write("Sample data for " + file)

    print("Mock MedDRA data folder created successfully.")

# Example usage:

if __name__ == "__main__":
    generate_meddra("data")
    emt = Emt()
    print("\n".join(emt.list_files()))

