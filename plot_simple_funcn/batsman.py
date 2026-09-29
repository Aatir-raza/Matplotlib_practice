import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

batsman=pd.read_csv(r'C:\Users\Homes\Desktop\matplotlib\sharma-kohli.csv')
plt.plot(batsman['index'],batsman['V Kohli'])
plt.plot(batsman['index'],batsman['RG Sharma'])

plt.title('Rohit sharma vs virat kohli carreer comparison')
plt.xlabel('Season')
plt.ylabel('Runs scored')

plt.plot(batsman['index'],batsman['V Kohli'],color='#D9F10F',linestyle='solid',linewidth=3,marker='D',markersize=10,label='virat')
plt.plot(batsman['index'],batsman['RG Sharma'],color="#F10F8F",linestyle='dashdot',linewidth=3,marker='D',markersize=10,label='rohit')

plt.legend()
plt.show()
