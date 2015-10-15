# Simple regression model in R
# Load the voxel time course
voxels = read.table('voxel_time_course.txt')$V1
# Load the convolved regressor
convolved = read.table('ds114_sub009_t2r1_conv.txt')$V1
# Drop the first four values to correspond to the data
convolved = convolved[-(1:4)]
# Fit linear model
res = lm(voxels ~ convolved)
print(summary(res))
