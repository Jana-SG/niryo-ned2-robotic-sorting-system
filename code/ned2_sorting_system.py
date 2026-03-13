# !/usr/bin/env python

from niryo_robot_python_ros_wrapper.ros_wrapper import *
import sys
import rospy

rospy.init_node('niryo_blockly_interpreted_code')
n = NiryoRosWrapper()

n.calibrate_auto()

from numbers import Number

Red_stack = None
Blue_stack = None


n.highlight_block('i.wp8fn*yE4dzaI.z6Uc')
n.update_tool()
n.highlight_block('j%EaMPZE3_spe=DY:|T7')
n.set_conveyor()
n.wait(2)
n.highlight_block('z(L*f30$X~]p*%a(i^VR')
Red_stack = 1
n.highlight_block('ga2{QALz`l8Of2v~i:9J')
Blue_stack = 1
n.highlight_block('gr~7PD2W#K7c!r76DYMB')
for count in range(9):
  n.highlight_block('746qW~NQPt/#R+e!XQFi')
  n.open_gripper(500, 100, 100)
  n.highlight_block('#7A+~r$w$g9C?*nRvui(')
  n.move_joints(*[0.771, -0.347, -0.304, 0.385, -1, 0.578])
  n.highlight_block('LGI0px5Z_7S+TZdDBc4;')
  n.close_gripper(500, 100, 100)
  n.highlight_block('HZ=[+dG7|xjGHGop0PV_')
  n.move_pose(*[0.176, 0.191, 0.309, 0.62, 0.982, 1.061])
  n.highlight_block('!@]x.(u):USOAon}9t:G')
  n.move_pose(*[0.269, 0.13, 0.202, -0.493, 1.435, 0.978])
  n.highlight_block('MS3u}w`]Um*Oy_A1:]c%')
  n.open_gripper(500, 100, 100)
  n.highlight_block('d-~+*^~RZI!Psr+JAn$r')
  n.move_pose(*[0.14, 0, 0.203, 0, 0.759, -0.001])
  n.highlight_block('0}bjPg$=nfrWB[cZpvup')
  n.close_gripper(500, 100, 100)
  n.highlight_block('X$+%e*xo+EC[`y|xHICc')
  n.control_conveyor(ConveyorID.ID_1, True, 100, ConveyorDirection.BACKWARD)
  n.highlight_block('SPvurlHNo4RO/=tjTOcw')
  while n.digital_read('DI5'):
    n.highlight_block('SPvurlHNo4RO/=tjTOcw')
  n.highlight_block('lPOAXsqKcqY*SH^[0$x^')
  n.control_conveyor(ConveyorID.ID_1, False, 0, 1)
  n.highlight_block('{Ug6ywZ!?x%-U,m/op8P')
  # Move to an observation position then
  n.highlight_block('+PD9eoRP}_pAh?PehWM+')
  n.move_pose(*[0.127, (-0.064), 0.305, -0.611, 1.496, -0.547])
  n.highlight_block('AK0pwNqy89k?+W912ZlX')
  if n.vision_pick('', 9/1000.0, ObjectShape.ANY, ObjectColor.RED)[0]:
    n.highlight_block('s5$p._c^|ZyFmoV#AwLn')
    # If the pick is successful,
    n.highlight_block('k;`kT}-:mp(5g5[K8$E:')
    n.led_ring.solid([153,51,0,0], wait=False)
    n.highlight_block('P0`d0RP?K-$FF?{5OqvJ')
    n.move_pose(*[0.004, (-0.208), 0.228, -0.055, 1.31, -1.675])
    n.highlight_block('C!TrRjS`a~c^r{WtcjF]')
    n.place_from_pose(*[0.04, (-0.292), (0.115 + Red_stack * 0.01), -0.627, 1.502, -2.186])
    n.highlight_block('zNpQ4Dr_Oa+QursLDHx6')
    if True:
      n.highlight_block('z(U]Zj1Ze1:A_cOCW[eC')
      Red_stack = (Red_stack if isinstance(Red_stack, Number) else 0) + (Red_stack + 1)
  n.highlight_block('{5e`gWEV[!!y=@B!7URw')
  if n.vision_pick('', 9/1000.0, ObjectShape.ANY, ObjectColor.BLUE)[0]:
    n.highlight_block('TU`T#$Wak/ZkLo085z0[')
    # If the pick is successful,
    n.highlight_block('xN^pz0COq$b?GkU,mKV_')
    n.led_ring.solid([0,0,153,0], wait=False)
    n.highlight_block(';-I9lCgta!3y^s#=PccK')
    n.move_pose(*[0.004, (-0.208), 0.228, -0.055, 1.31, -1.675])
    n.highlight_block('0{ms3blFn;]exOPr`Xi8')
    n.place_from_pose(*[(-0.065), (-0.286), (0.095 + Blue_stack * 0.01), -0.013, 1.478, -1.611])
    n.highlight_block('QX688@9_?G^912,/c%~?')
    if True:
      n.highlight_block('_!oJrM]tp6mWLGZ*9|,y')
      Blue_stack = (Blue_stack if isinstance(Blue_stack, Number) else 0) + (Blue_stack + 1)
  n.highlight_block(']+%^Mr`x4Q@x6JX,yH9c')
  if n.vision_pick('', 9/1000.0, ObjectShape.ANY, ObjectColor.GREEN)[0]:
    n.highlight_block('D3!kn]D1.Wt;^)k^5d~=')
    # If the pick is successful,
    n.highlight_block('xO?h2[jAL4gR[oeJ%t9[')
    n.led_ring.solid([0,102,0,0], wait=False)
    n.highlight_block('0]FFd#}qSURmx;L;SwBO')
    n.place_from_pose(*[(-0.191), (-0.227), 0.176, 0.519, 1.321, -2.547])
  n.highlight_block(']LQ$Yc9SY^~[Q.Hhxv(H')
  n.move_pose(*[0.004, (-0.208), 0.228, -0.055, 1.31, -1.675])
  n.highlight_block('gr~7PD2W#K7c!r76DYMB')
 
