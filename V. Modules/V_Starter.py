'''
V. Modules
----------
Predix Python Learning Series
GE Digital Shanghai
'''

### Standard package sys ###

# Import sys
import ___
# Print sys.path, which will return the list of locations that the system path could import from.
print(___)
# Append another path onto the sys.path, so you can import files/modules from that location.
sys.path.append(___)
print(___)


### Custom module, hi_Mod ###

# Import hi_Mod
import ___
# Import hi_Mod and save it under a new variable.
import ___ as _
# Call the hi and hi2 functions inside hi_Mod, with the arguments "bread" and "eggs" respectively.
___("bread")
___("eggs")
# Directly import the hi, hi2 function from hi_Mod
from ____ import ___
# Call the hi and hi2 functions directly, again with the arguments "bread" and "eggs" respectively.
___("bread")
___("eggs")

### Import your own module! ###

# Import module and save it under a new variable.
import ___
# Call some functions with your own arguments and have some fun with it!
