#   _  _         ___           
#   | \| |___ ___| _ \__ _ _  _ 
#   | .` / -_) _ \   / _` | || |
#   |_|\_\___\___/_|_\__,_|\_, |
#                           |__/ 
#
#   NeoRay Web Server by CodCatDev

import NeoRay.Web
import NeoRay.Web.BaseSetup

NeoRay.Web.BaseSetup.CheckSetup()
NeoRay.Web.RunServer('0.0.0.0', 80)