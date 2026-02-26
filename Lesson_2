"""
 ██╗  ██╗██╗  ██╗██████╗ ██╗  ██╗██╗   ██╗██████╗ 
 ██║ ██╔╝██║ ██╔╝██╔══██╗██║  ██║██║   ██║██╔══██╗
 █████╔╝ █████╔╝ ██████╔╝███████║██║   ██║██████╔╝
 ██╔═██╗ ██╔═██╗ ██╔══██╗██╔══██║██║   ██║██╔══██╗
 ██║  ██╗██║  ██╗██║  ██║██║  ██║╚██████╔╝██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝
 
ไจโล วิ่งตรงต่อ หมุนขวา 90° วิ่งตรงโดยคุมมุมให้อยู่ที่ 0°
"""
# ---------- นำเข้าเครื่องมือ ----------
from pybricks.hubs import PrimeHub          # ใช้ควบคุม Hub และ Gyro
from pybricks.pupdevices import Motor       # ใช้ควบคุมมอเตอร์
from pybricks.parameters import Port        # ใช้กำหนดพอร์ต
from pybricks.tools import wait             # ใช้หน่วงเวลา

# ---------- สร้างอุปกรณ์ ----------
hub = PrimeHub()                # สร้างตัวแปรควบคุม Hub

left_motor = Motor(Port.A)      # มอเตอร์ซ้ายเสียบพอร์ต A
right_motor = Motor(Port.B)     # มอเตอร์ขวาเสียบพอร์ต B

# ==========================================
# ฟังก์ชัน: วิ่งตรงด้วย Gyro (PRO VERSION)
# ==========================================
def gyro_straight(target_angle, speed):
    
    hub.imu.reset_heading(0)        # รีเซ็ตค่า Gyro ให้เริ่มที่ 0 องศา
    
    while True:                     # ทำงานวนลูปตลอด
        
        current_angle = hub.imu.heading()   # อ่านค่ามุมปัจจุบันจาก Gyro
        
        error = target_angle - current_angle
        # error คือค่าความคลาดเคลื่อน
        # ถ้ารถเบี้ยวขวา → current_angle เป็นบวก
        # error จะเป็นลบ → ดึงกลับ
        
        correction = error * 2
        # ตัวคูณ 2 คือค่า P (ปรับได้)
        # ถ้ารถแกว่งแรง → ลดค่า
        # ถ้ารถดึงช้า → เพิ่มค่า
        
        left_motor.run(speed - correction)
        # ลดความเร็วล้อซ้ายตามค่า correction
        
        right_motor.run(speed + correction)
        # เพิ่มความเร็วล้อขวาตามค่า correction
        
        if abs(left_motor.angle()) > 720:
            # 720 องศามอเตอร์ ≈ 1 รอบล้อ
            # เปลี่ยนค่าได้ตามระยะที่ต้องการ
            break
    
    left_motor.stop()    # หยุดมอเตอร์ซ้าย
    right_motor.stop()   # หยุดมอเตอร์ขวา


# ==========================================
# ฟังก์ชัน: เลี้ยวด้วย Gyro (PRO VERSION)
# ==========================================
def gyro_turn(angle, speed):
    
    hub.imu.reset_heading(0)    # รีเซ็ต Gyro ก่อนเริ่มหมุน
    
    while abs(hub.imu.heading()) < angle:
        # หมุนจนกว่าจะถึงมุมที่กำหนด
        
        left_motor.run(speed)       # ล้อซ้ายหมุนไปหน้า
        right_motor.run(-speed)     # ล้อขวาหมุนถอยหลัง
        # ทำให้รถหมุนอยู่กับที่
    
    left_motor.stop()    # หยุดล้อซ้าย
    right_motor.stop()   # หยุดล้อขวา


# ==========================================
# ตัวอย่างการใช้งานจริง (สนามแข่ง)
# ==========================================

gyro_straight(0, 400)   # วิ่งตรงโดยคุมมุมให้อยู่ที่ 0°
wait(500)
#       target_angle, speed | ของทุกอันเป็นแบบนี้
gyro_turn(90, 200)      # หมุนขวา 90°
wait(500)

gyro_straight(0, 400)   # วิ่งตรงต่อ
