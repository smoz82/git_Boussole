"""
Functions :
__init__(port, addr=0x1e, gauss=1.3)

Constructor to create instance requires the port (0 for old raspberry pi, 1 for new). If the rest are not provided, defaults are used.

__str__

Prints the axes, declination and heading to screen for quick troubleshooting

setContinuousMode()

Axes are constantly updated

setScale(gauss)

Set scale for axes. Gauss must be 0.88, 1.3, 1.9, 2.5, 4.0, 4.7, 5.6, or 8.1

setDeclination(degrees, minutes=0)

Sets declination to allow heading compensation to true north. Minutes are optional. See declination section above for more information.

setOption(register, options)

Sets options in hex in provided register

getDeclination()

Returns tuple with declination in degrees and minutes.

getDeclinationString()

Returns string with declination in standard format

getHeading()

Returns tuple with heading in degrees and minutes.

getHeadingString()

Returns string with heading in standard format

getAxes()

Returns tuple with scaled axes for x, y and z
"""


# Premier example

from i2clibraries import i2c_hmc5883l
 
hmc5883l = i2c_hmc5883l.i2c_hmc5883l(0)
 
hmc5883l.setContinuousMode()
hmc5883l.setDeclination(9,54)
 
print(hmc5883l)

# Deuxieme example
"""
from i2clibraries import i2c_hmc5883l

hmc5883l = i2c_hmc5883l.i2c_hmc5883l(0)

hmc5883l.setContinuousMode()
hmc5883l.setDeclination(9,54)

# To get degrees and minutes into variables
(degrees, minutes) = hmc5883l.getDeclination()
(degress, minutes) = hmc5883l.getHeading()

# To get string of degrees and minutes
declination = hmc5883l.getDeclinationString()
heading = hmc5883l.getHeadingString()
"""

# Troisieme example
"""
from i2clibraries import i2c_hmc5883l
 
hmc5883l = i2c_hmc5883l.i2c_hmc5883l(0)
 
hmc5883l.setContinuousMode()
 
# To scaled axes
(x, y, z) = hmc5883l.getAxes()
"""






