"""
 ██╗  ██╗██╗  ██╗██████╗ ██╗  ██╗██╗   ██╗██████╗ 
 ██║ ██╔╝██║ ██╔╝██╔══██╗██║  ██║██║   ██║██╔══██╗
 █████╔╝ █████╔╝ ██████╔╝███████║██║   ██║██████╔╝
 ██╔═██╗ ██╔═██╗ ██╔══██╗██╔══██║██║   ██║██╔══██╗
 ██║  ██╗██║  ██╗██║  ██║██║  ██║╚██████╔╝██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝
 
ไจโล PID
"""


from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# ==============================
#  GYRO  WITH PID
# ==============================
def gyro_straight_pid(distance, speed):

    hub.imu.reset_heading(0)        # รีเซ็ตมุม
    left_motor.reset_angle(0)       # รีเซ็ตระยะมอเตอร์
    
    # ----- ค่าปรับจูน (ต้องทดลองเอง) -----
    Kp = 2.0      # แรงดึงหลัก
    Ki = 0.02     # แก้ error สะสม
    Kd = 0.8      # กันการแกว่ง
    
    integral = 0          # เก็บค่า error สะสม
    last_error = 0        # เก็บ error รอบก่อน
    
    while abs(left_motor.angle()) < distance:
        
        current_angle = hub.imu.heading()    # อ่านมุมปัจจุบัน
        error = 0 - current_angle            # ต้องการรักษาที่ 0°
        
        integral += error                    # สะสม error
        
        derivative = error - last_error      # ดูการเปลี่ยนแปลง
        
        correction = (Kp * error) + (Ki * integral) + (Kd * derivative)
        # รวม 3 ส่วนเป็นค่าแก้ไข
        
        left_motor.run(speed - correction)
        right_motor.run(speed + correction)
        
        last_error = error                   # เก็บค่าไว้รอบหน้า
    
    left_motor.stop()
    right_motor.stop()


# ===== ตัวอย่างใช้งาน =====
gyro_straight_pid(720, 400)