import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

def counts(df):
    ''' Assuming input from pd.DataFrame with col 2 as sentiments, col 3 as accuracies '''
    topic = []
    acc = []
    for i in df.iloc[:,1]:
        topic.append(i)
    for j in df.iloc[:,2]:
        acc.append(j)

    count_dict ={}

    for j in set(df.iloc[:,1]):
        for i in range(len(topic)):
            if j == topic[i]:
                if j in count_dict.keys():
                    count_dict[j] += acc[i]
                else:
                    count_dict[j] = acc[i]
    return count_dict
            
def make_bar(D):
    D = {k: v for k, v in sorted(D.items(), key=lambda item: item[1])}
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.3,0.8,0.7])
    ax.bar(range(len(D)), list(D.values()), align='center')
    plt.xticks(range(len(D)), list(D.keys()))
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    '''
    fig.update_layout(
        title="Total Votes", 
        template=theme_hodp
        )
    '''
    # # for python 2.x:
    # plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
    # plt.xticks(range(len(D)), D.keys())  # in python 2.x
    # plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.show()

def reformat_dict(D,name):
    D = {k: v for k, v in sorted(D.items(), key=lambda item: item[1])}
    plot_dict = {'Topics':[], 'Weighted Frequency':[]}
    for key in D:
        plot_dict['Topics'].append(key)
        plot_dict['Weighted Frequency'].append(D[key])
    plot_dict['Name'] = name
    return plot_dict

def make_pxbar(D_list):
    bar_list = []
    for bar, name in D_list:
        D = reformat_dict(bar,name)
        bar_list.append(go.Bar(name=D['Name'], x = D['Topics'], y=D['Weighted Frequency']))

    fig = go.Figure(bar_list)
    fig.update_layout(title="Sentiments", template=theme_hodp)
    fig.show()
    
def main():
    '''
    for i in year:
        df = pd.read_csv(i+topic)
        D = counts(df)
        D = {k: v for k, v in sorted(D.items(), key=lambda item: item[1])}
    '''
    b_list = []
    for y in year:
        df = pd.read_csv(y+sentiment)
        D = counts(df)
        D = {k: v for k, v in sorted(D.items(), key=lambda item: item[1])}
        b_list.append((D, y))
        # make_bar(D)
    make_pxbar(b_list)
    
    
topic = '.csv'
sentiment = '.csv'
year = [f'Comm/Sentiments/{i}' for i in [2020,2019]]
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# template
theme_hodp = go.layout.Template(
    layout=go.Layout(
        title = {'font':{'size':24, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
        font = {'size':18, 'family':'Helvetica', 'color':'#717171'},
        xaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'showline': True,
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'automargin': True
                },
        yaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'showline': True,
                'automargin': True
                },
        legend = {'bgcolor':'rgba(0,0,0,0)', 
                'title':{'font':{'size':18, 'family':"Helvetica", 'color':monochrome_colors[0]}}, 
                'font':{'size':14, 'family':"Helvetica"}, 
                'yanchor':'bottom'
                },
        colorscale = {'diverging':monochrome_colors},
        coloraxis = {'autocolorscale':True, 
                'cauto':True, 
                'colorbar':{'tickfont':{'size':14,'family':'Helvetica'}, 'title':{'font':{'size':18, 'family':'Helvetica'}}},
                }
    )
)


if __name__=='__main__':
    main()
