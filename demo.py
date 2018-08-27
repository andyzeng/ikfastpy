import numpy as np
import ikfastpy

# Initialize kinematics for UR5 robot arm
ur5_kin = ikfastpy.PyKinematics()
n_joints = ur5_kin.getDOF()

joint_angles = [-3.1,-1.6,1.6,-1.6,-1.6,0.] # in radians

# Test forward kinematics: get end effector pose from joint angles
print("\nTesting forward kinematics:\n")
print("Joint angles:")
print(joint_angles)
ee_pose = ur5_kin.forward(joint_angles)
ee_pose = np.asarray(ee_pose).reshape(3,4) # 3x4 rigid transformation matrix
print("\nEnd effector pose:")
print(ee_pose)
print("\n-----------------------------")

# Test inverse kinematics: get joint angles from end effector pose
print("\nTesting inverse kinematics:\n")
joint_configs = ur5_kin.inverse(ee_pose.reshape(-1).tolist())
n_solutions = int(len(joint_configs)/n_joints)
print("%d solutions found:"%(n_solutions))
joint_configs = np.asarray(joint_configs).reshape(n_solutions,n_joints)
for joint_config in joint_configs:
    print(joint_config)
assert(np.any([np.sum(np.abs(joint_config-np.asarray(joint_angles))) < 1e-4 for joint_config in joint_configs]))
print("\nTest passed!")
# joint_configs = ur5_kin.inverse([0.04071115,-0.99870914,0.03037599,0.472,
#                                 -0.99874455,-0.04156303,-0.02796067,0.12648243,
#                                 0.0291871,-0.02919955,-0.99914742,0.43451169])