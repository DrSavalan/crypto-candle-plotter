# plotter.py

import plotly.graph_objects as go

def candlePlot(df, title):
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])
    
    fig.update_layout(
        title=title,
        xaxis_rangeslider_visible=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    
    fileName = title + '.html'
    fig.write_html(fileName)
    print(f"Candlestick chart saved to {fileName}")
