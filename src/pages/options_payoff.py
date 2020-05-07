import streamlit as st
import numpy as np
from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider, Column
from bokeh.models.annotations import Span
from bokeh.plotting import ColumnDataSource, figure, show, output_file

max_x = 60
call_premium = Slider(start=0, end=max_x, value=0, step=1, title="Premium")
strike_price = Slider(start=0, end=max_x, value=10, step=1, title="strike_price")
x = np.linspace(0, max_x, 500)
y = np.max([np.zeros(x.shape), x - strike_price.value ], axis=0) - call_premium.value

source = ColumnDataSource(data=dict(x=x, y=y))
plot = figure(x_range = (0, max_x), y_range=(-30, max_x), plot_width=400, plot_height=400)

zero = Span(location=0, dimension='width', line_color='firebrick', line_dash='dashed', line_alpha=0.7, line_width=1)
plot.add_layout(zero)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6, color='cadetblue')

callback = CustomJS(args=dict(source=source, call_premium=call_premium, strike=strike_price),
                    code="""
    let data = source.data;
    let prem = call_premium.value ;
    let s = strike.value;
    let x = data['x'];
    let y = data['y'];
    for (let i = 0; i < x.length; i++) {
        
        y[i] = Math.max(0, x[i] - s) - prem
    };
    source.change.emit();
""")

call_premium.js_on_change('value', callback)
strike_price.js_on_change('value', callback)

layout = column(call_premium, strike_price, plot)

st.bokeh_chart(layout)