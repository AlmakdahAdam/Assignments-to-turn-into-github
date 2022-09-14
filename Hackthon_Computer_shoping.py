
m_expensive_laptop_amount = 4295.54
l_expensive_laptop_amount = 1849.79
msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zephyrus_m16_price = 1849.79

def function(most_expensive, least_expensive):
    most_expensive = (m_expensive_laptop_amount)
    print(f"The most expensive laptop amount is {most_expensive}")
    least_expensive = (l_expensive_laptop_amount)
    print(f"The least expensive laptop amount is {least_expensive}")
    msi_price = round(msi_rtxa5000_price)
    print(f"The rounded price of the MSI RTX 5000 is {msi_price}")
    giga_price = round(gigabyte_aero_price)
    print(f"The rounded price of the Gigabyte Aero is {giga_price}")
    razer_price = round(razer_blade15_price)
    print(f"The rounded pruce of the Razer Blade 15 is {razer_price}")
    asus_price = round(asus_zephyrus_m16_price)
    print(f"The rounded price of the Asus Zephyrus is {asus_price}")
    average = (msi_rtxa5000_price + gigabyte_aero_price + razer_blade15_price + asus_zephyrus_m16_price) / 4
    print(f"The average price of all computers is {average:.2f}")
function(gigabyte_aero_price, asus_zephyrus_m16_price)
