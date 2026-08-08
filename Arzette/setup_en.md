
# Setup Guide for Arzette Archipelago (TODO)

## Patch the game files

- Find steam game folder. You can normally access it by clicking on the gear icon on the game's page in your Steam library, and clicking `Manage > Browse local files`. On Windows, it is normally located at `C:\Program Files (x86)\Steam\steamapps\common\Arzette The Jewel of Faramore`.

- Go to the game folder and patch the Arzette game files. You’ll need xDelta patcher to successfully patch the files. This [online version](https://kotcrab.github.io/xdelta-wasm/) will do the trick. Make a copy of `Arzette.exe`, `data.win` files and the `textures` folder. I recommend renaming them `Arzette_original.exe`, `data_original.win` and `textures_original`, respectively.

- TODO (get inspiration from [this](https://docs.google.com/document/d/1chXFJcNZCV5EQSQ2Rq8UeIWYM6ar3_pV7tq0N0AH8wU) once the steps are set up)

## Set-up the connection info

- Find the save files folder of the game. On Windows, it is normally located on `C:\Users\[USER]\AppData\Local\Arzette`.

- You do not need to back up your save file `savedata.ini`. The Archipelago save file will be separate as `savedata_rando.ini`.

- Upon booting the game, a pop-up will appear asking you for Archipelago connection information. This information will be saved under `apconfig.txt` in the save files folder. To change connection information, you can either press Y on the title screen, modify the `apconfig.txt` file or delete the `apconfig.txt` file and enter the new information when rebooting the game.

- Sometimes, the game will not boot if the connection information is wrong. If this is the case, delete the `apconfig.txt` file in the save files folder and try again.

## Uninstall

- To uninstall the mod, if you backed up your original files as directed during the mod installation, delete `Arzette.exe`, `data.win` and `textures` from the game folder and rename the `Arzette_original.exe` to `Arzette.exe`, `data_original.win` to `data.win` and `textures_original` to `textures`. The game should now revert to its vanilla state.