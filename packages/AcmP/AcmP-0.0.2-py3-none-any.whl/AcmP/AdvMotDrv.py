from enum import Enum

class ADV_OBJ_TYPE(Enum):
    ADV_DEVICE = 0
    ADV_AXIS = 1
    ADV_GROUP = 2
    ADV_LATCH_CHANNEL = 3
    ADV_COMPARE_CHANNEL = 4
    ADV_RING = 5
    ADV_GENERAL_DI_PORT = 6
    ADV_GENERAL_DO_PORT = 7
    ADV_GENERAL_AI_CHANNEL = 8
    ADV_GENERAL_AO_CHANNEL = 9
    ADV_COUNTER_CHANNEL = 10
    ADV_MDAQ_CHANNEL = 11
    ADV_EXT_DRIVE_CHANNEL = 12

class DO_ONOFF(Enum):
    DO_OFF = 0
    DO_ON = 1

class ECAT_ID_TYPE(Enum):
    SUBDEVICE_ID = 0
    SUBDEVICE_POS = 1

class ABS_MODE(Enum):
    MOVE_REL = 0
    MOVE_ABS = 1

class MOTION_DIRECTION(Enum):
    DIRECTION_POS = 0
    DIRECTION_NEG = 1

class HOME_MODE(Enum):
    MODE1_ABS = 0
    MODE2_LMT = 1
    MODE3_REF = 2
    MODE4_ABS_REF = 3
    MODE5_ABS_NEG_REF = 4
    MODE6_LMT_REF = 5
    MODE7_ABS_SEARCH = 6
    MODE8_LMT_SEARCH = 7
    MODE9_ABS_SEARCH_REF = 8
    MODE10_ABS_SEARCH_NEG_REF = 9
    MODE11_LMT_SEARCH_REF = 10
    MODE12_ABS_SEARCH_REFIND = 11
    MODE13_LMT_SEARCH_REFIND = 12
    MODE14_ABS_SEARCH_REFIND_REF = 13
    MODE15_ABS_SEARCH_REFIND_NEG_REF = 14
    MODE16_LMT_SEARCH_REFIND_NEG_REF = 15

class AXIS_STATUS_TYPE(Enum):
    AXIS_STATE = 0
    MOTION_STATUS = 1

class POSITION_TYPE(Enum):
    POSITION_CMD = 0
    POSITION_ACT = 1

class VELOCITY_TYPE(Enum):
    VELOCITY_CMD = 0
    VELOCITY_ACT = 1

class GP_LINE_MODE(Enum):
    LINE_REL = 0
    LINE_ABS = 1
    DIRECT_REL = 2
    DIRECT_ABS = 3

class ARC_DIRECTION(Enum):
    ARC_CW = 0
    ARC_CCW = 1

class PATH_MOVE_MODE_CM2(Enum):
    BUFFER_MODE = 0
    BLENDING_MODE = 1
    FLY_MODE = 2
    SPEED_FORWARD_MODE = 3

class MOTION_STOP_MODE(Enum):
    MOTION_STOP_MODE_DEC = 0
    MOTION_STOP_MODE_EMG = 1

class EXT_DRIVE_MODE(Enum):
    JOG_STOP_MODE = 0
    JOG_MODE = 1
    MPG_MODE = 2

class ADV_EVENT_SUBSCRIBE(Enum):
    EVENT_DISABLE = -1
    AXIS_MOTION_DONE = 0
    AXIS_COMPARE = 1
    AXIS_LATCHED = 2
    AXIS_ERROR = 3
    AXIS_VH_START = 4
    AXIS_VH_END = 5
    AXIS_LATCH_BUFFER_DONE = 6
    AXIS_GEAR_IN = 7
    GROUP_MOTION_DONE = 100
    GROUP_VH_START = 101
    GROUP_VH_END = 102
    DEVICE_LATCHED = 200
    DEVICE_DISCONNECT = 300
    DEVICE_IO_DISCONNECT = 301
    DEVICE_MODE_CHANGE = 302
    DEVICE_IO_MODE_CHANGE = 303
    DEVICE_LOST_FRAME = 304
    DEVICE_IO_LOST_FRAME = 305
    DEVICE_LOST_FRAME_WARN = 306
    DEVICE_IO_LOST_FRAME_WARN = 307
    DEVICE_COMM_RECOVERY = 308
    DEVICE_IO_COMM_RECOVERY = 309

