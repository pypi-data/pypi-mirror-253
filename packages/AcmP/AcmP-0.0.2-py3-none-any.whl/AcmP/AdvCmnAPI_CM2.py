from AcmP.AdvMotApi_CM2 import *
from AcmP.MotionInfo import *
from AcmP.AdvMotDrv import *
import os

if os.name == 'nt':
    lib = CDLL(r'C:\Windows\System32\ADVMOT.dll')
else:
    lib = CDLL('/usr/lib/libadvmot.so')

class AdvCmnAPI_CM2:
# Device
    try:
        Acm2_DevOpen = lib.Acm2_DevOpen
        Acm2_DevOpen.argtypes = [c_uint32, POINTER(DEVICEINFO)]
        Acm2_DevOpen.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevInitialize = lib.Acm2_DevInitialize
        Acm2_DevInitialize.restype = c_uint32
    except:
        pass

    try:
        Acm2_GetAvailableDevs = lib.Acm2_GetAvailableDevs
        Acm2_GetAvailableDevs.argtypes = [POINTER(DEVLIST), c_uint32, POINTER(c_uint32)]
        Acm2_GetAvailableDevs.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevExportMappingTable = lib.Acm2_DevExportMappingTable
        Acm2_DevExportMappingTable.argtypes = [c_char_p]
        Acm2_DevExportMappingTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevImportMappingTable = lib.Acm2_DevImportMappingTable
        Acm2_DevImportMappingTable.argtypes = [c_char_p]
        Acm2_DevImportMappingTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_GetMappedPhysicalID = lib.Acm2_GetMappedPhysicalID
        Acm2_GetMappedPhysicalID.argtypes = [c_int, c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_GetMappedPhysicalID.restype = c_uint32
    except:
        pass
    
    try:
        Acm2_GetMappedLogicalIDList = lib.Acm2_GetMappedLogicalIDList
        Acm2_GetMappedLogicalIDList.argtypes = [c_int, c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_GetMappedLogicalIDList.restype = c_uint32
    except:
        pass

    try:
        Acm2_GetMappedObjInfo = lib.Acm2_GetMappedObjInfo
        Acm2_GetMappedObjInfo.argtypes = [c_int, c_uint32, c_void_p]
        Acm2_GetMappedObjInfo.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevAllClose = lib.Acm2_DevAllClose
        Acm2_DevAllClose.restype = c_uint32
    except:
        pass

    try:
        Acm2_GetLastError = lib.Acm2_GetLastError
        Acm2_GetLastError.argtypes = [c_uint, c_uint32]
        Acm2_GetLastError.restype = c_uint32
    except:
        pass

    try:
        Acm2_GetProperty = lib.Acm2_GetProperty
        Acm2_GetProperty.argtypes = [c_uint32, c_uint32, POINTER(c_double)]
        Acm2_GetProperty.restype = c_uint32
    except:
        pass

    try:
        Acm2_SetProperty = lib.Acm2_SetProperty
        Acm2_SetProperty.argtypes = [c_uint32, c_uint32, c_double]
        Acm2_SetProperty.restype = c_uint32
    except:
        pass

    try:
        Acm2_SetMultiProperty = lib.Acm2_SetMultiProperty
        Acm2_SetMultiProperty.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_double), c_uint32, POINTER(c_uint32)]
        Acm2_SetMultiProperty.restype = c_uint32
    except:
        pass

    try:
        Acm2_GetMultiProperty = lib.Acm2_GetMultiProperty
        Acm2_GetMultiProperty.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_double), c_uint32, POINTER(c_uint32)]
        Acm2_GetMultiProperty.restype = c_uint32
    except:
        pass

    try:
        Acm2_GetRawProperty = lib.Acm2_GetRawProperty
        Acm2_GetRawProperty.argtypes = [c_uint32, c_uint32, c_void_p, POINTER(c_uint32)]
        Acm2_GetRawProperty.restype = c_uint32
    except:
        pass

    try:
        Acm2_EnableCallBackFuncForOneEvent = lib.Acm2_EnableCallBackFuncForOneEvent
        Acm2_EnableCallBackFuncForOneEvent.argtypes = [c_uint32, c_int, CFUNCTYPE(c_uint32, c_uint32, c_void_p)]
        Acm2_EnableCallBackFuncForOneEvent.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevLoadAllConfig = lib.Acm2_DevLoadAllConfig
        Acm2_DevLoadAllConfig.argtypes = [c_char_p]
        Acm2_DevLoadAllConfig.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevLoadConfig = lib.Acm2_DevLoadConfig
        Acm2_DevLoadConfig.argtypes = [c_uint32, c_char_p]
        Acm2_DevLoadConfig.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevReadMailBox = lib.Acm2_DevReadMailBox
        Acm2_DevReadMailBox.argtypes = [c_uint, c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_DevReadMailBox.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevWriteMailBox = lib.Acm2_DevWriteMailBox
        Acm2_DevWriteMailBox.argtypes = [c_uint, c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_DevWriteMailBox.restype = c_uint32
    except:
        pass

    try:
        Acm2_GetErrors = lib.Acm2_GetErrors
        Acm2_GetErrors.argtypes = [c_uint32, c_void_p, POINTER(c_uint32)]
        Acm2_GetErrors.restype = c_uint32
    except:
        pass

    try:
        Acm2_ResetErrorRecord = lib.Acm2_ResetErrorRecord
        Acm2_ResetErrorRecord.argtypes = [c_uint32]
        Acm2_ResetErrorRecord.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevPreviewMotion = lib.Acm2_DevPreviewMotion
        Acm2_DevPreviewMotion.argtypes = [c_uint32, c_char_p, c_char_p, c_uint16]
        Acm2_DevPreviewMotion.restype = c_uint32
    except:
        pass
# Axis
    try:
        Acm2_AxReturnPausePosition = lib.Acm2_AxReturnPausePosition
        Acm2_AxReturnPausePosition.argtypes = [c_uint32]
        Acm2_AxReturnPausePosition.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSetSvOn = lib.Acm2_AxSetSvOn
        Acm2_AxSetSvOn.argtypes = [c_uint32, c_uint]
        Acm2_AxSetSvOn.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevSetAllSvOn = lib.Acm2_DevSetAllSvOn
        Acm2_DevSetAllSvOn.argtypes = [c_uint]
        Acm2_DevSetAllSvOn.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSetErcOn = lib.Acm2_AxSetErcOn
        Acm2_AxSetErcOn.argtypes = [c_uint32, c_uint]
        Acm2_AxSetErcOn.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxResetAlm = lib.Acm2_AxResetAlm
        Acm2_AxResetAlm.argtypes = [c_uint32, c_uint]
        Acm2_AxResetAlm.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxPTP = lib.Acm2_AxPTP
        Acm2_AxPTP.argtypes = [c_uint32, c_uint, c_double]
        Acm2_AxPTP.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxMoveContinue = lib.Acm2_AxMoveContinue
        Acm2_AxMoveContinue.argtypes = [c_uint32, c_uint]
        Acm2_AxMoveContinue.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxMotionStop = lib.Acm2_AxMotionStop
        Acm2_AxMotionStop.argtypes = [POINTER(c_uint32), c_uint32, c_uint, c_double]
        Acm2_AxMotionStop.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxHome = lib.Acm2_AxHome
        Acm2_AxHome.argtypes = [c_uint32, c_uint, c_uint]
        Acm2_AxHome.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxMoveGantryHome = lib.Acm2_AxMoveGantryHome
        Acm2_AxMoveGantryHome.argtypes = [c_uint32, c_uint, c_uint]
        Acm2_AxMoveGantryHome.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSetHomeSpeedProfile = lib.Acm2_AxSetHomeSpeedProfile
        Acm2_AxSetHomeSpeedProfile.argtypes = [c_uint32, SPEED_PROFILE_PRM]
        Acm2_AxSetHomeSpeedProfile.restype = c_uint32
    except:
        pass
    
    try:
        Acm2_AxChangePos = lib.Acm2_AxChangePos
        Acm2_AxChangePos.argtypes = [c_uint32, c_double]
        Acm2_AxChangePos.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxChangeVel = lib.Acm2_AxChangeVel
        Acm2_AxChangeVel.argtypes = [c_uint32, c_double, c_double, c_double]
        Acm2_AxChangeVel.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxChangeVelByRate = lib.Acm2_AxChangeVelByRate
        Acm2_AxChangeVelByRate.argtypes = [c_uint32, c_uint32, c_double, c_double]
        Acm2_AxChangeVelByRate.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxMoveImpose = lib.Acm2_AxMoveImpose
        Acm2_AxMoveImpose.argtypes = [c_uint32, c_double, c_double]
        Acm2_AxMoveImpose.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxResetError = lib.Acm2_AxResetError
        Acm2_AxResetError.argtypes = [c_uint32]
        Acm2_AxResetError.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevResetAllError = lib.Acm2_DevResetAllError
        Acm2_DevResetAllError.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGetState = lib.Acm2_AxGetState
        Acm2_AxGetState.argtypes = [c_uint32, c_uint, POINTER(c_uint32)]
        Acm2_AxGetState.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGetMotionIO = lib.Acm2_AxGetMotionIO
        Acm2_AxGetMotionIO.argtypes = [c_uint32, POINTER(MOTION_IO)]
        Acm2_AxGetMotionIO.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSetPosition = lib.Acm2_AxSetPosition
        Acm2_AxSetPosition.argtypes = [c_uint32, c_uint, c_double]
        Acm2_AxSetPosition.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGetPosition = lib.Acm2_AxGetPosition
        Acm2_AxGetPosition.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        Acm2_AxGetPosition.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGetMachPosition = lib.Acm2_AxGetMachPosition
        Acm2_AxGetMachPosition.argtypes = [c_uint32, POINTER(c_double)]
        Acm2_AxGetMachPosition.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSetSpeedProfile = lib.Acm2_AxSetSpeedProfile
        Acm2_AxSetSpeedProfile.argtypes = [c_uint32, SPEED_PROFILE_PRM]
        Acm2_AxSetSpeedProfile.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGetVel = lib.Acm2_AxGetVel
        Acm2_AxGetVel.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        Acm2_AxGetVel.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxEnableExternalMode = lib.Acm2_AxEnableExternalMode
        Acm2_AxEnableExternalMode.argtypes = [c_uint32, c_uint]
        Acm2_AxEnableExternalMode.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSoftJog = lib.Acm2_AxSoftJog
        Acm2_AxSoftJog.argtypes = [c_uint32, c_uint]
        Acm2_AxSoftJog.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSetJogSpeedProfile = lib.Acm2_AxSetJogSpeedProfile
        Acm2_AxSetJogSpeedProfile.argtypes = [c_uint32, JOG_SPEED_PROFILE_PRM]
        Acm2_AxSetJogSpeedProfile.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxMotionStart = lib.Acm2_AxMotionStart
        Acm2_AxMotionStart.argtypes = [c_uint32, c_uint32]
        Acm2_AxMotionStart.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxPause = lib.Acm2_AxPause
        Acm2_AxPause.argtypes = [c_uint32]
        Acm2_AxPause.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxResume = lib.Acm2_AxResume
        Acm2_AxResume.argtypes = [c_uint32]
        Acm2_AxResume.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxResetPVTTable = lib.Acm2_AxResetPVTTable
        Acm2_AxResetPVTTable.argtypes = [c_uint32]
        Acm2_AxResetPVTTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxLoadPVTTable = lib.Acm2_AxLoadPVTTable
        Acm2_AxLoadPVTTable.argtypes = [c_uint32, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint32]
        Acm2_AxLoadPVTTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxLoadPVTTableContinuous = lib.Acm2_AxLoadPVTTableContinuous
        Acm2_AxLoadPVTTableContinuous.argtypes = [c_uint32, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double, c_uint32]
        Acm2_AxLoadPVTTableContinuous.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxMovePVT = lib.Acm2_AxMovePVT
        Acm2_AxMovePVT.argtypes = [c_uint32]
        Acm2_AxMovePVT.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxCheckPTBuffer = lib.Acm2_AxCheckPTBuffer
        Acm2_AxCheckPTBuffer.argtypes = [c_uint32, POINTER(c_uint32)]
        Acm2_AxCheckPTBuffer.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxAddPTData = lib.Acm2_AxAddPTData
        Acm2_AxAddPTData.argtypes = [c_uint32, c_double, c_double]
        Acm2_AxAddPTData.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxMovePT = lib.Acm2_AxMovePT
        Acm2_AxMovePT.argtypes = [c_uint32]
        Acm2_AxMovePT.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxResetPTData = lib.Acm2_AxResetPTData
        Acm2_AxResetPTData.argtypes = [c_uint32]
        Acm2_AxResetPTData.restype = c_uint32
    except:
        pass
# Follow
    try:
        Acm2_AxGearIn = lib.Acm2_AxGearIn
        Acm2_AxGearIn.argtypes = [c_uint32, c_uint32, GEAR_IN_PRM]
        Acm2_AxGearIn.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGantryIn = lib.Acm2_AxGantryIn
        Acm2_AxGantryIn.argtypes = [c_uint32, c_uint32, GANTRY_IN_PRM]
        Acm2_AxGantryIn.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxPhaseAx = lib.Acm2_AxPhaseAx
        Acm2_AxPhaseAx.argtypes = [c_uint32, PHASE_AXIS_PRM]
        Acm2_AxPhaseAx.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSyncOut = lib.Acm2_AxSyncOut
        Acm2_AxSyncOut.argtypes = [c_uint32]
        Acm2_AxSyncOut.restype = c_uint32
    except:
        pass

# Group
    try:
        Acm2_GpGetPausePosition = lib.Acm2_GpGetPausePosition
        Acm2_GpGetPausePosition.argtypes = [c_uint32, POINTER(c_double)]
        Acm2_GpGetPausePosition.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpCreate = lib.Acm2_GpCreate
        Acm2_GpCreate.argtypes = [c_uint32, POINTER(c_uint32), c_uint32]
        Acm2_GpCreate.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpGetAxesInGroup = lib.Acm2_GpGetAxesInGroup
        Acm2_GpGetAxesInGroup.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_GpGetAxesInGroup.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpResetError = lib.Acm2_GpResetError
        Acm2_GpResetError.argtypes = [c_uint32]
        Acm2_GpResetError.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpLine = lib.Acm2_GpLine
        Acm2_GpLine.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_uint32)]
        Acm2_GpLine.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpArc_Center = lib.Acm2_GpArc_Center
        Acm2_GpArc_Center.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        Acm2_GpArc_Center.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpArc_3P = lib.Acm2_GpArc_3P
        Acm2_GpArc_3P.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        Acm2_GpArc_3P.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpArc_Angle = lib.Acm2_GpArc_Angle
        Acm2_GpArc_Angle.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_uint32), c_double, c_uint]
        Acm2_GpArc_Angle.restype = c_uint32
    except:
        pass

    try:
        Acm2_Gp3DArc_Center = lib.Acm2_Gp3DArc_Center
        Acm2_Gp3DArc_Center.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        Acm2_Gp3DArc_Center.restype = c_uint32
    except:
        pass

    try:
        Acm2_Gp3DArc_NormVec = lib.Acm2_Gp3DArc_NormVec
        Acm2_Gp3DArc_NormVec.argtypese = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_float), c_double, c_uint]
        Acm2_Gp3DArc_NormVec.restype = c_uint32
    except:
        pass

    try:
        Acm2_Gp3DArc_3P = lib.Acm2_Gp3DArc_3P
        Acm2_Gp3DArc_3P.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint, c_uint32]
        Acm2_Gp3DArc_3P.restype = c_uint32
    except:
        pass

    try:
        Acm2_Gp3DArc_3PAngle = lib.Acm2_Gp3DArc_3PAngle
        Acm2_Gp3DArc_3PAngle.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_double, c_uint]
        Acm2_Gp3DArc_3PAngle.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpHelix_Center = lib.Acm2_GpHelix_Center
        Acm2_GpHelix_Center.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        Acm2_GpHelix_Center.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpHelix_3P = lib.Acm2_GpHelix_3P
        Acm2_GpHelix_3P.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        Acm2_GpHelix_3P.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpHelix_Angle = lib.Acm2_GpHelix_Angle
        Acm2_GpHelix_Angle.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        Acm2_GpHelix_Angle.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpResume = lib.Acm2_GpResume
        Acm2_GpResume.argtypes = [c_uint32]
        Acm2_GpResume.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpPause = lib.Acm2_GpPause
        Acm2_GpPause.argtypes = [c_uint32]
        Acm2_GpPause.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpMotionStop = lib.Acm2_GpMotionStop
        Acm2_GpMotionStop.argtypes = [c_uint32, c_uint, c_double]
        Acm2_GpMotionStop.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpChangeVel = lib.Acm2_GpChangeVel
        Acm2_GpChangeVel.argtypes = [c_uint32, c_double, c_double, c_double]
        Acm2_GpChangeVel.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpChangeVelByRate = lib.Acm2_GpChangeVelByRate
        Acm2_GpChangeVelByRate.argtypes = [c_uint32, c_uint32, c_double, c_double]
        Acm2_GpChangeVelByRate.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpGetVel = lib.Acm2_GpGetVel
        Acm2_GpGetVel.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        Acm2_GpGetVel.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpSetSpeedProfile = lib.Acm2_GpSetSpeedProfile
        Acm2_GpSetSpeedProfile.argtypes = [c_uint32, SPEED_PROFILE_PRM]
        Acm2_GpSetSpeedProfile.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpGetState = lib.Acm2_GpGetState
        Acm2_GpGetState.argtypes = [c_uint32, POINTER(c_uint32)]
        Acm2_GpGetState.restype = c_uint32
    except:
        pass

