# Single source of truth (v2, 11-08) for Maela Walk / Run / JumpUp / Fall / Lantern.
# Rotation = localEulerAngles.z in degrees (Unity, +CCW; Maela faces +x).
# Position = localPosition (units) - only Hip.y and Body.y are animated.
HIP_Y = 0.565
CLIPS = {
 # v2 (11-08): Walk = upright, small swing, near-straight legs. Run = more lean, back leg bent, front leg slightly bent.
 "Maela_Walk": dict(length=0.9, loop=True, keys={
   # t:       0     .225   .45    .675   .9
   "Hip:y":   [0.559,0.566,0.559,0.566,0.559],
   "Hip/Body":[-1,-2,-1,-2,-1],
   "Hip/Body/Head":[1,1,1,1,1],
   "Hip/Thigh_R":[10,0,-9,0,10],
   "Hip/Thigh_R/Shin_R":[-3,-2,-8,-18,-3],
   "Hip/Thigh_R/Shin_R/Foot_R":[3,0,-5,-3,3],
   "Hip/Thigh_L":[-9,0,10,0,-9],
   "Hip/Thigh_L/Shin_L":[-8,-18,-3,-2,-8],
   "Hip/Thigh_L/Shin_L/Foot_L":[-5,-3,3,0,-5],
   "Hip/Body/Shoulder_R":[-2,1,5,1,-2],
   "Hip/Body/Shoulder_R/Elbow_R":[5,6,5,6,5],
   "Hip/Body/Shoulder_R/Elbow_R/Wrist_R/Lantern":[5,1,-5,-1,5],
   "Hip/Body/Shoulder_L":[3,0,-6,0,3],
 }),
 "Maela_Run": dict(length=0.5, loop=True, keys={
   # t:       0     .125   .25    .375   .5
   "Hip:y":   [0.546,0.578,0.546,0.578,0.546],
   "Hip/Body":[-10,-12,-10,-12,-10],
   "Hip/Body/Head":[6,8,6,8,6],
   "Hip/Thigh_R":[18,2,-14,2,18],
   "Hip/Thigh_R/Shin_R":[-14,-8,-28,-52,-14],
   "Hip/Thigh_R/Shin_R/Foot_R":[8,2,-14,-8,8],
   "Hip/Thigh_L":[-14,2,18,2,-14],
   "Hip/Thigh_L/Shin_L":[-28,-52,-14,-8,-28],
   "Hip/Thigh_L/Shin_L/Foot_L":[-14,-8,8,2,-14],
   "Hip/Body/Shoulder_R":[-4,2,10,2,-4],
   "Hip/Body/Shoulder_R/Elbow_R":[8,10,8,10,8],
   "Hip/Body/Shoulder_R/Elbow_R/Wrist_R/Lantern":[12,2,-12,-2,12],
   "Hip/Body/Shoulder_L":[6,0,-12,0,6],
 }),
 "Maela_JumpUp": dict(length=0.3, loop=False, times=[0,0.12,0.3], keys={
   "Hip/Body":[0,-6,-4],
   "Hip/Body/Head":[0,5,4],
   "Hip/Thigh_R":[0,24,22],
   "Hip/Thigh_R/Shin_R":[0,-55,-50],
   "Hip/Thigh_R/Shin_R/Foot_R":[0,-10,-8],
   "Hip/Thigh_L":[0,-7,-5],
   "Hip/Thigh_L/Shin_L":[0,-24,-30],
   "Hip/Thigh_L/Shin_L/Foot_L":[0,-20,-16],
   "Hip/Body/Shoulder_R":[0,14,12],
   "Hip/Body/Shoulder_R/Elbow_R":[0,2,2],
   "Hip/Body/Shoulder_R/Elbow_R/Wrist_R/Lantern":[0,-26,-18],
   "Hip/Body/Shoulder_L":[0,-12,-10],
 }),
 "Maela_Fall": dict(length=0.6, loop=True, times=[0,0.3,0.6], keys={
   "Hip/Body":[3,4,3],
   "Hip/Body/Head":[-3,-4,-3],
   "Hip/Thigh_R":[11,13,11],
   "Hip/Thigh_R/Shin_R":[-26,-22,-26],
   "Hip/Thigh_R/Shin_R/Foot_R":[8,10,8],
   "Hip/Thigh_L":[3,1,3],
   "Hip/Thigh_L/Shin_L":[-14,-18,-14],
   "Hip/Thigh_L/Shin_L/Foot_L":[4,6,4],
   "Hip/Body/Shoulder_R":[10,13,10],
   "Hip/Body/Shoulder_R/Elbow_R":[2,3,2],
   "Hip/Body/Shoulder_R/Elbow_R/Wrist_R/Lantern":[2,8,2],
   "Hip/Body/Shoulder_L":[-14,-18,-14],
 }),
 # Option A (11-07): no arm raise. Lantern pushed forward a little, a small lift + flare of light.
 "Maela_Lantern": dict(length=1.1, loop=False, times=[0,0.2,0.32,0.75,1.1], keys={
   "Hip:y":[HIP_Y,0.557,HIP_Y+0.004,HIP_Y+0.004,HIP_Y],
   "Hip/Body":[0,-3,-2,-2,0],
   "Hip/Body/Head":[0,-2,3,3,0],
   "Hip/Body/Shoulder_R":[0,10,16,15,0],
   "Hip/Body/Shoulder_R/Elbow_R":[0,2,3,3,0],
   "Hip/Body/Shoulder_R/Elbow_R/Wrist_R/Lantern":[0,-6,-19,-14,0],
   "LIGHT":[1.0,1.3,2.6,1.9,1.0],
 }),
}
LIGHT_PATH = "Hip/Body/Shoulder_R/Elbow_R/Wrist_R/Lantern/LanternLight"
