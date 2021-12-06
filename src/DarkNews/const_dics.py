################################################
# NUCLEAR FORM FACTORS -- 
# http://discovery.phys.virginia.edu/research/groups/ncd/index.html
# data from Nuclear Data Tables (74, 87, and 95)
from numpy import array

fourier_bessel_dic = {
 'h3': array([0.025182, 0.034215, 0.015257, 0.      , 0.      , 0.      ,
        0.      , 0.      , 0.      , 0.      , 0.      , 0.      ,
        0.      , 0.      , 0.      , 0.      , 0.      , 3.5     ]),
 'he3': array([9.9442e-03, 2.0829e-02, 1.8008e-02, 8.9117e-03, 2.3151e-03,
        2.3263e-03, 2.5850e-03, 1.9014e-03, 1.2746e-03, 7.0446e-04,
        3.0493e-04, 1.1389e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
        0.0000e+00, 0.0000e+00, 5.0000e+00]),
 'li6': array([ 1.6353e-02,  2.9603e-02,  2.0807e-02,  7.2731e-03,  4.7580e-04,
        -8.7510e-04,  1.1413e-03,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  6.0000e+00]),
 'b10': array([1.3296e-02, 3.3636e-02, 3.5841e-02, 2.5432e-02, 1.5516e-02,
        9.0030e-03, 5.2231e-03, 2.9666e-03, 1.7294e-03, 0.0000e+00,
        0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
        0.0000e+00, 0.0000e+00, 8.0000e+00]),
 'c12': array([ 1.5737e-02,  3.8897e-02,  3.7085e-02,  1.4795e-02, -4.4831e-03,
        -1.0057e-02, -6.8696e-03, -2.8813e-03, -7.7229e-04,  6.6908e-05,
         1.0636e-04, -3.6864e-05, -5.0135e-06,  9.4550e-06, -4.7687e-06,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 'n15': array([ 2.5491e-02,  5.0618e-02,  2.9822e-02, -5.5196e-03, -1.5913e-02,
        -7.6184e-03, -2.3992e-03, -4.7940e-04,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  7.0000e+00]),
 'o16': array([ 2.0238e-02,  4.4793e-02,  3.3533e-02,  3.5030e-03, -1.2293e-02,
        -1.0329e-02, -3.4036e-03, -4.1627e-04, -9.4435e-04, -2.5771e-04,
         2.3759e-04, -1.0603e-04,  4.1480e-05,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 'al27': array([ 4.3418e-02,  6.0298e-02,  2.8950e-03, -2.3522e-02, -7.9791e-03,
         2.3010e-03,  1.0794e-03,  1.2574e-04, -1.3021e-04,  5.6563e-05,
        -1.8011e-05,  4.2869e-06,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  7.0000e+00]),
 'si28': array([ 3.3495e-02,  5.9533e-02,  2.0979e-02, -1.6900e-02, -1.4998e-02,
        -9.3248e-04,  3.3266e-03,  5.9244e-04, -4.0013e-04,  1.2242e-04,
        -1.2994e-05, -9.2784e-06,  7.2595e-06, -4.2096e-06,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 'si29': array([ 3.3521e-02,  5.9679e-02,  2.0593e-02, -1.8646e-02, -1.6550e-02,
        -1.1922e-03,  2.8025e-03, -6.7353e-05, -3.4619e-04,  1.7611e-04,
        -5.7173e-06,  1.2371e-05,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 'si30': array([ 2.8397e-02,  5.4163e-02,  2.5167e-02, -1.2858e-02, -1.7592e-02,
        -4.6722e-03,  2.4804e-03,  1.4760e-03, -3.0168e-04,  4.8346e-05,
         0.0000e+00, -5.1570e-06,  3.0261e-06,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  8.5000e+00]),
 'p31': array([ 3.5305e-02,  5.9642e-02,  1.7274e-02, -1.9303e-02, -1.3545e-02,
         6.3209e-04,  3.5462e-03,  8.3653e-04, -4.7904e-04,  1.9099e-04,
        -6.9611e-05,  2.3196e-05, -7.7780e-06,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 's32': array([ 3.7251e-02,  6.0248e-02,  1.4748e-02, -1.8352e-02, -1.0347e-02,
         3.0461e-03,  3.5277e-03, -3.9834e-05, -9.7177e-05,  9.2279e-05,
        -5.1931e-05,  2.2958e-05, -8.6609e-06,  2.8879e-06, -8.6632e-07,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 's34': array([ 3.7036e-02,  5.8506e-02,  1.2082e-02, -1.9022e-02, -8.3421e-03,
         4.5434e-03,  2.8346e-03, -5.2304e-04,  2.7754e-05,  5.9403e-05,
        -4.2794e-05,  2.0407e-05, -7.9934e-06,  2.7354e-06, -8.3914e-07,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 's36': array([ 3.7032e-02,  5.7939e-02,  1.0049e-02, -1.9852e-02, -6.7176e-03,
         6.1882e-03,  3.7795e-03, -5.5272e-04, -1.2904e-04,  1.5845e-04,
        -8.4063e-05,  3.4010e-05, -1.1663e-05,  3.5204e-06, -9.5135e-07,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 'ar40': array([ 3.0451e-02,  5.5337e-02,  2.0203e-02, -1.6765e-02, -1.3578e-02,
        -4.3204e-05,  9.1988e-04, -4.1205e-04,  1.1971e-04, -1.9801e-05,
        -4.3204e-06,  6.1205e-06, -3.7803e-06,  1.8001e-06, -7.7407e-07,
         0.0000e+00,  0.0000e+00,  9.0000e+00]),
 'ca40': array([ 4.4846e-02,  6.1326e-02, -1.6818e-03, -2.6217e-02, -2.9725e-03,
         8.5534e-03,  3.5322e-03, -4.8258e-04, -3.9346e-04,  2.0338e-04,
         2.5461e-05, -1.7794e-05,  6.7394e-06, -2.1033e-06,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 'ca48': array([ 4.4782e-02,  5.9523e-02, -7.4148e-03, -2.9466e-02, -2.8350e-04,
         1.0829e-02,  3.0465e-03, -1.0237e-03, -1.7830e-04,  5.5391e-05,
        -2.2644e-05,  8.2671e-06, -2.7343e-06,  8.2461e-07, -2.2780e-07,
         0.0000e+00,  0.0000e+00,  8.0000e+00]),
 'ti48': array([ 2.7850e-02,  5.5432e-02,  2.6369e-02, -1.7091e-02, -2.1798e-02,
        -2.4889e-03,  7.6631e-03,  3.4554e-03, -6.7477e-04,  1.0764e-04,
        -1.6564e-06, -5.5566e-06,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'ti50': array([ 3.1818e-02,  5.8556e-02,  1.9637e-02, -2.4309e-02, -1.8748e-02,
         3.3741e-03,  8.9961e-03,  3.7954e-03, -4.1238e-04,  1.2540e-04,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  9.5000e+00]),
 'cr50': array([ 3.9174e-02,  6.1822e-02,  6.8550e-03, -3.0170e-02, -9.8745e-03,
         8.7944e-03,  6.8502e-03, -9.3609e-04, -2.4962e-03, -1.5361e-03,
        -7.3687e-04,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  9.0000e+00]),
 'cr52': array([ 3.9287e-02,  6.2477e-02,  6.2482e-03, -3.2885e-02, -1.0648e-02,
         1.0520e-02,  8.5478e-03, -2.4003e-04, -2.0499e-03, -1.2001e-03,
        -5.6649e-04,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  9.0000e+00]),
 'cr54': array([ 3.9002e-02,  6.0305e-02,  4.5845e-03, -3.0723e-02, -9.1355e-03,
         9.3251e-03,  6.0583e-03, -1.5602e-03, -7.6809e-04,  7.6809e-04,
        -3.4804e-04,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  9.0000e+00]),
 'fe54': array([ 4.2339e-02,  6.4428e-02,  1.5840e-03, -3.5171e-02, -1.0116e-02,
         1.2069e-02,  6.2230e-03, -1.2045e-03,  1.3561e-04,  1.0428e-05,
        -1.6980e-05,  9.1817e-06, -3.9988e-06,  1.5731e-06, -5.7862e-07,
         2.0186e-07, -6.7892e-08,  9.0000e+00]),
 'fe56': array([ 4.2018e-02,  6.2337e-02,  2.3995e-04, -3.2776e-02, -7.9941e-03,
         1.0844e-02,  4.9123e-03, -2.2144e-03, -1.8146e-04,  3.7261e-04,
        -2.3296e-04,  1.1494e-04, -5.0596e-05,  2.0652e-05, -7.9428e-06,
         2.8986e-06, -1.0075e-06,  9.0000e+00]),
 'fe58': array([ 4.1791e-02,  6.0524e-02, -1.4978e-03, -3.1183e-02, -5.8013e-03,
         1.0611e-02,  4.1629e-03, -2.9045e-06,  5.4106e-04, -3.8689e-04,
         2.0514e-04, -9.5237e-05,  4.0707e-05, -1.6346e-05,  6.2233e-06,
        -2.2568e-06,  7.8077e-07,  9.0000e+00]),
 'co59': array([ 4.3133e-02,  6.1249e-02, -3.2523e-03, -3.2681e-02, -4.9583e-03,
         1.1494e-02,  5.5428e-03,  3.1398e-04, -7.0578e-05,  5.3725e-06,
        -7.4650e-07,  1.9793e-06, -2.8059e-06,  2.7183e-06, -1.9454e-06,
         1.0963e-06, -5.1114e-07,  9.0000e+00]),
 'ni58': array([ 4.5030e-02,  6.5044e-02, -3.2843e-03, -3.6241e-02, -6.7442e-03,
         1.3146e-02,  5.0903e-03, -2.0787e-03,  1.2901e-04,  1.4828e-04,
        -1.1530e-04,  6.0881e-05, -2.7676e-05,  1.1506e-05,  4.4764e-06,
         1.6468e-06, -5.7496e-07,  9.0000e+00]),
 'ni60': array([ 4.4742e-02,  6.2987e-02,  4.2797e-03, -3.4306e-02, -4.4060e-03,
         1.2810e-02,  4.6914e-03, -8.4373e-04,  3.6928e-04, -1.5003e-04,
         5.9665e-05, -2.3215e-05,  8.8005e-06, -3.2305e-06,  1.1496e-06,
        -3.9658e-07,  1.3145e-07,  9.0000e+00]),
 'ni62': array([ 4.4581e-02,  6.1478e-02, -6.9425e-03, -3.3126e-02, -2.4964e-03,
         1.2674e-02,  3.7148e-03, -2.0881e-03,  3.0193e-04,  5.7573e-05,
        -7.7965e-05,  4.6906e-05, -2.2724e-05,  9.8243e-06, -3.9250e-06,
         1.4732e-06,  5.2344e-07,  9.0000e+00]),
 'ni64': array([ 4.4429e-02,  6.0116e-02, -9.2003e-03, -3.3452e-02, -5.2856e-04,
         1.3156e-02,  3.5152e-03,  2.1671e-03,  4.6497e-05,  2.5366e-04,
        -1.8438e-03,  9.6874e-05, -4.4224e-05,  1.8493e-05, -7.2361e-06,
         2.6740e-06, -9.3929e-07,  9.0000e+00]),
 'cu63': array([ 4.5598e-02,  6.0706e-02, -7.8616e-03, -3.1638e-02, -1.4447e-03,
         1.0953e-02,  4.2578e-03, -2.4224e-04, -3.0067e-04,  2.3903e-04,
        -1.2910e-04,  6.0195e-05, -2.5755e-05,  1.0332e-05, -3.9330e-06,
         1.4254e-06, -4.9221e-07,  9.0000e+00]),
 'cu65': array([ 4.5444e-02,  5.9544e-02, -9.4968e-03, -3.1561e-02,  2.2898e-04,
         1.1189e-02,  3.7360e-03, -6.4873e-04, -5.1133e-04,  4.3765e-04,
        -2.4276e-04,  1.1507e-04, -4.9761e-05,  2.0140e-05, -7.6945e-06,
         2.8055e-06, -9.7411e-07,  9.0000e+00]),
 'zn64': array([ 4.7038e-02,  6.1536e-02, -9.0045e-03, -3.0669e-02, -7.8705e-04,
         1.0034e-02,  1.4053e-03, -2.0640e-03,  3.5105e-04,  2.7303e-05,
        -6.3811e-05,  4.0893e-05, -2.0311e-05,  8.8986e-06, -3.5849e-06,
         1.3522e-06, -3.8635e-07,  9.0000e+00]),
 'zn66': array([ 4.6991e-02,  6.0995e-02, -9.6693e-03, -3.0457e-02, -5.3435e-04,
         9.7083e-03,  1.4091e-03, -7.0813e-04,  2.0809e-04, -4.8275e-05,
         7.2680e-06,  9.1369e-07, -1.4874e-06,  8.8831e-07, -4.1689e-07,
         1.7283e-07, -6.5968e-08,  9.0000e+00]),
 'zn68': array([ 4.6654e-02,  5.8827e-02, -1.2283e-02, -2.9865e-02,  2.5669e-03,
         1.0235e-02,  3.1861e-03, -1.7351e-04, -4.2979e-04,  3.3700e-04,
        -1.8435e-04,  8.7043e-05, -3.7612e-05,  1.5220e-05, -5.8282e-06,
         2.1230e-06, -7.3709e-07,  9.0000e+00]),
 'zn70': array([ 4.6362e-02,  5.7130e-02, -1.3877e-02, -3.0030e-02,  3.5341e-03,
         1.0113e-02,  4.1029e-03,  7.6469e-04, -1.0138e-03,  6.0837e-04,
        -2.9929e-04,  1.3329e-04, -5.5502e-05,  2.1893e-05, -8.2286e-06,
         2.9559e-06, -1.0148e-06,  9.0000e+00]),
 'ge70': array([ 3.8182e-02,  6.0306e-02,  6.4346e-03, -2.9427e-02, -9.5888e-03,
         8.7849e-03,  4.9187e-03, -1.5189e-03, -1.7385e-03, -1.6794e-04,
        -1.1746e-04,  6.5768e-05, -3.0691e-05,  1.3051e-06, -5.2251e-06,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'ge72': array([ 3.8083e-02,  5.9342e-02,  4.7718e-03, -2.9953e-02, -8.8476e-03,
         9.6205e-03,  4.7901e-03, -1.6869e-03, -1.5406e-03, -9.7230e-05,
        -4.7640e-05, -1.5669e-06,  6.7076e-06, -4.4500e-06,  2.2158e-06,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'ge74': array([ 3.7989e-02,  5.8298e-02,  2.7406e-03, -3.0666e-02, -8.1505e-03,
         1.0231e-02,  4.9382e-03, -1.6270e-03, -1.3937e-03,  1.5476e-04,
         1.4396e-04, -7.3075e-05,  3.1998e-05, -1.2822e-05,  4.8406e-06,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'ge76': array([ 3.7951e-02,  5.7876e-02,  1.5303e-03, -3.1822e-02, -7.6875e-03,
         1.1237e-02,  5.0780e-03, -1.7293e-03, -1.5523e-03,  7.2439e-05,
         1.6560e-04, -8.6631e-05,  3.9159e-05, -1.6259e-05,  6.3681e-06,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'sr88': array([ 5.6435e-02,  5.5072e-02, -3.3363e-02, -2.6061e-02,  1.5749e-02,
         7.5233e-03, -5.5044e-03, -2.3643e-03,  3.9362e-04, -2.2733e-04,
         1.2519e-04, -6.1176e-05,  2.7243e-05, -1.1285e-05,  4.3997e-06,
        -1.6200e-06,  5.7100e-07,  9.0000e+00]),
 'zr98': array([ 4.6188e-02,  6.1795e-02, -1.2315e-02, -3.6915e-02,  2.5175e-03,
         1.5234e-02, -5.5146e-04, -6.0631e-03, -1.2198e-03,  3.6200e-04,
        -1.6466e-04,  5.3305e-05, -5.0873e-06, -8.5658e-06,  8.6095e-06,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'zr92': array([ 4.5939e-02,  6.0104e-02, -1.3341e-02, -3.5106e-02,  3.1760e-03,
         1.3753e-02, -8.2682e-04, -5.3001e-03, -9.7579e-04,  2.6489e-04,
        -1.5873e-04,  6.9301e-05, -2.2278e-05,  3.9533e-06,  1.0609e-06,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'zr94': array([ 4.5798e-02,  5.9245e-02, -1.3389e-02, -3.3252e-02,  3.9888e-03,
         1.2750e-02, -1.5793e-03, -5.6692e-03, -1.5698e-03,  5.4394e-05,
        -2.4032e-05,  3.8401e-05, -3.1690e-05,  1.8481e-05, -8.5367e-06,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'mo92': array([ 3.0782e-02,  5.9896e-02,  2.2016e-02, -2.8945e-02, -2.6707e-02,
         4.0426e-03,  1.4429e-02,  3.1696e-03, -6.3061e-03, -4.5119e-03,
         4.6236e-04,  9.4909e-04, -3.8930e-04, -1.4808e-04,  1.9622e-04,
        -4.0197e-05, -7.1949e-05,  1.2000e+01]),
 'mo94': array([ 3.0661e-02,  5.8828e-02,  2.0396e-02, -2.8830e-02, -2.5077e-02,
         4.4768e-03,  1.3127e-02,  1.9548e-03, -6.1403e-03, -3.5825e-03,
         7.3790e-04,  6.1882e-04, -4.0556e-04, -5.5748e-06, -1.2453e-04,
        -5.7812e-05, -2.1657e-05,  1.2000e+01]),
 'mo96': array([ 3.0564e-02,  5.8013e-02,  1.9255e-02, -2.8372e-02, -2.3304e-02,
         4.9894e-03,  1.2126e-02,  1.0496e-03, -6.2592e-03, -3.2814e-03,
         8.9668e-04,  5.0636e-04, -4.3412e-04,  7.1531e-05,  7.6745e-05,
        -5.4316e-05,  2.3386e-07,  1.2000e+01]),
 'mo98': array([ 3.0483e-02,  5.7207e-02,  1.7888e-02, -2.8388e-02, -2.1778e-02,
         5.6780e-03,  1.1236e-02,  8.2176e-04, -5.0390e-03, -2.3877e-03,
         7.1492e-04,  2.9839e-04, -3.1408e-04,  8.0177e-04,  4.3682e-05,
        -5.1394e-05,  2.2293e-05,  1.2000e+01]),
 'mo100': array([ 3.0353e-02,  5.6087e-02,  1.6057e-02, -2.8767e-02, -2.0683e-02,
         6.2429e-03,  1.1058e-02,  1.1502e-03, -3.9395e-03, -1.4978e-03,
         7.6350e-04,  1.0554e-04, -2.5658e-04,  1.0964e-04,  1.0015e-05,
        -4.0341e-05,  2.5744e-05,  1.2000e+01]),
 'pd104': array([ 4.1210e-02,  6.2846e-02, -2.1202e-03, -3.8359e-02, -4.4693e-03,
         1.6656e-02,  3.6873e-03, -5.7534e-03, -3.2499e-03,  6.9844e-04,
         1.6304e-03,  5.9882e-04,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'pd106': array([ 4.1056e-02,  6.1757e-02, -2.9891e-03, -3.7356e-02, -3.5348e-03,
         1.6085e-02,  2.8502e-03, -5.5764e-03, -1.5433e-03,  2.2281e-03,
         1.3160e-03,  1.6508e-05,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'pd108': array([ 4.0754e-02,  5.9460e-02, -5.4077e-03, -3.6305e-02, -2.1987e-03,
         1.5418e-02,  2.5927e-03, -5.2781e-03, -1.9757e-03,  1.0339e-03,
         2.2891e-04, -3.3464e-04,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'pd110': array([ 4.0668e-02,  5.8793e-02, -6.1375e-03, -3.5983e-02, -1.7447e-03,
         1.4998e-02,  1.9994e-03, -5.3170e-03, -1.4289e-03,  1.6033e-03,
         3.1574e-04, -4.2195e-04,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'sm144': array([ 7.4734e-02,  2.6145e-02, -6.3832e-02,  1.0432e-02,  1.9183e-02,
        -1.2572e-02, -3.9707e-03, -1.8703e-03,  1.2602e-03, -1.1902e-03,
        -1.5703e-03,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  9.2000e+00]),
 'sm148': array([ 7.3859e-02,  2.4023e-02, -5.9437e-02,  1.0761e-02,  1.7022e-02,
        -1.1401e-02, -1.8102e-03,  9.3011e-04,  9.8012e-04, -1.2601e-03,
        -1.7402e-03,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  9.2000e+00]),
 'sm150': array([ 7.3338e-02,  2.4626e-02, -5.2773e-02,  1.0582e-02,  1.5353e-02,
        -9.5624e-03, -1.8804e-03, -7.9019e-04,  1.0102e-03, -2.6606e-03,
        -1.8304e-03,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  9.2000e+00]),
 'sm152': array([ 7.2646e-02,  2.1824e-02, -5.4112e-02,  9.8321e-03,  1.6213e-02,
        -6.5614e-03,  5.3611e-03, -1.4103e-03, -9.9022e-04, -2.3005e-03,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  9.2000e+00]),
 'sm154': array([ 5.5859e-02,  4.4002e-02, -4.0342e-02, -1.7989e-02,  1.9817e-02,
         5.1643e-03, -6.0212e-03, -2.3127e-03,  4.7024e-04,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.0500e+01]),
 'gd154': array([ 6.3832e-02,  3.6983e-02, -4.8193e-02, -5.1046e-03,  1.9805e-02,
        -8.2574e-04, -4.6942e-03,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.0000e+01]),
 'gd158': array([ 5.7217e-02,  4.3061e-02, -4.1996e-02, -1.7203e-02,  1.9933e-02,
         5.1060e-03, -7.3665e-03, -2.0926e-03,  2.1883e-03,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.0500e+01]),
 'er166': array([ 5.4426e-02,  4.7165e-02, -3.8654e-02, -1.9672e-02,  2.2092e-02,
         7.8708e-03, -5.3005e-03,  5.0005e-04,  5.2005e-04, -3.5003e-04,
         1.2001e-04,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'yb174': array([ 5.4440e-02,  4.0034e-02, -4.5606e-02, -2.0932e-02,  2.0455e-02,
         2.7061e-03, -6.0489e-03, -1.5918e-04,  1.1938e-03,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'lu175': array([ 5.5609e-02,  4.2243e-02, -4.5028e-02, -1.9491e-02,  2.2514e-02,
         3.8982e-03, -7.2395e-03,  3.1822e-04, -2.3866e-04,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'os192': array([ 5.9041e-02,  4.1498e-02, -4.9900e-02, -1.0183e-02,  2.9067e-02,
        -5.7382e-03, -9.2348e-03,  3.6170e-03,  2.8736e-03,  2.4194e-04,
        -1.6766e-03,  7.3610e-04,  0.0000e+00,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'pt196': array([ 5.0218e-02,  5.3722e-02, -3.5015e-02, -3.4588e-02,  2.3564e-02,
         1.4340e-02, -1.3270e-02, -5.1212e-03,  5.6088e-03,  1.4890e-03,
        -1.0928e-03,  5.5662e-04, -5.0557e-05, -1.9708e-04,  2.4016e-04,
         0.0000e+00,  0.0000e+00,  1.2000e+01]),
 't1203': array([ 5.1568e-02,  5.1562e-02, -3.9299e-02, -3.0826e-02,  2.7491e-02,
         1.0795e-02, -1.5922e-02, -2.5527e-03,  5.8548e-03,  1.9324e-04,
        -1.7925e-04,  1.4307e-04, -9.1669e-05,  5.3497e-05, -2.9492e-05,
         1.5625e-05, -8.0141e-06,  1.2000e+01]),
 't1205': array([ 5.1518e-02,  5.1165e-02, -3.9559e-02, -3.0118e-02,  2.7600e-02,
         1.0412e-02, -1.5725e-02, -2.6546e-03,  7.0184e-03,  8.2116e-04,
        -5.1805e-04,  3.2560e-04, -1.8670e-04,  1.0202e-04, -5.3857e-05,
         2.7672e-05, -1.3873e-05,  1.2000e+01]),
 'pb204': array([ 5.2102e-02,  5.1786e-02, -3.9188e-02, -2.9242e-02,  2.8992e-02,
         1.1040e-02, -1.4591e-02, -9.4917e-04,  7.1349e-03,  2.4780e-04,
        -6.1656e-04,  4.2335e-04, -2.5250e-04,  1.4106e-04, -7.5446e-05,
         3.9143e-05, -1.9760e-05,  1.2000e+01]),
 'pb206': array([ 5.2019e-02,  5.1190e-02, -3.9459e-02, -2.8405e-02,  2.8862e-02,
         1.0685e-02, -1.4550e-02, -1.3519e-03,  7.7624e-03, -4.1882e-05,
        -9.7010e-04,  6.9611e-04, -4.2410e-04,  2.3857e-04, -1.2828e-04,
         6.6663e-05, -3.3718e-05,  1.2000e+01]),
 'pb207': array([ 5.1981e-02,  5.1059e-02, -3.9447e-02, -2.8428e-02,  2.8988e-02,
         1.0329e-02, -1.4029e-02, -4.6728e-04,  6.7984e-03,  5.6905e-04,
        -5.0430e-04,  3.2796e-04, -1.9157e-04,  1.0565e-04, -5.6200e-05,
         2.9020e-05, -1.4621e-05,  1.2000e+01]),
 'pb208': array([ 6.2732e-02,  3.8542e-02, -5.5105e-02, -2.6990e-03,  3.1016e-02,
        -9.9486e-03, -9.3012e-03,  7.6653e-03,  2.0885e-03, -1.7840e-03,
         7.4876e-05,  3.2278e-04, -1.1353e-04,  0.0000e+00,  0.0000e+00,
         0.0000e+00,  0.0000e+00,  1.1000e+01]),
 'bi209': array([ 5.2448e-02,  5.0400e-02, -4.1014e-02, -2.7927e-02,  2.9587e-02,
         9.8017e-03, -1.4930e-02, -3.1967e-04,  7.7252e-03,  5.7533e-04,
        -8.2529e-04,  2.5728e-04, -1.1043e-04,  5.1930e-05, -2.4767e-05,
         1.1863e-05, -5.6554e-06,  1.2000e+01])}