# Path
    try:
        Acm2_GpLoadPath = lib.Acm2_GpLoadPath
        Acm2_GpLoadPath.argtypes = [c_uint32, c_char_p, POINTER(c_uint32)]
        Acm2_GpLoadPath.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpAddPath = lib.Acm2_GpAddPath
        Acm2_GpAddPath.argtypes = [c_uint32, c_uint32, c_uint, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_uint32)]
        Acm2_GpAddPath.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpMovePath = lib.Acm2_GpMovePath
        Acm2_GpMovePath.argtypes = [c_uint32]
        Acm2_GpMovePath.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpResetPath = lib.Acm2_GpResetPath
        Acm2_GpResetPath.argtypes = [c_uint32]
        Acm2_GpResetPath.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpGetPathStatus = lib.Acm2_GpGetPathStatus
        Acm2_GpGetPathStatus.argtypes = [c_uint32, POINTER(c_uint)]
        Acm2_GpGetPathStatus.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpMoveSelPath = lib.Acm2_GpMoveSelPath
        Acm2_GpMoveSelPath.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32]
        Acm2_GpMoveSelPath.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpGetPathIndexStatus = lib.Acm2_GpGetPathIndexStatus
        Acm2_GpGetPathIndexStatus.argtypes = [c_uint32, c_uint32, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_uint32)]
        Acm2_GpGetPathIndexStatus.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpDelay = lib.Acm2_GpDelay
        Acm2_GpDelay.argtypes = [c_uint32, c_uint32]
        Acm2_GpDelay.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpPathDO = lib.Acm2_GpPathDO
        Acm2_GpPathDO.argtypes = [c_uint32, PATH_DO_PRM]
        Acm2_GpPathDO.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpPathWaitDI = lib.Acm2_GpPathWaitDI
        Acm2_GpPathWaitDI.argtypes = [c_uint32, PATH_DI_WAIT_PRM]
        Acm2_GpPathWaitDI.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpPathWaitForAxis = lib.Acm2_GpPathWaitForAxis
        Acm2_GpPathWaitForAxis.argtypes = [c_uint32, PATH_AX_WAIT_PRM]
        Acm2_GpPathWaitForAxis.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpLookAheadPath = lib.Acm2_GpLookAheadPath
        Acm2_GpLookAheadPath.argtypes = [c_uint32, c_uint16, c_char_p]
        Acm2_GpLookAheadPath.restype = c_uint32
    except:
        pass

    try:
        Acm2_GpLookAheadPathFile = lib.Acm2_GpLookAheadPathFile
        Acm2_GpLookAheadPathFile.argtypes = [c_uint32, c_uint16, c_char_p, c_char_p, POINTER(c_uint32)]
        Acm2_GpLookAheadPathFile.restype = c_uint32
    except:
        pass

    # try:
    #     Acm2_GpLoadAndMovePath = lib.Acm2_GpLoadAndMovePath
    #     Acm2_GpLoadAndMovePath.argtypes = [c_uint32, c_char_p, POINTER(c_uint32)]
    #     Acm2_GpLoadAndMovePath.restype = c_uint32
    # except:
    #     pass

