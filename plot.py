#
# plot.py, 30 Apr 23

from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

import pandas

# import os
# openai.api_key = os.getenv("OPENAI_API_KEY")

def plot_data(file_str, usr_str):
   # agent = create_csv_agent(OpenAI(temperature=0.0, model_name="text-davinci-003", verbose=True),
   # agent = create_csv_agent(OpenAI(temperature=0.0, verbose=True),
   agent = create_csv_agent(OpenAI(top_p=0.1, verbose=True),
			file_str, verbose=True)

   plot_txt="Use matplotlib to plot data and" +\
   " use the column names for axis labels." +\
   " Use the same indentation for each python statement." +\
   " I want you to create a scatter " +\
   usr_str + " Display the plot."
   agent.run(plot_txt)

# agent.run("Generate a plot of second column against the third column and call matplotlib")

# plot_data("aug-oct_day_items.csv", "plot using the two month columns.")

plot_data("task-est-act.csv", "plot using the estimates and actuals.")
plot_data("task-est-act.csv", "plot the estimates and actuals using a logarithmic scale.")

