login_url = 'https://smartapi.bboxx.co.uk/v1/auth/login'
dashboard_url = 'https://smart.bboxx.co.uk/#/dashboard'
file_path = 'Data/ss_input_data.xlsx'

# product_imei = 866557056453766
def params_url(product_imei):
    parameters_url = f'https://smartapi.bboxx.co.uk/v1/products/{product_imei}/parameters'

    return parameters_url