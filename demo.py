import numpy as np
import ikfastpy

# Initialize kinematics for UR5 robot arm
ur5_kin = ikfastpy.PyKinematics()
num_joints = ur5_kin.getDOF()

# Test forward kinematics
ee_pose = ur5_kin.forward([-3.1,-1.6,1.6,-1.6,-1.6,0])
ee_pose = np.asarray(ee_pose).reshape(3,4)
print("\nForward kinematics:\n")
print(ee_pose)

# Test inverse kinematics
print("\nInverse kinematics:\n")
joint_configs = ur5_kin.inverse([0.04071115,-0.99870914,0.03037599,0.472,-0.99874455,-0.04156303,-0.02796067,0.12648243,0.0291871,-0.02919955,-0.99914742,0.43451169])
num_solutions = len(joint_configs)/num_joints
joint_configs = np.asarray(joint_configs).reshape(num_solutions,num_joints)
print(joint_configs)