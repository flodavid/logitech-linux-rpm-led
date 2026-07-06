import socket
import struct

import time
import struct

MAX_POS = 63
CURR_POS = 37
BUFFER_SIZE = 2048
CAR_TELEMETRY = struct.Struct('<66f')
CAR_TELEMETRY_SIZE = CAR_TELEMETRY.size


class Wreckfest2:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 23123
        self.rpm = 0
        self.rpmMax = 1
        
    def connect(self):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((self.ip, self.port))
        return udp_socket
        
    def read_data(self, udp_socket):
        data, addr = udp_socket.recvfrom(BUFFER_SIZE)
        return data
    
    def calc_rpm_percent(self):
        if (self.rpmMax == 0):
            return 0

        rpm_percent = (self.rpm * 100) / self.rpmMax
        # Return 0 if rpm is 99 or above to have a blinking effect when reaching max RPM
        if (rpm_percent >= 99):
            return 0
        return rpm_percent

    def get_rpm_percent(self, data, percent) -> int:
        signature = int.from_bytes(data[0:4], byteorder='little', signed=False)
        packetType = int.from_bytes(data[4:5], byteorder='little', signed=False)
        # statusFlags = int.from_bytes(data[5:6], byteorder='little', signed=False)
        # sessionTime = int.from_bytes(data[6:10], byteorder='little', signed=True)
        # raceTime = int.from_bytes(data[10:14], byteorder='little', signed=True)

        if signature != 1869769584:
            print ("ERROR: Invalid packet signature")
            return percent
        
        if packetType != 0:
            return percent

        # print("GameStatusFlag: ", statusFlags) #U8
        # print("sessionTime: ", sessionTime) #S32
        # print("raceTime: ", raceTime) #S32


        # marshalFlagsPlayer = int.from_bytes(data[14:16]) #U16
        # print("marshalFlagsPlayer: ", marshalFlagsPlayer)

        # print("===Leaderboard===")
        # status = int.from_bytes(data[16:17], byteorder='little', signed=False)
        # trackStatus = int.from_bytes(data[17:18], byteorder='little', signed=False)
        # lapCurrent = int.from_bytes(data[18:20], byteorder='little', signed=False)
        # position = int.from_bytes(data[20:21], byteorder='little', signed=False)
        # health = int.from_bytes(data[21:22], byteorder='little', signed=False)

        # wrecks = int.from_bytes(data[22:24], byteorder='little', signed=False)
        # frags = int.from_bytes(data[24:26], byteorder='little', signed=False)
        # assists = int.from_bytes(data[26:28], byteorder='little', signed=False)

        # score = int.from_bytes(data[28:32], byteorder='little', signed=True)
        # points = int.from_bytes(data[32:36], byteorder='little', signed=True)
        
        # deltaLeader = int.from_bytes(data[36:40], byteorder='little', signed=True)

        # lapTiming = int.from_bytes(data[40:42], byteorder='little', signed=False)
        # reserved1 = int.from_bytes(data[42:48])

        # print("status: ", status)
        # print("trackStatus: ", trackStatus)
        # print("lapCurrent: ", lapCurrent)
        # print("position: ", position)
        # print("health: ", health)
        # print("wrecks: ", wrecks)
        # print("frags", frags)
        # print("assists: ", assists)
        # print("score: ", score)
        # print("points: ", points)
        # print("deltaLeader: ", deltaLeader)
        # print("lapTiming: ", lapTiming)
        # print("reserved1: ", reserved1)

        # print("===Timing===")
        # timing = data[48:77]
        # lapTimeCurrent = int.from_bytes(data[48:52], byteorder='little', signed=False)
        # lapTimePenaltyCurrent = int.from_bytes(data[52:56], byteorder='little', signed=False)
        # lapTimeLast = int.from_bytes(data[56:60], byteorder='little', signed=False)
        # lapTimeBest = int.from_bytes(data[60:64], byteorder='little', signed=False)
        # lapBest = data[64] #U8
        # deltaAhead = int.from_bytes(data[65:69], byteorder='little', signed=True) # S32
        # deltaBehind = int.from_bytes(data[69:73], byteorder='little', signed=True)# S32
        # lapProgress = struct.unpack('f', data[73:77]) #float
        # reserved2 = int.from_bytes(data[77:80]) #3
        
        # print("lapTimeCurrent: ", lapTimeCurrent)
        # print("lapTimePenaltyCurrent", lapTimePenaltyCurrent)
        # print("lapTimeLast: ", lapTimeLast)
        # print("lapTimeBest: ", lapTimeBest)
        # print("lapBest: ", lapBest)
        # print("deltaAhead: ", deltaAhead)
        # print("deltaBehind: ", deltaBehind)
        # print("lapProgress: ", lapProgress)
        # print("reserved2: ", reserved2)

        # print("===TimingSectors===")
        # timingSectors = data[80:116]
        # sectorTimeCurrentLap1 = int.from_bytes(data[80:84], byteorder='little', signed=False)# U32
        # sectorTimeCurrentLap2 = int.from_bytes(data[84:88], byteorder='little', signed=False)# U32
        # sectorTimeLastLap1 = int.from_bytes(data[88:92], byteorder='little', signed=False)# U32
        # sectorTimeLastLap2 = int.from_bytes(data[92:96], byteorder='little', signed=False)# U32
        # sectorTimeBestLap1 = int.from_bytes(data[96:100], byteorder='little', signed=False)# U32
        # sectorTimeBestLap2 = int.from_bytes(data[100:104], byteorder='little', signed=False)# U32
        # sectorTimeBest1 = int.from_bytes(data[104:108], byteorder='little', signed=False)# U32
        # sectorTimeBest2 = int.from_bytes(data[108:112], byteorder='little', signed=False)# U32
        # sectorTimeBest3 = int.from_bytes(data[112:116], byteorder='little', signed=False)# U32
        # print("sectorTimeCurrentLap1: ", sectorTimeCurrentLap1)
        # print("sectorTimeCurrentLap2", sectorTimeCurrentLap2)
        # print("sectorTimeLastLap1: ", sectorTimeLastLap1)
        # print("sectorTimeLastLap2: ", sectorTimeLastLap2)
        # print("sectorTimeBestLap1: ", sectorTimeBestLap1)
        # print("sectorTimeBest1: ", sectorTimeBest1)
        # print("sectorTimeBest2: ", sectorTimeBest2)
        # print("sectorTimeBest3: ", sectorTimeBest3)

        # print("===Info===")
        # info = data[116:326]
        # carId = data[116:180].decode("utf-8") #char[64]
        # carName = data[180:276].decode("utf-8") #char[96]
        # playerName = data[276:300].decode("utf-8") #char[96]
        # participantIndex = data[300]# U8
        # lastNormalTrackStatusTime = int.from_bytes(data[301:305], byteorder='little', signed=True)# S32
        # lastCollisionTime = int.from_bytes(data[305:309], byteorder='little', signed=True)# S32
        # lastResetTime = int.from_bytes(data[309:313], byteorder='little', signed=True)# S32
        # reserved3 = int.from_bytes(data[313:329]) #16

        # print("carId: ", carId)
        # print("carName: ", carName)
        # print("playerName: ", playerName)
        # print("participantIndex: ", participantIndex)
        # print("lastNormalTrackStatusTime: ", lastNormalTrackStatusTime)
        # print("lastCollisionTime: ", lastCollisionTime)
        # print("lastResetTime: ", lastResetTime)
        # print("reserved3: ", reserved3)

        # print("===Damage===")
        # damage = data[329:351]
        # damageStates = data[329:351] # U8[DAMAGE_BYTES_PER_PARTICIPANT] : (56 * 3 + 7) / 8 = 21.875;
        # print("damageStates: ", damageStates)

        # print("===Car Full (carPlayer)===")

        # print("===Car (Assists)===")
        # assists = data[351:356]
        # flags = data[351] # AssistFlags #U8
        # assistGearbox = data[352]# AssistGearbox #U8
        # levelAbs = data[353]# AssistLevel #U8
        # levelTcs = data[354]# AssistLevel #U8
        # levelEsc = data[355]# AssistLevel #U8
        # reserved4 = int.from_bytes(data[356:359]) #3

        # print("assists: ", assists)
        # print("flags: ", flags)
        # print("assistGearbox: ", assistGearbox)
        # print("levelAbs: ", levelAbs)
        # print("levelTcs: ", levelTcs)
        # print("levelEsc: ", levelEsc)
        # print("reserved4: ", reserved4)

        # print("===Car (Chassis)===")
        # chassis = data[359:410]
        # # trackWidths = struct.unpack('f', data[359:367]) #float[AXLE_LOCATION_COUNT] 2 * 4
        # trackWidth1 = struct.unpack('f', data[359:363]) #
        # trackWidth2 = struct.unpack('f', data[363:367]) #
        # wheelBase = struct.unpack('f', data[367:371]) #float
        # steeringWheelLockToLock = int.from_bytes(data[371:375], byteorder='little', signed=True)# S32
        # steeringLock = int.from_bytes(data[374:378], byteorder='little', signed=True)# S32
        # # cornerWeights = struct.unpack('f', data[378:394]) #float[AXLE_LOCATION_COUNT] 4 * 4
        # reserved5 = int.from_bytes(data[394:410]) #16

        # print("chassis: ", chassis)
        # # print("trackWidths: ", trackWidths)
        # print("trackWidth1: ", trackWidth1)
        # print("trackWidth2: ", trackWidth2)
        # print("steeringWheelLockToLock: ", steeringWheelLockToLock)
        # print("steeringLock: ", steeringLock)
        # # print("cornerWeights: ", cornerWeights)
        # print("reserved5: ", reserved5)

        # print("===Car (Driveline)===")
        # driveline = data[410:434]
        # drivelineType = data[410] # DrivelineType #U8
        # gear = data[411] # U8 gear; // 0 = R, 1 = N, 2 = 1st...
        # gearMax = data[412] # U8
        # speed = struct.unpack('f', data[413:417]) #float m/s
        # reserved6 = int.from_bytes(data[417:434]) #17

        # print("drivelineType: ", drivelineType)
        print("gear: ", gear)
        print("gearMax: ", gearMax)
        print("speed: ", speed)
        print("reserved6: ", reserved6)
        
        print("===Car (Engine)===")
        engineFlags = data[434] # U8
        self.rpm = int.from_bytes(data[435:439], byteorder='little', signed=True)# S32
        self.rpmMax = int.from_bytes(data[439:443], byteorder='little', signed=True)# S32
        print("engineFlags: ", engineFlags)
        # print("rpm: ", self.rpm)
        # print("rpmMax: ", self.rpmMax)
        # print("rpm ratio: ", self.calc_rpm_percent())

        print("===Car (Input)===")
        

        return self.calc_rpm_percent()
