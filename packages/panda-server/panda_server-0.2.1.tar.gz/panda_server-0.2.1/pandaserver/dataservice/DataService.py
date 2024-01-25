"""
provide web service for DDM

"""

import sys

from pandacommon.pandalogger.PandaLogger import PandaLogger
from pandaserver.dataservice.DDMHandler import DDMHandler
from pandaserver.taskbuffer.WrappedPickle import WrappedPickle

# logger
_logger = PandaLogger().getLogger("DataService")


class DataService:
    # constructor
    def __init__(self):
        self.taskBuffer = None

    # set taskbuffer
    def init(self, taskBuffer):
        self.taskBuffer = taskBuffer


# Singleton
dataService = DataService()
del DataService


"""
web interface

"""


# callback for dataset verification
def datasetCompleted(req, vuid, site=None):
    thr = DDMHandler(dataService.taskBuffer, vuid, site)
    thr.start()
    thr.join()
    return True


# get FQANs
def _getFQAN(req):
    fqans = []
    for tmpKey in req.subprocess_env:
        tmpVal = req.subprocess_env[tmpKey]
        # compact credentials
        if tmpKey.startswith("GRST_CRED_"):
            # VOMS attribute
            if tmpVal.startswith("VOMS"):
                # FQAN
                fqan = tmpVal.split()[-1]
                # append
                fqans.append(fqan)
        # old style
        elif tmpKey.startswith("GRST_CONN_"):
            tmpItems = tmpVal.split(":")
            # FQAN
            if len(tmpItems) == 2 and tmpItems[0] == "fqan":
                fqans.append(tmpItems[-1])
    # return
    return fqans


# set file status
def updateFileStatusInDisp(req, dataset, fileStatus):
    try:
        # get FQAN
        fqans = _getFQAN(req)
        roleOK = False
        # loop over all FQANs
        for fqan in fqans:
            # check production role
            for rolePat in [
                "/atlas/usatlas/Role=production",
                "/atlas/Role=production",
                # use /atlas since delegation proxy doesn't inherit roles
                "/atlas/",
            ]:
                if fqan.startswith(rolePat):
                    roleOK = True
                    break
        if not roleOK:
            _logger.error(f"updateFileStatusInDisp : invalid proxy {fqans}")
            return "False"
        # deserialize fileStatus
        fileStatusMap = WrappedPickle.loads(fileStatus)
        _logger.debug(f"updateFileStatusInDisp : start {dataset} - {fileStatusMap}")
        # update status
        dataService.taskBuffer.updateFileStatusInDisp(dataset, fileStatusMap)
        _logger.debug("updateFileStatusInDisp : done")
        return "True"
    except Exception:
        type, value, traceBack = sys.exc_info()
        _logger.error(f"updateFileStatusInDisp : {type} {value}")
        return "False"