# DIO
    try:
        Acm2_ChSetDOBit = lib.Acm2_ChSetDOBit
        Acm2_ChSetDOBit.argtypes = [c_uint32, c_uint32]
        Acm2_ChSetDOBit.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetDOBit = lib.Acm2_ChGetDOBit
        Acm2_ChGetDOBit.argtypes = [c_uint32, POINTER(c_uint32)]
        Acm2_ChGetDOBit.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetDIBit = lib.Acm2_ChGetDIBit
        Acm2_ChGetDIBit.argtypes = [c_uint32, POINTER(c_uint32)]
        Acm2_ChGetDIBit.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetDOBitByRingNo = lib.Acm2_ChSetDOBitByRingNo
        Acm2_ChSetDOBitByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32]
        Acm2_ChSetDOBitByRingNo.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetDOBitByRingNo = lib.Acm2_ChGetDOBitByRingNo
        Acm2_ChGetDOBitByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_ChGetDOBitByRingNo.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetDIBitByRingNo = lib.Acm2_ChGetDIBitByRingNo
        Acm2_ChGetDIBitByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_ChGetDIBitByRingNo.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetDOByte = lib.Acm2_ChSetDOByte
        Acm2_ChSetDOByte.argtypes = [c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_ChSetDOByte.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetDOByte = lib.Acm2_ChGetDOByte
        Acm2_ChGetDOByte.argtypes = [c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_ChGetDOByte.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetDIByte = lib.Acm2_ChGetDIByte
        Acm2_ChGetDIByte.argtypes = [c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_ChGetDIByte.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetDOByteByRingNo = lib.Acm2_ChSetDOByteByRingNo
        Acm2_ChSetDOByteByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_ChSetDOByteByRingNo.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetDOByteByRingNo = lib.Acm2_ChGetDOByteByRingNo
        Acm2_ChGetDOByteByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_ChGetDOByteByRingNo.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetDIByteByRingNo = lib.Acm2_ChGetDIByteByRingNo
        Acm2_ChGetDIByteByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        Acm2_ChGetDIByteByRingNo.restype = c_uint32
    except:
        pass
# AIO
    try:
        Acm2_ChSetAOData = lib.Acm2_ChSetAOData
        Acm2_ChSetAOData.argtypes = [c_uint32, c_uint, c_double]
        Acm2_ChSetAOData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetAOData = lib.Acm2_ChGetAOData
        Acm2_ChGetAOData.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        Acm2_ChGetAOData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetAODataByRingNo = lib.Acm2_ChSetAODataByRingNo
        Acm2_ChSetAODataByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint, c_double]
        Acm2_ChSetAODataByRingNo.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetAODataByRingNo = lib.Acm2_ChGetAODataByRingNo
        Acm2_ChGetAODataByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint, POINTER(c_double)]
        Acm2_ChGetAODataByRingNo.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetAIData = lib.Acm2_ChGetAIData
        Acm2_ChGetAIData.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        Acm2_ChGetAIData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetAIDataByRingNo = lib.Acm2_ChGetAIDataByRingNo
        Acm2_ChGetAIDataByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint, POINTER(c_double)]
        Acm2_ChGetAIDataByRingNo.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetCntData = lib.Acm2_ChGetCntData
        Acm2_ChGetCntData.argtypes = [c_uint32, POINTER(c_double)]
        Acm2_ChGetCntData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetCntData = lib.Acm2_ChSetCntData
        Acm2_ChSetCntData.argtypes = [c_uint32, c_double]
        Acm2_ChSetCntData.restype = c_uint32
    except:
        pass
