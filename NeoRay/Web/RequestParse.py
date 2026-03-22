#   _  _         ___           
#   | \| |___ ___| _ \__ _ _  _ 
#   | .` / -_) _ \   / _` | || |
#   |_|\_\___\___/_|_\__,_|\_, |
#                           |__/ 
#
#   NeoRay Web Server by CodCatDev

def reqParse(req):
    data = []
    lines = 0
    for l in req.splitlines():
        lines += 1
        if l.startswith("GET") and lines == 1:
            data.append(l.split(" "))
        elif lines == 1:
            return {
                "type":"err",
                "code":405
            }
        data.append(l.split(": "))
    print(data)
    path = data[0][1]
    host = data[1][1]
    userAgent = data[2][1]