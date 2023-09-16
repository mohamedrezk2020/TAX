# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:35:29 2019

@author: MuHaMmEd
"""

# Programming Exercise 13-5

import tkinter

class PropertyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create frames
        self.value_frame = tkinter.Frame(self.main_window)
        self.assess_frame = tkinter.Frame(self.main_window)
        self.tax_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the value frame
        self.value_label = tkinter.Label \
                           (self.value_frame, \
                            text = 'Enter the property value: $')
        self.value_entry = tkinter.Entry(self.value_frame, width = 10)

        # Pack the value frame widgets
        self.value_label.pack(side = 'left')
        self.value_entry.pack(side = 'left')

        # Create the widgets for the assess frame
        self.assess_results_label = tkinter.Label \
                                    (self.assess_frame, \
                                     text = 'Assessment Value: ')
                  
        # Create a blank label for assessment value
        self.assess = tkinter.StringVar()
        self.assess_label = tkinter.Label(self.assess_frame, \
                                          textvariable= self.assess)

        # Pack the assess frame widgets
        self.assess_results_label.pack(side = 'left')
        self.assess_label.pack(side = 'left')

        # Create the widgets for the tax frame
        self.tax_results_label = tkinter.Label \
                                 (self.tax_frame, \
                                  text = 'Property Tax: ')
                  
        # Create a blank label for property tax value
        self.tax = tkinter.StringVar()
        self.tax_label = tkinter.Label(self.tax_frame, \
                                       textvariable= self.tax)

        # Pack the tax frame widgets
        self.tax_results_label.pack(side = 'left')
        self.tax_label.pack(side = 'left')
                                                           
        # Create the two buttons in the bottom frame
        self.display_button = tkinter.Button \
                              (self.bottom_frame, \
                               text = 'Calculate', \
                               command = self.calculate)
        self.quit_button = tkinter.Button \
                           (self.bottom_frame, \
                            text = 'Quit', \
                            command = self.main_window.destroy)
              
        # Pack the widgets in the bottom frame
        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')
                
        # Pack the frames
        self.value_frame.pack()
        self.assess_frame.pack()
        self.tax_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def calculate(self):
        # Get the values entered
        self.value = float(self.value_entry.get())

        # Calculate assessment
        self.assessment = 0.60 * self.value

        # Update the assessment label
        self.assess.set('$' + str(self.assessment))

        # Calculate tax
        self.property_tax = float(self.assessment) / 100 * 0.75
        
        # Update the tax label
        self.tax.set('$' + str(self.property_tax))
        
# Create an instance of PropertyGUI
prop = PropertyGUI()


