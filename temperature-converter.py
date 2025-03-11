from nicegui import ui

ui.colors(
      primary='#890ca6',
      secondary='#3ab0a4',
      accent='#8c0ba3',
      positive='#00bb00',
      negative='#b00505',
      info='#4158bf',
      warning='#ffa724'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: makes the text color the positive color (#38e31e)
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: makes the text color the negative color (#b00505)

with ui.row().classes("flex flex-col md:flex-row gap-6 justify-center"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-gradient-to-br from-white to-gray-100"):
        # w-100: Set element width to be fixed at 100
        # p-6: adds padding of 6 units on all sides
        # shadow-xl: extra large drop shadow effect
        # mx-auto: centers horizontally using auto margins
        # mt-10: adds margin-top spacing of 10 units
        # rounded-xl: adds extra large border radius for rounded corners
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: sets font size to 2xl
        # font-bold: bolds the text
        # text-accent: makes the text color the accent color (8c0ba3)
        # mb-4: adds margin-bottom spacing of 4 units
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border border-gray-300 rounded focus:border-primary focus:ring-2 focus:ring-primary-light focus:outline-none")
        # w-full: makes element take up 100% of the parent's width
        # border: adds border around the element
        # rounded: adds border radius for slightly rounded corners
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4 space-y-2")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded bg-primary hover:bg-accent transition-colors duration-300 text-lg")
        # text-white: sets text color to white
        # py-2: adds padding of 2 units on top and bottom
        # px-4: adds padding of 4 units on left and right
        result_label = ui.label("").classes("text-lg mt-4 p-2 bg-gray-50 rounded-md")

    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-gradient-to-br from-white to-gray-100"):
        ui.label("Slider Temperature Converter").classes("text-2xl font-bold text-primary mb-4")
        ui.label("Select Temperature:").classes("text-lg mb-2")
        
        # making the slider
        temperature_slider = ui.slider(min=-50, max=150, value=25, step=0.5).classes("w-full mb-4")
        
        # slider button selections (F vs. C or C vs F)
        slider_conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4 space-y-2")
        
        # display
        slider_result = ui.label(f"25°C = 77.00°F").classes("text-lg font-semibold text-positive mt-4 p-2 bg-gray-50 rounded-md")

        def slider_convert():
            value = temperature_slider.value
            if slider_conversion_type.value == "Celsius to Fahrenheit":
                slider_result.set_text(f"{value}°C = {value * 9/5 + 32:.2f}°F")
                slider_result.classes("text-lg font-semibold text-positive mt-4 p-2 bg-gray-50 rounded-md")
            else:
                slider_result.set_text(f"{value}°F = {(value - 32) * 5/9:.2f}°C") 
                slider_result.classes("text-lg font-semibold text-positive mt-4 p-2 bg-gray-50 rounded-md")

        temperature_slider.on("update:model-value", lambda e: slider_convert())
        
        slider_conversion_type.on("change", lambda: slider_convert())
        
        slider_convert()

ui.run()