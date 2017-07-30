# A Python program for determining land owners in EconomyLand PocketMine plugin
If you are a [PocketMine](https://github.com/PocketMine/PocketMine-MP) server administrator, and your server has [EconomyLand](https://github.com/onebone/EconomyS/tree/master/EconomyLand) installed,  sometimes you would like to clean up lands of players who quitted your server.   
Once you generate a list of players waiting to be deleted, this tiny Python program can help you find out players who have land on your server.

## Requirements
* EconomyLand v2.0.9
* Any GNU/Linux operating system

## Instructions
1. Download `LandCleanup.py`.
2. Obtain `Land.yml` (land list of EconomyLand) from `./plugins/Economyland` of PocketMine installation path, then put the file into the directory which stores `LandCleanup.py`.
3. Generate a list of players who have not logged in your server for more than `x` days. Execute **find -mtime +`x` |xargs ls > cleanup.txt** in `./players` of PocketMine installation path.
4. Obtain `cleanup.txt`, then put the file into the directory which stores `LandCleanup.py`.
5. Run `LandCleanup.py`. The list of players who lave land will generate in `hasland.txt` in the same directory.

## License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.   
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.   
You should have received a copy of the GNU General Public License along with this program. If not, click [here] (http://www.gnu.org/licenses/).
