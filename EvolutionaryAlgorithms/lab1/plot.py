import sys
import os

import plotly.plotly as py
import plotly.graph_objs as go

if not os.path.exists(os.path.expanduser('~/.plotly/.credentials')):
    print("""
        Please fill `~/.plotly/.credentials` file with your credentials

        {
            "username": "XXX",
            "api_key": "SuperAPIKey"
        }

        Find your API key at: https://plot.ly/settings/api#/
    """)
    sys.exit(1)

values = [float(x) for x in sys.stdin]

# Create a trace
trace = go.Scatter(
    y=values,
    mode=sys.argv[1] if len(sys.argv) > 1 else 'markers'
)

py.plot([trace], filename='basic-line')
