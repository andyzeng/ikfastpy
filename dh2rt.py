import numpy as np









# Convert from rotation matrix to quaternion (w,x,y,z)
def rotm2quat(matrix,isprecise=False):
    # From: Christoph Gohlke

    M = np.array(matrix, dtype=np.float64, copy=False)[:4, :4]
    if isprecise:
        q = np.empty((4, ))
        t = np.trace(M)
        if t > M[3, 3]:
            q[0] = t
            q[3] = M[1, 0] - M[0, 1]
            q[2] = M[0, 2] - M[2, 0]
            q[1] = M[2, 1] - M[1, 2]
        else:
            i, j, k = 0, 1, 2
            if M[1, 1] > M[0, 0]:
                i, j, k = 1, 2, 0
            if M[2, 2] > M[i, i]:
                i, j, k = 2, 0, 1
            t = M[i, i] - (M[j, j] + M[k, k]) + M[3, 3]
            q[i] = t
            q[j] = M[i, j] + M[j, i]
            q[k] = M[k, i] + M[i, k]
            q[3] = M[k, j] - M[j, k]
            q = q[[3, 0, 1, 2]]
        q *= 0.5 / math.sqrt(t * M[3, 3])
    else:
        m00 = M[0, 0]
        m01 = M[0, 1]
        m02 = M[0, 2]
        m10 = M[1, 0]
        m11 = M[1, 1]
        m12 = M[1, 2]
        m20 = M[2, 0]
        m21 = M[2, 1]
        m22 = M[2, 2]
        # symmetric matrix K
        K = np.array([[m00-m11-m22, 0.0,         0.0,         0.0],
                         [m01+m10,     m11-m00-m22, 0.0,         0.0],
                         [m02+m20,     m12+m21,     m22-m00-m11, 0.0],
                         [m21-m12,     m02-m20,     m10-m01,     m00+m11+m22]])
        K /= 3.0
        # quaternion is eigenvector of K that corresponds to largest eigenvalue
        w, V = np.linalg.eigh(K)
        q = V[[3, 0, 1, 2], np.argmax(w)]
    if q[0] < 0.0:
        np.negative(q, q)
    return q





# columns: theta, a, d, alpha
dhparams = np.array([[0, 0,        0.089159, np.pi/2],
                     [0, -0.425,   0,        0],
                     [0, -0.39225, 0,        0],
                     [0,  0,       0.10915,  np.pi/2],
                     [0,  0,       0.09465, -np.pi/2],
                     [0,  0,       0.0823,   0]])

for link_dhparams in dhparams:

    theta = link_dhparams[0] # in radians
    a = link_dhparams[1] # in meters
    d = link_dhparams[2] # in meters
    alpha = link_dhparams[3] # in radians




    rotm = np.array([[np.cos(theta), -np.sin(theta)*np.cos(alpha),  np.sin(theta)*np.sin(alpha)],
                     [np.sin(theta),  np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha)],
                     [0,              np.sin(alpha),                np.cos(alpha)]])
    trans = np.array([a*np.cos(theta), a*np.sin(theta), d])





    print(trans)
    print(rotm2quat(rotm))

    print()