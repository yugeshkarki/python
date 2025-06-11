
def https_status(status):
    match status:
        case 200:
            return "OK"
    
        case 404:
            return "Not found"
        
        case _:
            return "unkown Status"
print(https_status(404))