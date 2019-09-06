from flask_sqlalchemy import SQLAlchemy


# ############################################################################
# AUDIT DATA
# ############################################################################

# Audit Data
# ----------------------------------------------------------------------------
class _AuditData (appDB.Model):
    _dateCreated = appDB.Column(appDB.datetime.datetime, nullable=False)
    _dateLastUpdated = appDB.Column(appDB.datetime.datetime, nullable=True)
    _userCreated = appDB.Column(appDB.String(50), nullable=False)
    _userLastUpdated = appDB.Column(appDB.String(50), nullable=True)
# ----------------------------------------------------------------------------


# ############################################################################
# VALUE CHAIN
# ############################################################################

# Data Component
# ----------------------------------------------------------------------------
class CFG_DataComponent (AuditData, appDB.Model):
    def __init__(self, DataComponentId, DataComponentName, DataComponentDescription):
        self.DataComponentId = DataComponentId
        self.DataComponentName = DataComponentName
        self.DataComponentDescription = DataComponentDescription

    DataComponentId = appDB.Column(appDB.String(20), primary_key=True)
    DataComponentName = appDB.Column(appDB.String(255), unique=True, nullable=False)
    DataComponentDescription = appDB.Column(appDB.TEXT, nullable=False)


# Data Item
# ----------------------------------------------------------------------------
class CFG_DataItem (AuditData, appDB.Model):
    def __init__(self, DataItemId, DataItemName, DataItemDescription):
        self.DataItemId = DataItemId
        self.DataItemName = DataItemName
        self.DataItemDescription = DataItemDescription

    DataItemId = appDB.Column(appDB.String(20), primary_key=True)
    DataItemName = appDB.Column(appDB.String(255), unique=True, nullable=False)
    DataItemDescription = appDB.Column(appDB.TEXT, nullable=False)
# ----------------------------------------------------------------------------


# ############################################################################
# DATA MODEL
# ############################################################################

# Data Entity
# ----------------------------------------------------------------------------
class CFG_DataEntity (AuditData, appDB.Model):
    DataEntityId = appDB.Column(appDB.varchar(255), primary_key=True)


# Data Entity Attribute
# ----------------------------------------------------------------------------
class CFG_DataEntityAttribute (AuditData, appDB.Model):
    DataEntityAttributeId = appDB.Column(appDB.varchar(20), primary_key=True)
# ----------------------------------------------------------------------------


# ############################################################################
if __name__ == '__main__':
    responseText = 'Please execute this application using the main application file.'
    print (responseText)