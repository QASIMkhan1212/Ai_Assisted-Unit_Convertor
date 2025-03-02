import streamlit as st

# Conversion rates for different categories
conversion_rates = {
    'length': {
        'meters': {
            'meters': 1,
            'kilometers': 0.001,
            'miles': 0.000621371
        },
        'kilometers': {
            'meters': 1000,
            'kilometers': 1,
            'miles': 0.621371
        },
        'miles': {
            'meters': 1609.34,
            'kilometers': 1.60934,
            'miles': 1
        }
    },
    'mass': {
        'grams': {
            'grams': 1,
            'kilograms': 0.001,
            'pounds': 0.00220462
        },
        'kilograms': {
            'grams': 1000,
            'kilograms': 1,
            'pounds': 2.20462
        },
        'pounds': {
            'grams': 453.592,
            'kilograms': 0.453592,
            'pounds': 1
        }
    },
    'temperature': {
        'celsius': {
            'celsius': lambda x: x,
            'fahrenheit': lambda x: (x * 9/5) + 32,
            'kelvin': lambda x: x + 273.15
        },
        'fahrenheit': {
            'celsius': lambda x: (x - 32) * 5/9,
            'fahrenheit': lambda x: x,
            'kelvin': lambda x: (x - 32) * 5/9 + 273.15
        },
        'kelvin': {
            'celsius': lambda x: x - 273.15,
            'fahrenheit': lambda x: (x - 273.15) * 9/5 + 32,
            'kelvin': lambda x: x
        }
    },
    'energy': {
        'joules': {
            'joules': 1,
            'kilojoules': 0.001,
            'calories': 0.239006
        },
        'kilojoules': {
            'joules': 1000,
            'kilojoules': 1,
            'calories': 239.006
        },
        'calories': {
            'joules': 4.184,
            'kilojoules': 0.004184,
            'calories': 1
        }
    },
    'frequency': {
        'hertz': {
            'hertz': 1,
            'kilohertz': 0.001,
            'megahertz': 0.000001
        },
        'kilohertz': {
            'hertz': 1000,
            'kilohertz': 1,
            'megahertz': 0.001
        },
        'megahertz': {
            'hertz': 1000000,
            'kilohertz': 1000,
            'megahertz': 1
        }
    },
    'plane angle': {
        'degrees': {
            'degrees': 1,
            'radians': 0.0174533
        },
        'radians': {
            'degrees': 57.2958,
            'radians': 1
        }
    },
    'pressure': {
        'pascals': {
            'pascals': 1,
            'bar': 0.00001,
            'psi': 0.000145038
        },
        'bar': {
            'pascals': 100000,
            'bar': 1,
            'psi': 14.5038
        },
        'psi': {
            'pascals': 6894.76,
            'bar': 0.0689476,
            'psi': 1
        }
    },
    'speed': {
        'meters per second': {
            'meters per second': 1,
            'kilometers per hour': 3.6,
            'miles per hour': 2.23694
        },
        'kilometers per hour': {
            'meters per second': 0.277778,
            'kilometers per hour': 1,
            'miles per hour': 0.621371
        },
        'miles per hour': {
            'meters per second': 0.44704,
            'kilometers per hour': 1.60934,
            'miles per hour': 1
        }
    },
    'time': {
        'seconds': {
            'seconds': 1,
            'minutes': 0.0166667,
            'hours': 0.000277778
        },
        'minutes': {
            'seconds': 60,
            'minutes': 1,
            'hours': 0.0166667
        },
        'hours': {
            'seconds': 3600,
            'minutes': 60,
            'hours': 1
        }
    },
    'volume': {
        'liters': {
            'liters': 1,
            'milliliters': 1000,
            'cubic meters': 0.001
        },
        'milliliters': {
            'liters': 0.001,
            'milliliters': 1,
            'cubic meters': 0.000001
        },
        'cubic meters': {
            'liters': 1000,
            'milliliters': 1000000,
            'cubic meters': 1
        }
    },
    'area': {
        'square meters': {
            'square meters': 1,
            'square kilometers': 0.000001,
            'acres': 0.000247105
        },
        'square kilometers': {
            'square meters': 1000000,
            'square kilometers': 1,
            'acres': 247.105
        },
        'acres': {
            'square meters': 4046.86,
            'square kilometers': 0.00404686,
            'acres': 1
        }
    },
    'digital storage': {
        'bytes': {
            'bytes': 1,
            'kilobytes': 0.001,
            'megabytes': 0.000001
        },
        'kilobytes': {
            'bytes': 1000,
            'kilobytes': 1,
            'megabytes': 0.001
        },
        'megabytes': {
            'bytes': 1000000,
            'kilobytes': 1000,
            'megabytes': 1
        }
    },
    'data transfer rate': {
        'bps': {
            'bps': 1,
            'kbps': 0.001,
            'mbps': 0.000001
        },
        'kbps': {
            'bps': 1000,
            'kbps': 1,
            'mbps': 0.001
        },
        'mbps': {
            'bps': 1000000,
            'kbps': 1000,
            'mbps': 1
        }
    }
}

# Streamlit app
st.title("Advanced Unit Converter")

# Select category
category = st.selectbox("Select category", options=list(conversion_rates.keys()))

# Input value
input_value = st.number_input("Enter value", format="%.4f")

# Input unit
input_unit = st.selectbox("Input unit", options=list(conversion_rates[category].keys()))

# Output unit
output_unit = st.selectbox("Output unit", options=list(conversion_rates[category].keys()))

# Convert button
if st.button("Convert"):
    if category == 'temperature':
        converted_value = conversion_rates[category][input_unit][output_unit](input_value)
    else:
        converted_value = input_value * conversion_rates[category][input_unit][output_unit]
    st.write(f"Converted value: {converted_value:.4f} {output_unit}") 
    
    # Embed the JavaScript chatbot
chatbot_html = """
<script> window.chtlConfig = { chatbotId: "3674989389", display: "page_inline" } </script>
<div id="chatling-inline-bot" style="width: 70%; height: 500px;"></div>
<script async data-id="3674989389" data-display="page_inline" id="chatling-embed-script" type="text/javascript" src="https://chatling.ai/js/embed.js"></script>
<div id="chatbot"></div>
"""

st.components.v1.html(chatbot_html, height=500, width=600) 