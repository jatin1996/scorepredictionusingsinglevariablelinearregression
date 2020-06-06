{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "X=pd.read_csv('Linear_X_Train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "Y=pd.read_csv('Linear_Y_Train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>x</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>-0.289307</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>-0.588810</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1.027507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>-0.259013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>0.782043</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          x\n",
       "0 -0.289307\n",
       "1 -0.588810\n",
       "2  1.027507\n",
       "3 -0.259013\n",
       "4  0.782043"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>-0.091101</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>-53.467721</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>75.457009</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>-12.025286</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>57.414187</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           y\n",
       "0  -0.091101\n",
       "1 -53.467721\n",
       "2  75.457009\n",
       "3 -12.025286\n",
       "4  57.414187"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x2211692db08>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X,Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "x   -0.037795\n",
       "dtype: float64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "X=X-X.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "Y=Y-Y.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "plt.scatter(X,Y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x22118863c88>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X,Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "X=X.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "Y=Y.values\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x2211b03b108>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X,Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "def hypothesis(x,theta):\n",
    "    y_=theta[0]+theta[1]*x\n",
    "    return y_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gradient(X,Y,theta):\n",
    "    grad=np.zeros((2,))\n",
    "    m=X.shape[0]\n",
    "    for i in range(m):\n",
    "        y_=hypothesis(X[i],theta)\n",
    "        y=Y[i]\n",
    "        grad[0]+=(y_-y)\n",
    "        grad[1]+=(y_-y)*X[i]\n",
    "    return grad/m\n",
    "def error(X,Y,theta):\n",
    "    m=X.shape[0]\n",
    "    totalerror=0.0\n",
    "    for i in range(m):\n",
    "        y_=hypothesis(X[i],theta)\n",
    "        totalerror+=(y_-Y[i])**2\n",
    "    return totalerror/m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gradienDescent(X,Y,max_steps=100,learningrate=0.1):\n",
    "    theta=np.zeros((2,))\n",
    "    errorlist=[]\n",
    "    for i in range(max_steps):\n",
    "        e=error(X,Y,theta)\n",
    "        errorlist.append(e)\n",
    "        grad=gradient(X,Y,theta)\n",
    "        theta[0]=theta[0]-learningrate*grad[0]\n",
    "        theta[1]=theta[1]-learningrate*grad[1]\n",
    "    return theta,errorlist\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "theta,errorlist=gradienDescent(X,Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([6.73414509e-15, 8.05410830e+01])"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "theta\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[array([6575.8823757]),\n",
       " array([5380.89448845]),\n",
       " array([4409.55772458]),\n",
       " array([3620.01406568]),\n",
       " array([2978.23954163]),\n",
       " array([2456.57802859]),\n",
       " array([2032.54945783]),\n",
       " array([1687.88107741]),\n",
       " array([1407.7200207]),\n",
       " array([1179.99324866]),\n",
       " array([994.88728386]),\n",
       " array([844.42531622]),\n",
       " array([722.12345668]),\n",
       " array([622.71132562]),\n",
       " array([541.90493528]),\n",
       " array([476.22207896]),\n",
       " array([422.83227161]),\n",
       " array([379.43477507]),\n",
       " array([344.15945194]),\n",
       " array([315.48617536]),\n",
       " array([292.17932181]),\n",
       " array([273.23452416]),\n",
       " array([257.83539031]),\n",
       " array([245.31832214]),\n",
       " array([235.14391902]),\n",
       " array([226.87373326]),\n",
       " array([220.15137603]),\n",
       " array([214.68715937]),\n",
       " array([210.24561266]),\n",
       " array([206.63533538]),\n",
       " array([203.70074911]),\n",
       " array([201.31539311]),\n",
       " array([199.37647473]),\n",
       " array([197.80043975]),\n",
       " array([196.51937178]),\n",
       " array([195.47806547]),\n",
       " array([194.63164761]),\n",
       " array([193.94364332]),\n",
       " array([193.3844043]),\n",
       " array([192.92983113]),\n",
       " array([192.56033482]),\n",
       " array([192.25999256]),\n",
       " array([192.01586165]),\n",
       " array([191.81742172]),\n",
       " array([191.65612133]),\n",
       " array([191.52500954]),\n",
       " array([191.41843633]),\n",
       " array([191.33180911]),\n",
       " array([191.26139484]),\n",
       " array([191.20415913]),\n",
       " array([191.15763553]),\n",
       " array([191.11981918]),\n",
       " array([191.08908044]),\n",
       " array([191.06409469]),\n",
       " array([191.04378522]),\n",
       " array([191.02727682]),\n",
       " array([191.0138581]),\n",
       " array([191.00295079]),\n",
       " array([190.99408486]),\n",
       " array([190.98687827]),\n",
       " array([190.98102044]),\n",
       " array([190.97625895]),\n",
       " array([190.97238861]),\n",
       " array([190.96924263]),\n",
       " array([190.96668545]),\n",
       " array([190.96460686]),\n",
       " array([190.9629173]),\n",
       " array([190.96154395]),\n",
       " array([190.96042763]),\n",
       " array([190.95952024]),\n",
       " array([190.95878268]),\n",
       " array([190.95818316]),\n",
       " array([190.95769584]),\n",
       " array([190.95729973]),\n",
       " array([190.95697775]),\n",
       " array([190.95671603]),\n",
       " array([190.9565033]),\n",
       " array([190.95633038]),\n",
       " array([190.95618982]),\n",
       " array([190.95607557]),\n",
       " array([190.9559827]),\n",
       " array([190.95590722]),\n",
       " array([190.95584586]),\n",
       " array([190.95579598]),\n",
       " array([190.95575544]),\n",
       " array([190.95572249]),\n",
       " array([190.9556957]),\n",
       " array([190.95567393]),\n",
       " array([190.95565623]),\n",
       " array([190.95564185]),\n",
       " array([190.95563016]),\n",
       " array([190.95562065]),\n",
       " array([190.95561293]),\n",
       " array([190.95560665]),\n",
       " array([190.95560154]),\n",
       " array([190.95559739]),\n",
       " array([190.95559402]),\n",
       " array([190.95559128]),\n",
       " array([190.95558905]),\n",
       " array([190.95558724])]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "errorlist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2211b702308>]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(errorlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_=hypothesis(X,theta)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2211b7a9c48>]"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(y_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2211b837708>]"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(y_,X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2211c0d5108>]"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "plt.scatter(X,Y)\n",
    "plt.plot(X,y_,color='orange')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2211bc96508>]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(X,y_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_test=pd.read_csv('Linear_X_Test.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_test=hypothesis(x_test,theta)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.DataFrame(data=y_test,columns=['y'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('y_prediciton.csv',index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