class DAQ_DATA_TYPE(Enum):
    RAW_DATA = 0
    SCALED_DATA = 1

class AXIS_STATE(Enum):
    STA_AX_DISABLE = 0
    STA_AX_READY = 1
    STA_AX_STOPPING = 2
    STA_AX_ERROR_STOP = 3
    STA_AX_HOMING = 4
    STA_AX_PTP_MOT = 5
    STA_AX_CONTI_MOT = 6
    STA_AX_SYNC_MOT = 7
    STA_AX_EXT_JOG = 8
    STA_AX_EXT_MPG = 9
    STA_AX_PAUSE = 10
    STA_AX_BUSY = 11
    STA_AX_WAIT_DI = 12
    STA_AX_WAIT_PTP = 13
    STA_AX_WAIT_VEL = 14
    STA_AX_EXT_JOG_READY = 15

class SUB_DEV_STATE(Enum):
    # unknown state
    EC_SLAVE_STATE_UNKNOWN = 0x00
    # INIT state (no mailbox communication, no IO)
    EC_SLAVE_STATE_INIT = 0x01
    # PREOP state (mailbox communication, no IO)
    EC_SLAVE_STATE_PREOP = 0x02
    # Bootstrap state (mailbox communication, firmware update)
    EC_SLAVE_STATE_BOOT = 0x03
    # SAFEOP (mailbox communication and input update)
    EC_SLAVE_STATE_SAFEOP = 0x04
    # OP (mailbox communication and input/output update)
    EC_SLAVE_STATE_OP = 0x08
    EC_SLAVE_STATE_OFFLINE = 0x0F
    # Acknowledge/Error bit (no actual state)
    EC_SLAVE_STATE_ACK_ERR = 0x10

class ECAT_TYPE(Enum):
    ECAT_TYPE_I8 = 1
    ECAT_TYPE_U8 = 2
    ECAT_TYPE_I16 = 3
    ECAT_TYPE_U16 = 4
    ECAT_TYPE_I32 = 5
    ECAT_TYPE_U32 = 6
    ECAT_TYPE_I64 = 7
    ECAT_TYPE_U64 = 8
    ECAT_TYPE_STRING = 9
    ECAT_TYPE_BOOL = 10
    ECAT_TYPE_F32 = 11
    ECAT_TYPE_F64 = 12