# Motion DIO:Compare
    try:
        Acm2_ChLinkCmpFIFO = lib.Acm2_ChLinkCmpFIFO
        Acm2_ChLinkCmpFIFO.argtypes = [c_uint32, POINTER(c_uint32), c_uint32]
        Acm2_ChLinkCmpFIFO.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChLinkCmpObject = lib.Acm2_ChLinkCmpObject
        Acm2_ChLinkCmpObject.argtypes = [c_uint32, c_uint, POINTER(c_uint32), c_uint32]
        Acm2_ChLinkCmpObject.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetLinkedCmpObject = lib.Acm2_ChGetLinkedCmpObject
        Acm2_ChGetLinkedCmpObject.argtypes = [c_uint32, c_uint, POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_ChGetLinkedCmpObject.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChEnableCmp = lib.Acm2_ChEnableCmp
        Acm2_ChEnableCmp.argtypes = [c_uint32, c_uint32]
        Acm2_ChEnableCmp.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetCmpOut = lib.Acm2_ChSetCmpOut
        Acm2_ChSetCmpOut.argtypes = [c_uint32, c_uint]
        Acm2_ChSetCmpOut.restype = c_uint32
    except:
        pass
    
    try:
        Acm2_ChSetCmpDoOut = lib.Acm2_ChSetCmpDoOut
        Acm2_ChSetCmpDoOut.argtypes = [c_uint32, c_uint]
        Acm2_ChSetCmpDoOut.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGetCmpData = lib.Acm2_AxGetCmpData
        Acm2_AxGetCmpData.argtypes = [c_uint32, POINTER(c_double)]
        Acm2_AxGetCmpData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetCmpData = lib.Acm2_ChGetCmpData
        Acm2_ChGetCmpData.argtypes = [c_uint32, POINTER(c_double), c_uint32]
        Acm2_ChGetCmpData.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSetCmpTable = lib.Acm2_AxSetCmpTable
        Acm2_AxSetCmpTable.argtypes = [c_uint32, POINTER(c_double), c_uint32]
        Acm2_AxSetCmpTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxSetCmpAuto = lib.Acm2_AxSetCmpAuto
        Acm2_AxSetCmpAuto.argtypes = [c_uint32, c_double, c_double, c_double]
        Acm2_AxSetCmpAuto.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetCmpAuto = lib.Acm2_ChSetCmpAuto
        Acm2_ChSetCmpAuto.argtypes = [c_uint32, c_double, c_double, c_double]
        Acm2_ChSetCmpAuto.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetCmpBufferData = lib.Acm2_ChSetCmpBufferData
        Acm2_ChSetCmpBufferData.argtypes = [c_uint32, POINTER(c_double), c_uint32]
        Acm2_ChSetCmpBufferData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetMultiCmpTable = lib.Acm2_ChSetMultiCmpTable
        Acm2_ChSetMultiCmpTable.argtypes = [c_uint32, c_uint, c_uint32]
        Acm2_ChSetMultiCmpTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetMultiCmpBufferData = lib.Acm2_ChSetMultiCmpBufferData
        Acm2_ChSetMultiCmpBufferData.argtypes = [c_uint32, POINTER(c_double), c_uint32, c_uint32]
        Acm2_ChSetMultiCmpBufferData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChResetCmpData = lib.Acm2_ChResetCmpData
        Acm2_ChResetCmpData.argtypes = [c_uint32]
        Acm2_ChResetCmpData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetCmpBufferStatus = lib.Acm2_ChGetCmpBufferStatus
        Acm2_ChGetCmpBufferStatus.argtypes = [c_uint32, POINTER(BUFFER_STATUS)]
        Acm2_ChGetCmpBufferStatus.restype = c_uint32
    except:
        pass
# Motion IO: Latch
    try:
        Acm2_ChLinkLatchAxis = lib.Acm2_ChLinkLatchAxis
        Acm2_ChLinkLatchAxis.argtypes = [c_uint32, POINTER(c_uint32), c_uint32]
        Acm2_ChLinkLatchAxis.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChLinkLatchObject = lib.Acm2_ChLinkLatchObject
        Acm2_ChLinkLatchObject.argtypes = [c_uint32, c_uint, POINTER(c_uint32), c_uint32]
        Acm2_ChLinkLatchObject.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetLinkedLatchObject = lib.Acm2_ChGetLinkedLatchObject
        Acm2_ChGetLinkedLatchObject.argtypes = [c_uint32, POINTER(c_uint),POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_ChGetLinkedLatchObject.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChTriggerLatch = lib.Acm2_ChTriggerLatch
        Acm2_ChTriggerLatch.argtypes = [c_uint32]
        Acm2_ChTriggerLatch.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxReadLatchBuffer = lib.Acm2_AxReadLatchBuffer
        Acm2_AxReadLatchBuffer.argtypes = [c_uint32, POINTER(c_double), POINTER(c_uint32)]
        Acm2_AxReadLatchBuffer.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChReadLatchBuffer = lib.Acm2_ChReadLatchBuffer
        Acm2_ChReadLatchBuffer.argtypes = [c_uint32, POINTER(c_double), c_uint32, POINTER(c_uint32)]
        Acm2_ChReadLatchBuffer.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGetLatchBufferStatus = lib.Acm2_AxGetLatchBufferStatus
        Acm2_AxGetLatchBufferStatus.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_AxGetLatchBufferStatus.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetLatchBufferStatus = lib.Acm2_ChGetLatchBufferStatus
        Acm2_ChGetLatchBufferStatus.argtypes = [c_uint32, POINTER(BUFFER_STATUS)]
        Acm2_ChGetLatchBufferStatus.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxResetLatchBuffer = lib.Acm2_AxResetLatchBuffer
        Acm2_AxResetLatchBuffer.argtypes = [c_uint32]
        Acm2_AxResetLatchBuffer.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChResetLatchBuffer = lib.Acm2_ChResetLatchBuffer
        Acm2_ChResetLatchBuffer.argtypes = [c_uint32]
        Acm2_ChResetLatchBuffer.restype = c_uint32
    except:
        pass
# Motion IO: PWM
    try:
        Acm2_ChLinkPWMTable = lib.Acm2_ChLinkPWMTable
        Acm2_ChLinkPWMTable.argtypes = [c_uint32, c_uint, c_uint32]
        Acm2_ChLinkPWMTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetLinkedPWMTable = lib.Acm2_ChGetLinkedPWMTable
        Acm2_ChGetLinkedPWMTable.argtypes = [c_uint32, POINTER(c_uint), POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_ChGetLinkedPWMTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetPWMTable = lib.Acm2_ChSetPWMTable
        Acm2_ChSetPWMTable.argtypes = [c_uint32, POINTER(c_double), POINTER(c_double), c_uint32]
        Acm2_ChSetPWMTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChLoadPWMTableFile = lib.Acm2_ChLoadPWMTableFile
        Acm2_ChLoadPWMTableFile.argtypes = [c_uint32, c_char_p, POINTER(c_uint32)]
        Acm2_ChLoadPWMTableFile.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetPWMTableStatus = lib.Acm2_ChGetPWMTableStatus
        Acm2_ChGetPWMTableStatus.argtypes = [c_uint32, POINTER(PWM_TABLE_STATUS)]
        Acm2_ChGetPWMTableStatus.restype = c_uint32
    except:
        pass
# Motion IO: External Drive
    try:
        Acm2_ChGetExtDriveData = lib.Acm2_ChGetExtDriveData
        Acm2_ChGetExtDriveData.argtypes = [c_uint32, POINTER(c_double)]
        Acm2_ChGetExtDriveData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChSetExtDriveData = lib.Acm2_ChSetExtDriveData
        Acm2_ChSetExtDriveData.argtypes = [c_uint32, c_double]
        Acm2_ChSetExtDriveData.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChLinkExtDriveObject = lib.Acm2_ChLinkExtDriveObject
        Acm2_ChLinkExtDriveObject.argtypes = [c_uint32, c_uint, c_uint32]
        Acm2_ChLinkExtDriveObject.restype = c_uint32
    except:
        pass

    try:
        Acm2_ChGetLinkedExtDriveObject = lib.Acm2_ChGetLinkedExtDriveObject
        Acm2_ChGetLinkedExtDriveObject.argtypes = [c_uint32, POINTER(c_uint), POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_ChGetLinkedExtDriveObject.restype = c_uint32
    except:
        pass
# Motion DAQ
    try:
        Acm2_DevMDaqConfig = lib.Acm2_DevMDaqConfig
        Acm2_DevMDaqConfig.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32]
        Acm2_DevMDaqConfig.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevMDaqGetConfig = lib.Acm2_DevMDaqGetConfig
        Acm2_DevMDaqGetConfig.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_DevMDaqGetConfig.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevMDaqStart = lib.Acm2_DevMDaqStart
        Acm2_DevMDaqStart.argtypes = [c_uint32]
        Acm2_DevMDaqStart.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevMDaqStop = lib.Acm2_DevMDaqStop
        Acm2_DevMDaqStop.argtypes = [c_uint32]
        Acm2_DevMDaqStop.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevMDaqReset = lib.Acm2_DevMDaqReset
        Acm2_DevMDaqReset.argtypes = [c_uint32]
        Acm2_DevMDaqReset.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevMDaqGetStatus = lib.Acm2_DevMDaqGetStatus
        Acm2_DevMDaqGetStatus.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_DevMDaqGetStatus.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevMDaqGetData = lib.Acm2_DevMDaqGetData
        Acm2_DevMDaqGetData.argtypes = [c_uint32, c_uint32, c_uint32, POINTER(c_double)]
        Acm2_DevMDaqGetData.restype = c_uint32
    except:
        pass
# Donwload DSP FW
    try:
        Acm2_GetDSPFrmWareDwnLoadRate = lib.Acm2_GetDSPFrmWareDwnLoadRate
        Acm2_GetDSPFrmWareDwnLoadRate.argtypes = [c_uint32, POINTER(c_double)]
        Acm2_GetDSPFrmWareDwnLoadRate.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevDownLoadDSPFrmWare_STP2 = lib.Acm2_DevDownLoadDSPFrmWare_STP2
        Acm2_DevDownLoadDSPFrmWare_STP2.argtypes = [c_uint32, c_char_p]
        Acm2_DevDownLoadDSPFrmWare_STP2.restype = c_uint32
    except:
        pass
# EtherCAT
    try:
        Acm2_DevLoadENI = lib.Acm2_DevLoadENI
        Acm2_DevLoadENI.argtypes = [c_uint32, c_char_p]
        Acm2_DevLoadENI.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevConnect = lib.Acm2_DevConnect
        Acm2_DevConnect.argtypes = [c_uint32]
        Acm2_DevConnect.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevDisConnect = lib.Acm2_DevDisConnect
        Acm2_DevDisConnect.argtypes = [c_uint32]
        Acm2_DevDisConnect.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevGetSubDevicesID = lib.Acm2_DevGetSubDevicesID
        Acm2_DevGetSubDevicesID.argtypes = [c_uint32, c_uint, POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_DevGetSubDevicesID.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevGetMDeviceInfo = lib.Acm2_DevGetMDeviceInfo
        Acm2_DevGetMDeviceInfo.argtypes = [c_uint32, POINTER(ADVAPI_MDEVICE_INFO)]
        Acm2_DevGetMDeviceInfo.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevGetSubDeviceInfo = lib.Acm2_DevGetSubDeviceInfo
        Acm2_DevGetSubDeviceInfo.argtypes = [c_uint32, c_uint, c_uint32, POINTER(ADVAPI_SUBDEVICE_INFO_CM2)]
        Acm2_DevGetSubDeviceInfo.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevGetSubDeviceFwVersion = lib.Acm2_DevGetSubDeviceFwVersion
        Acm2_DevGetSubDeviceFwVersion.argtypes = [c_uint32, c_uint, c_uint32, c_char_p]
        Acm2_DevGetSubDeviceFwVersion.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevSetSubDeviceID = lib.Acm2_DevSetSubDeviceID
        Acm2_DevSetSubDeviceID.argtypes = [c_uint32, c_int, c_uint32, c_uint32]
        Acm2_DevSetSubDeviceID.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevSetSubDeviceStates = lib.Acm2_DevSetSubDeviceStates
        Acm2_DevSetSubDeviceStates.argtypes = [c_uint32, c_uint, c_uint32, POINTER(c_uint32)]
        Acm2_DevSetSubDeviceStates.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevGetSubDeviceStates = lib.Acm2_DevGetSubDeviceStates
        Acm2_DevGetSubDeviceStates.argtypes = [c_uint32, c_uint, c_uint32, POINTER(c_uint32)]
        Acm2_DevGetSubDeviceStates.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevWriteSDO = lib.Acm2_DevWriteSDO
        Acm2_DevWriteSDO.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        Acm2_DevWriteSDO.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevReadSDO = lib.Acm2_DevReadSDO
        Acm2_DevReadSDO.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        Acm2_DevReadSDO.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevWritePDO = lib.Acm2_DevWritePDO
        Acm2_DevWritePDO.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        Acm2_DevWritePDO.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevReadPDO = lib.Acm2_DevReadPDO
        Acm2_DevReadPDO.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        Acm2_DevReadPDO.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevWriteReg = lib.Acm2_DevWriteReg
        Acm2_DevWriteReg.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        Acm2_DevWriteReg.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevReadReg = lib.Acm2_DevReadReg
        Acm2_DevReadReg.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        Acm2_DevReadReg.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevReadSubDeviceCommErrCnt = lib.Acm2_DevReadSubDeviceCommErrCnt
        Acm2_DevReadSubDeviceCommErrCnt.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        Acm2_DevReadSubDeviceCommErrCnt.restype = c_uint32
    except:
        pass

    try:
        Acm2_Ax1DCompensateTable = lib.Acm2_Ax1DCompensateTable
        Acm2_Ax1DCompensateTable.argtypes = [c_uint32, c_double, c_double, POINTER(c_double), c_uint32, c_uint32]
        Acm2_Ax1DCompensateTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_Ax2DCompensateTable = lib.Acm2_Ax2DCompensateTable
        Acm2_Ax2DCompensateTable.argtypes = [c_uint32, c_uint32, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), c_uint32, c_uint32]
        Acm2_Ax2DCompensateTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxZAxisCompensateTable = lib.Acm2_AxZAxisCompensateTable
        Acm2_AxZAxisCompensateTable.argtypes = [c_uint32, c_uint32, c_uint32, c_double, c_double, c_double, c_double, POINTER(c_double), c_uint32, c_uint32]
        Acm2_AxZAxisCompensateTable.restype = c_uint32
    except:
        pass

    try:
        Acm2_AxGetCompensatePosition = lib.Acm2_AxGetCompensatePosition
        Acm2_AxGetCompensatePosition.argtypes = [c_uint32, POINTER(c_double)]
        Acm2_AxGetCompensatePosition.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevOscChannelDataStart = lib.Acm2_DevOscChannelDataStart
        Acm2_DevOscChannelDataStart.argtypes = [c_uint32]
        Acm2_DevOscChannelDataStart.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevOscChannelDataStop = lib.Acm2_DevOscChannelDataStop
        Acm2_DevOscChannelDataStop.argtypes = [c_uint32]
        Acm2_DevOscChannelDataStop.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevGetOscChannelDataConfig = lib.Acm2_DevGetOscChannelDataConfig
        Acm2_DevGetOscChannelDataConfig.argtypes = [c_uint32, c_uint16, POINTER(OSC_PROFILE_PRM)]
        Acm2_DevGetOscChannelDataConfig.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevSetOscChannelDataConfig = lib.Acm2_DevSetOscChannelDataConfig
        Acm2_DevSetOscChannelDataConfig.argtypes = [c_uint32, c_uint16, OSC_PROFILE_PRM]
        Acm2_DevSetOscChannelDataConfig.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevGetOscChannelData = lib.Acm2_DevGetOscChannelData
        Acm2_DevGetOscChannelData.argtypes = [c_uint32, c_uint16, c_uint32, POINTER(c_uint32), POINTER(c_double)]
        Acm2_DevGetOscChannelData.restype = c_uint32
    except:
        pass

    try:
        Acm2_DevGetOscChannelStatus = lib.Acm2_DevGetOscChannelStatus
        Acm2_DevGetOscChannelStatus.argtypes = [c_uint32, POINTER(c_uint32)]
        Acm2_DevGetOscChannelStatus.restype = c_uint32
    except:
        pass