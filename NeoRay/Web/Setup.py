#   _  _         ___           
#   | \| |___ ___| _ \__ _ _  _ 
#   | .` / -_) _ \   / _` | || |
#   |_|\_\___\___/_|_\__,_|\_, |
#                           |__/ 
#
#   NeoRay Web Server by CodCatDev
#
#   NeoRay.Web.Setup

import os
import NeoRay.Logger
import NeoRay.Config

def Setup() -> None:
    """
    Setup NeoRay (Create/Check dirs, libs and etc.)
    """
    logger = NeoRay.Logger.MainLogger("Setup")
    if os.path.exists("WWW") == False:
        logger.log("Setup NeoRay...")
        os.mkdir("WWW")
        with open("NeoRay/Templates/index.NRtm.html", "r") as f:
            index = f.read()
        
        index = index.replace("{version}", NeoRay.Config.__VERSION__)
        index = index.replace("{versionType}", NeoRay.Config.__VERSION_TYPE__)
        index = index.replace("{buildDate}", NeoRay.Config.__BUILD_DATE__)
        with open("WWW/index.html", "w") as f:
            f.write(index)