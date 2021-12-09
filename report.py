# Import necessary modules
import json
import os
import datetime
import ijson
import io
import pandas as pd
import plotly.express as px

# Define functions

def extract_json(file):
    with open(file, encoding="UTF-8") as f:
        list_of_id=[]
        list_of_event=[]
        list_of_ts=[]
        cursor = 0
        for line_number, line in enumerate(f):
            line_as_file = io.StringIO(line)
            json_parser = ijson.parse(line_as_file) # using new parser for each line
            for prefix, type, value in json_parser:
                if prefix == 'id':
                    list_of_id.append(value)
                elif prefix == 'event':
                    list_of_event.append(value)
                elif prefix == 'timestamp':
                    list_of_ts.append(value)
            cursor += len(line) # increment cursor at end of length of line considering json string could span across multiple lines.
            df = pd.DataFrame(columns = ['id','event','timestamp'])
            df['id'] = list_of_id
            df['event'] = list_of_event
            df['timestamp'] = list_of_ts
            df['date'] = pd.to_datetime(df['timestamp']).apply(lambda x:x.date()) # adding a derived date field
    return df
    
def plot_viz(data):
    df_plot = data.groupby(['event','date'],as_index=False,dropna=False).agg(count=('id',pd.Series.count))  # get unique count of ids
    df_plot['date'] = pd.to_datetime(df_plot['date'])
    plot = px.bar(df_plot,x='date',y='count',color='event')
    if not os.path.exists("images"):
        os.mkdir("images")
    viz_filename = f'viz_{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.png'
    plot.write_image(f'./images/{viz_filename}')
    print("Visualization generated")
 
 
# Plot vizualization
df = extract_json('input.json')
plot_viz(df)