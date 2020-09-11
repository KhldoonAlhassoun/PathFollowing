from Robot import *
from Path import *
from ShowPath import *
import math


# load a path file
p = Path("Path-around-table.json")
path = p.getPath()

# plot the path
sp = ShowPath(path)

print("Path length = " + str(len(path)))
print("First point = " + str(path[0]['X']) + ", " + str(path[0]['Y']))

# make a robot to move around
robot = Robot()

#lerp(robotPosition, goalPoint)


goalPoint = path[-1]
robotPosition = robot.getPosition()
robotHeading = robot.getHeading()

xPrimeRCS= ((goalPoint['X'] - robotPosition['X']) * cos(robotHeading)) + ((goalPoint['Y'] - robotPosition['Y']) * sin(robotHeading))

yPrimeRCS= -((goalPoint['X'] - robotPosition['X']) * sin(robotHeading)) + ((goalPoint['Y'] - robotPosition['Y']) * cos(robotHeading))

#goalPointLacalPos = _vector2Subtract(robotPosition, goalPoint)
goalPointFound = False
lookAheadVector = 1

DistanceVector = math.sqrt((xPrimeRCS **2) + (yPrimeRCS ** 2))
goalAngel = math.atan2(xPrimeRCS,yPrimeRCS)


#def lerp(v1, v2, distance):


# move the robot

robot.setMotion(0.2, 0.2)

while goalPointFound == False:
    for i, in path.  :
    time.sleep(0.5)
    print("pos, heading")
    print(robot.getPosition())
    print(robot.getHeading())
    
    # Plot the current position and the look-ahead point:
    #just a dummy point that moves 
    
    
    sp.update(robot.getPosition(), lookAheadVector)

    

 
    
goalPointFound = robotPosition == goalPoint

echoes = robot.getLaser()
print(echoes)

# the last item of the path sequence GoalPoint.
# define distance between robot and goalPoint.



def _vector2Subtract(v1, v2):    
    v={}
    v["X"]=v1["X"] -v2["X"]
    v["Y"]=v1["Y"] -v2["Y"]

    return v



# Returns the current laser scan
# laser['Echoes'][271]

# Returns information about the laser configuration, such as angle between each laser beam in the scan. This information usually does not change and may hence be read only once at program startup.

# {"AngleIncrement":0.017388889566063881,"EndAngle":2.3561944961547852,"Pose":{"Orientation":{"W":1,"X":0,"Y":0,"Z":0},"Position":{"X":0.15,"Y":0,"Z":0.2}},"StartAngle":-2.3561944961547852}

