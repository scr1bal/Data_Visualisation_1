import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
#reading the file
my_data = pd.read_csv(my_filepath)

#printing the first 5 columns of the dataset
my_data.head()

sns.set_style('darkgrid')
sns.jointplot(x=my_data['player_height'], y=my_data['player_weight'], kind = "kde", shade=True)

