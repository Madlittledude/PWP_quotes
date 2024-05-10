import streamlit as st
import pandas as pd

# Define the data in a dictionary with nested dictionaries for prices and times
services_data = {
    'House Wash': {'Price': [100, 200, 300, 500], 'Time': [.75, 1.25, 2, 3]},
    'Patio Wash': {'Price': [100, 200, 300, 500], 'Time': [1, 1.5, 2, 3]},
    'Perimiters': {'Price': [200, 300, 425, 500], 'Time': [2, 2.5, 3, 3.5]},
    'Gutter Clean': {'Price': [175, 250, 300, 400], 'Time': [0.5, 0.75, 1, 1.25]},
    'Roof Wash': {'Price': [200, 300, 400, 600], 'Time': [2, 2.5, 3, 3.5]},
    'Driveway': {'Price': [100, 150, 200, 300], 'Time': [1.5, 2, 3, 3.5]},
    'Walk Way': {'Price': [70, 100, 130, 170], 'Time': [1, 2, 3, 3.5]},
    'Car': {'Price': [30, 30, 30, 30], 'Time': [0.25, 0.25, 0.25, 0.25]},
    'Chimney': {'Price': [50, 75, 100, 125], 'Time': [0.25, 0.75, 1, 1.25]},
    'Window Wash': {'Price': [30, 60, 80, 100], 'Time': [0.25, 0.5, .75, 1]},
    'Window Screen Repair': {'Price': [10, 20, 30, 50], 'Time': [1, 1.5, 2, 3]},
    'Side Walk': {'Price': [0, 0, 0, 0], 'Time': [0, 0, 0, 0]}
}
sizes = ['Small', 'Medium', 'Large', 'XL']

# Streamlit application starts here
st.title('Service Cost and Time Calculator')

# Containers for selections and calculations
selected_services = {}
service_details = []

# Discount factors
discounts = [1, 0.70, 0.75, 0.80, 0.85, 0.9, 0.95, 1]  # Extend as needed

# Generate checkboxes and size options
for service, details in services_data.items():
    if st.checkbox(f'{service}', key=service):
        size_index = sizes.index(st.selectbox(f'Choose size for {service}', sizes, key=f'size_{service}'))
        price = details['Price'][size_index]
        time = details['Time'][size_index]
        selected_services[service] = {'Size': sizes[size_index], 'Price': price, 'Time': time}

# Button to calculate total
if st.button('Calculate Total'):
    # Sort services by cost in descending order
    sorted_services = sorted(selected_services.items(), key=lambda x: x[1]['Price'], reverse=True)
    total_cost = 0
    pre_discount_total = 0  # Initialize pre-discount total cost
    total_time = 0
    display_costs = []
    # Apply discounts and calculate total cost and time
    for i, (service, info) in enumerate(sorted_services):
        discount = discounts[i] if i < len(discounts) else 0.1  # Use 0.1 if not enough predefined discounts
        discounted_cost = info['Price'] * discount
        total_cost += discounted_cost
        pre_discount_total += info['Price']  # Sum full price
        total_time += info['Time']
        display_costs.append(f"{info['Size']} {service}: ${info['Price']} ({discount}) --> ${discounted_cost:.2f}, Time: {info['Time']} hrs")

    display_costs.append('-' * 30)
    display_costs.append(f"Pre-Discount Total: ${pre_discount_total:.2f}")  # Display pre-discount total
    display_costs.append(f"Total Cost: ${total_cost:.2f}")
    display_costs.append(f"Total Time: {total_time:.2f} hrs")

    # Update display
    cost_display = st.text_area("Selected Services, Costs, and Times",
                                value='\n'.join(display_costs),
                                height=300)

