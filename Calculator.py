import dash  # Import the Dash module
from dash import dcc, html  # Import core Dash components
from dash.dependencies import Input, Output, State, ALL  # Import callback dependencies

# Create a Dash app instance
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define the layout of the app
app.layout = html.Div([
    # Output display area
    html.H1("Calculator",style={'fontSize': '10px',}),
    html.Div(id={'type': 'output', 'index': 'result'}, children='0',style={
        'border': '2px solid black',
        'padding': '20px',
        'width': '115px',
        'height': '0px',
        'margin': 'auto',
        'textAlign': 'center'
    }),
    html.Br(),
    

    # Buttons for numbers and operators with increased size
    html.Div([
        html.Button('1', id={'type': 'num', 'index': 1}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('2', id={'type': 'num', 'index': 2}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('3', id={'type': 'num', 'index': 3}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('+', id={'type': 'operator', 'index': '+'}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
    ]),
    html.Div([
        html.Button('4', id={'type': 'num', 'index': 4}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('5', id={'type': 'num', 'index': 5}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('6', id={'type': 'num', 'index': 6}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('-', id={'type': 'operator', 'index': '-'}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
    ]),
    html.Div([
        html.Button('7', id={'type': 'num', 'index': 7}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('8', id={'type': 'num', 'index': 8}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('9', id={'type': 'num', 'index': 9}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('*', id={'type': 'operator', 'index': '*'}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
    ]),
    html.Div([
        html.Button('0', id={'type': 'num', 'index': 0}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('=', id={'type': 'operator', 'index': '='}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('CE', id={'type': 'operator', 'index': 'CE'}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
        html.Button('/', id={'type': 'operator', 'index': '/'}, style={'fontSize': '20px', 'padding': '10px', 'margin': '5px'}),
    ]),
    dcc.Store(id='stored_value', data=''),  # Store to hold the first number entered
    dcc.Store(id='stored_operator', data=''),  # Store to hold the selected operator (e.g., '+', '-', etc.)
    dcc.Store(id='current_value', data='')  # Store to hold the current number being typed
],style={
        'border': '2px solid black',
        'padding': '20px',
        'width': '200px',
        'height': '300px',
        'margin': 'auto',
        'textAlign': 'center'
    })

# Define the callback to handle button clicks and update the display
@app.callback(
    [Output({'type': 'output', 'index': 'result'}, 'children'),
     Output('stored_value', 'data'),
     Output('stored_operator', 'data'),
     Output('current_value', 'data')],
    [Input({'type': 'num', 'index': ALL}, 'n_clicks'),
     Input({'type': 'operator', 'index': ALL}, 'n_clicks')],
    [State('stored_value', 'data'),
     State('stored_operator', 'data'),
     State('current_value', 'data'),
     State({'type': 'output', 'index': 'result'}, 'children')]
)
# Function to update the display and manage the calculator's state
def update_display(num_clicks, operator_clicks, stored_value, stored_operator, current_value, current_output):
    # Get the context of the triggered callback
    ctx = dash.callback_context

    # If no button has been clicked, return the current state
    if not ctx.triggered:
        return current_output, stored_value, stored_operator, current_value

    # Get the ID of the button that triggered the callback
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    # Extract whether it was a 'num' or 'operator' button
    button_type = eval(button_id)['type']
    # Extract the number or operator value of the button
    button_value = eval(button_id)['index']

    # Handle number button clicks
    if button_type == 'num':
        # Append number to the current value
        current_value += str(button_value)
        return current_value, stored_value, stored_operator, current_value

    # Handle operator button clicks
    if button_type == 'operator':
        # If 'CE' is clicked, reset everything
        if button_value == 'CE':
            return '0', '', '', ''
        # If '=' is clicked, perform the calculation
        elif button_value == '=':
            if stored_operator == '+':
                result = float(stored_value) + float(current_value)
            elif stored_operator == '-':
                result = float(stored_value) - float(current_value)
            elif stored_operator == '*':
                result = float(stored_value) * float(current_value)
            elif stored_operator == '/':
                result = float(stored_value) / float(current_value) if float(current_value) != 0 else 'Error'
            else:
                result = current_output  # Default case if operator is missing
            # Return the result and reset storage
            return str(result), '', '', ''
        else:
            # For other operators, store the operator and reset current_value
            return current_output, current_value, button_value, ''

# Start the Dash app server
if __name__ == '__main__':
    app.run_server(debug=True)
