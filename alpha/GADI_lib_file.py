import glob
import sys

global dbTableFlows
global dbTableTasks
global dbProvider
global dbServer
global dbUser
global dbName

# ----------------------------------------------
# Open parameters file
# ----------------------------------------------
def OpenParametersFile() :
	import json
	FilePath = 'dbGADI.json'
	with open(FilePath) as f:
	    data = json.load(f)
	    return data
# ----------------------------------------------


# ----------------------------------------------
# Get JSON data
# ----------------------------------------------
def GetJSONValue(JSONObject, JSONGroup, JSONElement) :
	return JSONObject[JSONGroup][JSONElement]
# ----------------------------------------------

# ----------------------------------------------
# GET PARAMETERS FROM FILE
# ----------------------------------------------
def GetParametersFromFileBACKUP():

	# Get parameters from external JSON file
	JSONData = OpenParametersFile()

	# Database service provider
	dbProvider = GetJSONValue(JSONData, "ACDDatabase", "dbProvider")
	# Server name or IP address
	dbServer = GetJSONValue(JSONData, "ACDDatabase", "dbServer")
	# Database user name
	dbUser = GetJSONValue(JSONData, "ACDDatabase", "dbUser")
	# Database name, without brackets
	dbName = GetJSONValue(JSONData, "ACDDatabase", "dbName")

	# Table to save the process flows
	dbTableFlows = GetJSONValue(JSONData, "ACDDatabase", "dbTableFlows")

	# Table to save the process tasks
	dbTableTasks = GetJSONValue(JSONData, "ACDDatabase", "dbTableTasks")
# ----------------------------------------------


# ----------------------------------------------
# GET PARAMETERS FROM FILE
# ----------------------------------------------
def GetParametersFromFile():

	ACDparameters = {}

	# Get parameters from external JSON file
	JSONData = OpenParametersFile()

	# Database service provider
	ACDparameters.update ( {"dbProvider":GetJSONValue(JSONData, "ACDDatabase", "dbProvider")} )

	# Server name or IP address
	ACDparameters.update ( {"dbServer":GetJSONValue(JSONData, "ACDDatabase", "dbServer")} )

	# Database user name
	ACDparameters.update ( {"dbUser":GetJSONValue(JSONData, "ACDDatabase", "dbUser")} )

	# Database name, without brackets
	ACDparameters.update ( {"dbName":GetJSONValue(JSONData, "ACDDatabase", "dbName")} )

	# Table to save the process flows
	ACDparameters.update ( {"dbTableFlows":GetJSONValue(JSONData, "ACDDatabase", "dbTableFlows")} )

	# Table to save the process tasks
	ACDparameters.update ( {"dbTableTasks":GetJSONValue(JSONData, "ACDDatabase", "dbTableTasks")} )

	return ACDparameters
# ----------------------------------------------
