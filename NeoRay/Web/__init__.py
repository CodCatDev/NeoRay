#   _  _         ___           
#   | \| |___ ___| _ \__ _ _  _ 
#   | .` / -_) _ \   / _` | || |
#   |_|\_\___\___/_|_\__,_|\_, |
#                           |__/ 
#
#   NeoRay Web Server by CodCatDev
#
#   NeoRay.Web (__init__)

import NeoRay.Config
import NeoRay.Logger
from . import Setup

logger = NeoRay.Logger.MainLogger()

logger.log("Initializing NeoRay...")
print()
logger.log("Version: v" + NeoRay.Config.__VERSION__)
logger.log("Type: " + NeoRay.Config.__VERSION_TYPE__)
logger.log("Build Date: " + NeoRay.Config.__BUILD_DATE__)
print()
logger.log("Contributors: ")

for contributor in NeoRay.Config.__CONTRIBUTORS__:
    logger.log(f"    {contributor[0]} -  {contributor[1]}")
print()

Setup.Setup()

def RunServer(host: str, port: int) -> None:
    pass