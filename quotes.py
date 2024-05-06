import streamlit as st
import pandas as pd

# Define the data in a DataFrame
data = {
    'House Wash': [100, 200, 300, 500],
    'Patio Wash': [100, 200, 300, 500],
    'Perimiters': [200, 300, 425, 500],
    'Gutter Clean': [75, 125, 175, 250],
    'Roof Wash': [200, 300, 400, 600],
    'Driveway': [100, 150, 200, 300],
    'Walk Way': [70, 85, 100, 120],
    'Car': [30, 30, 30, 30],
    'Chimney': [15, 20, 25, 35],
    'Window Wash': [20, 50, 60, 80],
    'Window Screen Repair': [5, 20, 30, 50],
    'Side Walk': [0, 0, 0, 0]
}
sizes = ['Small', 'Medium', 'Large', 'XL']
df = pd.DataFrame(data, index=sizes)

# Streamlit application starts here
st.title('Service Cost Calculator')

# Container for display
cost_display = st.empty()

# Containers for selections and calculations
selected_services = {}
service_costs = []

# Discount factors
discounts = [1, 0.6, 0.65, 0.70, 0.75, 0.8, 0.85, 0.9]  # Extend as needed for more services

# Generate checkboxes and size options
for service in df.columns:
    if st.checkbox(f'{service}', key=service):
        size = st.selectbox(f'Choose size for {service}', sizes, key=f'size_{service}')
        selected_services[service] = (size, df.at[size, service])

# Button to calculate total
if st.button('Calculate Total'):
    # Sort services by cost in descending order
    sorted_services = sorted(selected_services.items(), key=lambda x: x[1][1], reverse=True)
    total_cost = 0
    display_costs = []
    # Apply discounts and calculate total cost
    for i, (service, (size, cost)) in enumerate(sorted_services):
        discount = discounts[i] if i < len(discounts) else 0.1  # Use 0.1 if not enough predefined discounts
        discounted_cost = cost * discount
        total_cost += discounted_cost
        display_costs.append(f"{size[0]} {service}: {cost} ({discount}) --> {discounted_cost:.2f}")
    display_costs.append('-' * 30)
    display_costs.append(f"\n\nTotal Cost: ${total_cost:.2f}")

    # Update display
    cost_display.text_area("Selected Services and Costs",
                           value='\n'.join(display_costs),
                           height=300)
    
    # Display total cost
    st.write(f'Total Cost: ${total_cost:.2f}')

# Run this script using: streamlit run services_calculator.py