class MOTION_PATH_CMD(Enum):
    EndPath = 0
    Abs2DLine = 1
    Rel2DLine = 2
    Abs2DArcCW = 3
    Abs2DArcCCW = 4
    Rel2DArcCW = 5
    Rel2DArcCCW = 6
    Abs3DLine = 7
    Rel3DLine = 8
    AbsMultiLine = 9
    RelMultiLine = 10
    Abs2DDirect = 11  
    Rel2DDirect = 12
    Abs3DDirect = 13
    Rel3DDirect = 14
    Abs4DDirect = 15
    Rel4DDirect = 16
    Abs5DDirect = 17
    Rel5DDirect = 18
    Abs6DDirect = 19
    Rel6DDirect = 20
    Abs3DArcCW = 21
    Rel3DArcCW = 22
    Abs3DArcCCW = 23
    Rel3DArcCCW = 24
    Abs3DSpiralCW = 25  
    Rel3DSpiralCW = 26
    Abs3DSpiralCCW = 27
    Rel3DSpiralCCW = 28
    GPDELAY = 29
    Abs4DSpiralCW = 30
    Rel4DSpiralCW = 31
    Abs4DSpiralCCW = 32
    Rel4DSpiralCCW = 33
    Abs5DSpiralCW = 34  
    Rel5DSpiralCW = 35
    Abs5DSpiralCCW = 36
    Rel5DSpiralCCW = 37
    Abs6DSpiralCW = 38  
    Rel6DSpiralCW = 39
    Abs6DSpiralCCW = 40
    Rel6DSpiralCCW = 41
    Abs7DSpiralCW = 42  
    Rel7DSpiralCW = 43
    Abs7DSpiralCCW = 44
    Rel7DSpiralCCW = 45
    Abs8DSpiralCW = 46  
    Rel8DSpiralCW = 47
    Abs8DSpiralCCW = 48
    Rel8DSpiralCCW = 49
    Abs2DArcCWAngle = 50
    Rel2DArcCWAngle = 51
    Abs2DArcCCWAngle = 52
    Rel2DArcCCWAngle = 53
    Abs3DArcCWAngle = 54
    Rel3DArcCWAngle = 55
    Abs3DArcCCWAngle = 56
    Rel3DArcCCWAngle = 57
    Abs3DSpiralCWAngle = 58  
    Rel3DSpiralCWAngle = 59
    Abs3DSpiralCCWAngle = 60
    Rel3DSpiralCCWAngle = 61
    Abs4DSpiralCWAngle = 62  
    Rel4DSpiralCWAngle = 63
    Abs4DSpiralCCWAngle = 64
    Rel4DSpiralCCWAngle = 65
    Abs5DSpiralCWAngle = 66  
    Rel5DSpiralCWAngle = 67
    Abs5DSpiralCCWAngle = 68
    Rel5DSpiralCCWAngle = 69
    Abs6DSpiralCWAngle = 70 
    Rel6DSpiralCWAngle = 71
    Abs6DSpiralCCWAngle = 72
    Rel6DSpiralCCWAngle = 73
    Abs7DSpiralCWAngle = 74  
    Rel7DSpiralCWAngle = 75
    Abs7DSpiralCCWAngle = 76
    Rel7DSpiralCCWAngle = 77
    Abs8DSpiralCWAngle = 78  
    Rel8DSpiralCWAngle = 79
    Abs8DSpiralCCWAngle = 80
    Rel8DSpiralCCWAngle = 81
    Abs7DDirect = 82
    Rel7DDirect = 83
    Abs8DDirect = 84
    Rel8DDirect = 85
    Abs2DArcCW_3P = 86
    Rel2DArcCW_3P = 87 
    Abs2DArcCCW_3P = 88 
    Rel2DArcCCW_3P = 89
    DoControl = 90
    Abs1DDirect = 91  
    Rel1DDirect = 92
    Abs3DSpiralCW_3P = 93  
    Rel3DSpiralCW_3P = 94
    Abs3DSpiralCCW_3P = 95
    Rel3DSpiralCCW_3P = 96
    Abs4DSpiralCW_3P = 97
    Rel4DSpiralCW_3P = 98
    Abs4DSpiralCCW_3P = 99
    Rel4DSpiralCCW_3P = 100
    Abs5DSpiralCW_3P = 101  
    Rel5DSpiralCW_3P = 102
    Abs5DSpiralCCW_3P = 103
    Rel5DSpiralCCW_3P = 104
    Abs6DSpiralCW_3P = 105 
    Rel6DSpiralCW_3P = 106
    Abs6DSpiralCCW_3P = 107
    Rel6DSpiralCCW_3P = 108
    Abs7DSpiralCW_3P = 109
    Rel7DSpiralCW_3P = 110
    Abs7DSpiralCCW_3P = 111
    Rel7DSpiralCCW_3P = 112
    Abs8DSpiralCW_3P = 113  
    Rel8DSpiralCW_3P = 114
    Abs8DSpiralCCW_3P = 115
    Rel8DSpiralCCW_3P = 116
    WaitforAxis = 117
    Abs3DArcCW_3P = 118
    Rel3DArcCW_3P = 119
    Abs3DArcCCW_3P = 120
    Rel3DArcCCW_3P = 121
    AxDoControl = 122
    WaitforDI = 123
    SetRefPlane = 124
    Abs2DSpline = 125
    Rel2DSpline = 126
    Abs3DSpline = 127
    Rel3DSpline = 128
    Abs3DSplineR = 129
    Rel3DSplineR = 130
    Abs3DSpline2R = 131
    Rel3DSpline2R = 132
    WaitforDevDI = 133
    WaitforSlaveDI = 134
    WaitforSubDeviceDI = 134
    WaitforAxDI = 135
    DevDoControl = 136
    SlaveDoControl = 137
    SubDeviceDoControl = 137
