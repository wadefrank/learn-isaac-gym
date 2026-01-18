from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg


class G1Cfg(LeggedRobotCfg):
    class env(LeggedRobotCfg.env):
        num_actions = 29    # 自由度
    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0, 0.0, 0.76]  # x,y,z [m]
        # stand_pos_joint_angles
        default_joint_angles = {  # = target angles [rad] when action = 0.0
            'left_hip_pitch_joint': -0.312,
            'left_hip_roll_joint': 0.0,
            'left_hip_yaw_joint': 0.,
            'left_knee_joint': 0.669,
            'left_ankle_pitch_joint': -0.363,
            'left_ankle_roll_joint': 0.0,

            'right_hip_pitch_joint': -0.312,
            'right_hip_roll_joint': -0.,
            'right_hip_yaw_joint': 0.,
            'right_knee_joint': 0.669,
            'right_ankle_pitch_joint': -0.363,
            'right_ankle_roll_joint': 0.0,

            'waist_yaw_joint': 0.0,
            'waist_roll_joint': 0.0,
            'waist_pitch_joint': 0.0,

            'left_shoulder_pitch_joint':0.2,
            'left_shoulder_roll_joint':0.2,
            'left_shoulder_yaw_joint':0.0,
            'left_elbow_joint':0.6,
            'left_wrist_roll_joint': 0.0,
            'left_wrist_pitch_joint': 0.0,
            'left_wrist_yaw_joint': 0.0,

            'right_shoulder_pitch_joint':0.2,
            'right_shoulder_roll_joint':-0.2,
            'right_shoulder_yaw_joint':0.0,
            'right_elbow_joint':0.6,
            'right_wrist_roll_joint': 0.0,
            'right_wrist_pitch_joint': 0.0,
            'right_wrist_yaw_joint': 0.0,
        }

    class control(LeggedRobotCfg.control):
        # control_type = 'actuator_net'  # P: position, actuator_net
        control_type = 'P'
        # PD Drive parameters:
        stiffness = {'hip_roll': 100.0, 'hip_yaw': 40.0, 'hip_pitch': 40., 'knee': 100., 'ankle_pitch': 30.0,
                     'ankle_roll': 30.0, 'waist_yaw': 40.0, 'waist_roll':30.0, 'waist_pitch':30.0,
                     'shoulder_pitch': 14.0, 'shoulder_roll': 14.0, 'shoulder_yaw': 14.0,
                     'elbow': 14.0, 'wrist_roll': 14.0, 'wrist_pitch': 17.0, 'wrist_yaw': 17.0
                     }  # [N*m/rad]

        damping = {'hip_roll': 6.3, 'hip_yaw': 2.5, 'hip_pitch': 2.5, 'knee': 6.3, 'ankle_pitch': 2.,
                   'ankle_roll': 2., 'waist_yaw': 2.5, 'waist_roll':2.0, 'waist_pitch':2.0,
                   'shoulder_pitch': 0.9, 'shoulder_roll': 0.9, 'shoulder_yaw': 0.9,
                   'elbow': 0.9, 'wrist_roll': 0.9, 'wrist_pitch': 1.0, 'wrist_yaw': 1.0
                   }  # [N*m*s/rad]

        # torque_limits = {
        #     'HAA': 30.,
        #     'HFE': 30.,
        #     'KFE': 30.,
        # }     # [N*m]

        action_scale = 0.5  # [1.5, 2., 2.]*4
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4
        enable_action_interpolation = False

    class asset(LeggedRobotCfg.asset):
        file = '{PROJECT_ROOT_DIR}/resources/robots/g1/urdf/g1.urdf'
        name = "humanoid"
        foot_name = 'ankle_roll'
        thigh_name = 'hip_pitch'
        shin_name = 'knee_pitch'
        # torso_name = 'waistRoll'
        upper_arm_name = 'shoulder_roll'
        lower_arm_name = 'elbow_pitch'
        # terminate_after_contacts_on = ['pelvis', 'shoulder_roll', 'elbow_pitch', 'knee_pitch']
        terminate_after_contacts_on = ['pelvis']    # 骨盆
        flip_visual_attachments = False
        self_collisions = 1  # 1 to disable, 0 to enable...bitwise filter

    class terrain(LeggedRobotCfg.terrain):
        mesh_type = 'plane'
        curriculum = False
        selected = True
        horizontal_scale = 0.05
        num_rows = 1
        num_cols = 1
