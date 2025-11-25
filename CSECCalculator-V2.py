#!/usr/bin/env python3
import colorama
from colorama import init, Fore, Back, Style
import sys
import math
import cmath
import statistics
import time
import json
import os
from datetime import datetime
from collections import deque

# Initialize colorama
init(autoreset=True)

class CSECCalculator:
    def __init__(self):
        self.history = deque(maxlen=100)  # Store last 100 calculations
        self.memory = 0
        self.angle_mode = 'DEG'  # DEG or RAD
        self.settings = {
            'decimal_places': 6,
            'sci_notation': False,
            'history_enabled': True
        }
        self.load_history()
    
    def save_history(self):
        """Save calculation history to file"""
        try:
            with open('calculator_history.json', 'w') as f:
                json.dump(list(self.history), f)
        except:
            pass
    
    def load_history(self):
        """Load calculation history from file"""
        try:
            if os.path.exists('calculator_history.json'):
                with open('calculator_history.json', 'r') as f:
                    history_data = json.load(f)
                    self.history = deque(history_data, maxlen=100)
        except:
            pass
    
    def welcome(self):
        print(f'\n{Fore.CYAN}{"#"*60}')
        print(f'{Fore.CYAN}{"#"*60}')
        print(f'{Fore.GREEN}Welcome to CSEC Calculator v2.0')
        print(f'{Fore.YELLOW}Made by Cyb0rgBytes')
        print(f'{Fore.CYAN}{"#"*60}')
        print(f'{Fore.CYAN}{"#"*60}')
        print(f'{Fore.WHITE}Advanced features:')
        print(f'{Fore.WHITE}• Basic arithmetic & Scientific functions')
        print(f'{Fore.WHITE}• Trigonometry & Logarithms')
        print(f'{Fore.WHITE}• Complex numbers & Statistics')
        print(f'{Fore.WHITE}• Financial calculations & Unit conversions')
        print(f'{Fore.WHITE}• History & Memory functions')
        print(f'{Fore.CYAN}{"#"*60}\n')
    
    def animate_text(self, text, delay=0.03):
        """Display text with typing animation"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def format_result(self, result):
        """Format the result based on settings"""
        try:
            if self.settings['sci_notation'] and (abs(result) > 1e6 or (abs(result) < 1e-6 and result != 0)):
                return f"{result:.{self.settings['decimal_places']}e}"
            else:
                return f"{result:.{self.settings['decimal_places']}f}".rstrip('0').rstrip('.')
        except:
            return str(result)
    
    def get_number(self, prompt):
        """Get a number from user with validation"""
        while True:
            try:
                value = input(prompt)
                if value.lower() == 'ans' and self.history:
                    return self.history[-1]['result']
                elif value.lower() == 'mem':
                    return self.memory
                elif value.lower() == 'pi':
                    return math.pi
                elif value.lower() == 'e':
                    return math.e
                else:
                    return float(value)
            except ValueError:
                print(f"{Fore.RED}Invalid number! Please enter a valid number or 'ans', 'mem', 'pi', 'e'")
    
    def basic_operations(self):
        """Handle basic arithmetic operations"""
        print(f"\n{Fore.YELLOW}Basic Operations:")
        print(f"{Fore.WHITE}+ : Addition")
        print(f"{Fore.WHITE}- : Subtraction") 
        print(f"{Fore.WHITE}* : Multiplication")
        print(f"{Fore.WHITE}/ : Division")
        print(f"{Fore.WHITE}** : Power")
        print(f"{Fore.WHITE}% : Modulo")
        print(f"{Fore.WHITE}sqrt : Square Root")
        print(f"{Fore.WHITE}// : Floor Division")
        
        operation = input(f"{Fore.GREEN}Operation: ").strip().lower()
        
        if operation in ['+', '-', '*', '/', '**', '%', '//']:
            num1 = self.get_number(f"{Fore.GREEN}Enter first number: ")
            num2 = self.get_number(f"{Fore.GREEN}Enter second number: ")
            
            try:
                if operation == '+':
                    result = num1 + num2
                    expression = f"{num1} + {num2}"
                elif operation == '-':
                    result = num1 - num2
                    expression = f"{num1} - {num2}"
                elif operation == '*':
                    result = num1 * num2
                    expression = f"{num1} × {num2}"
                elif operation == '/':
                    if num2 == 0:
                        raise ZeroDivisionError("Division by zero!")
                    result = num1 / num2
                    expression = f"{num1} ÷ {num2}"
                elif operation == '**':
                    result = num1 ** num2
                    expression = f"{num1} ^ {num2}"
                elif operation == '%':
                    result = num1 % num2
                    expression = f"{num1} % {num2}"
                elif operation == '//':
                    result = num1 // num2
                    expression = f"{num1} // {num2}"
                
                self.display_result(expression, result)
                
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
        
        elif operation == 'sqrt':
            num = self.get_number(f"{Fore.GREEN}Enter number: ")
            if num < 0:
                result = cmath.sqrt(num)
                expression = f"√({num})"
            else:
                result = math.sqrt(num)
                expression = f"√{num}"
            self.display_result(expression, result)
    
    def scientific_operations(self):
        """Handle scientific operations"""
        print(f"\n{Fore.YELLOW}Scientific Operations:")
        print(f"{Fore.WHITE}sin/cos/tan : Trigonometric functions")
        print(f"{Fore.WHITE}asin/acos/atan : Inverse trigonometric")
        print(f"{Fore.WHITE}log/ln : Logarithms")
        print(f"{Fore.WHITE}exp : Exponential")
        print(f"{Fore.WHITE}fact : Factorial")
        print(f"{Fore.WHITE}perm/comb : Permutations/Combinations")
        print(f"{Fore.WHITE}abs : Absolute value")
        
        operation = input(f"{Fore.GREEN}Operation: ").strip().lower()
        
        if operation in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']:
            num = self.get_number(f"{Fore.GREEN}Enter angle: ")
            
            # Convert to radians if in degree mode
            if self.angle_mode == 'DEG' and operation in ['sin', 'cos', 'tan']:
                angle_rad = math.radians(num)
            else:
                angle_rad = num
            
            try:
                if operation == 'sin':
                    result = math.sin(angle_rad)
                elif operation == 'cos':
                    result = math.cos(angle_rad)
                elif operation == 'tan':
                    result = math.tan(angle_rad)
                elif operation == 'asin':
                    result = math.asin(num)
                    if self.angle_mode == 'DEG':
                        result = math.degrees(result)
                elif operation == 'acos':
                    result = math.acos(num)
                    if self.angle_mode == 'DEG':
                        result = math.degrees(result)
                elif operation == 'atan':
                    result = math.atan(num)
                    if self.angle_mode == 'DEG':
                        result = math.degrees(result)
                
                expression = f"{operation}({num})"
                self.display_result(expression, result)
                
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
        
        elif operation in ['log', 'ln', 'exp']:
            num = self.get_number(f"{Fore.GREEN}Enter number: ")
            
            try:
                if operation == 'log':
                    result = math.log10(num)
                    expression = f"log₁₀({num})"
                elif operation == 'ln':
                    result = math.log(num)
                    expression = f"ln({num})"
                elif operation == 'exp':
                    result = math.exp(num)
                    expression = f"e^{num}"
                
                self.display_result(expression, result)
                
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
        
        elif operation == 'fact':
            num = self.get_number(f"{Fore.GREEN}Enter integer: ")
            
            try:
                if num < 0 or num != int(num):
                    raise ValueError("Factorial requires non-negative integer")
                result = math.factorial(int(num))
                expression = f"{int(num)}!"
                self.display_result(expression, result)
                
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
        
        elif operation in ['perm', 'comb']:
            n = self.get_number(f"{Fore.GREEN}Enter n: ")
            r = self.get_number(f"{Fore.GREEN}Enter r: ")
            
            try:
                if n < 0 or r < 0 or n != int(n) or r != int(r) or r > n:
                    raise ValueError("Invalid values for permutation/combination")
                
                n, r = int(n), int(r)
                
                if operation == 'perm':
                    result = math.perm(n, r)
                    expression = f"P({n},{r})"
                else:
                    result = math.comb(n, r)
                    expression = f"C({n},{r})"
                
                self.display_result(expression, result)
                
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
    
    def financial_operations(self):
        """Handle financial calculations"""
        print(f"\n{Fore.YELLOW}Financial Operations:")
        print(f"{Fore.WHITE}fv : Future Value")
        print(f"{Fore.WHITE}pv : Present Value")
        print(f"{Fore.WHITE}pmt : Loan Payment")
        print(f"{Fore.WHITE}nper : Number of Periods")
        print(f"{Fore.WHITE}rate : Interest Rate")
        
        operation = input(f"{Fore.GREEN}Operation: ").strip().lower()
        
        if operation == 'fv':
            pv = self.get_number("Present Value: ")
            rate = self.get_number("Interest rate per period (decimal): ")
            nper = self.get_number("Number of periods: ")
            
            result = pv * (1 + rate) ** nper
            expression = f"FV(PV={pv}, rate={rate}, n={nper})"
            self.display_result(expression, result)
        
        elif operation == 'pv':
            fv = self.get_number("Future Value: ")
            rate = self.get_number("Interest rate per period (decimal): ")
            nper = self.get_number("Number of periods: ")
            
            result = fv / (1 + rate) ** nper
            expression = f"PV(FV={fv}, rate={rate}, n={nper})"
            self.display_result(expression, result)
        
        elif operation == 'pmt':
            pv = self.get_number("Loan amount: ")
            rate = self.get_number("Interest rate per period (decimal): ")
            nper = self.get_number("Number of periods: ")
            
            if rate == 0:
                result = pv / nper
            else:
                result = pv * rate * (1 + rate) ** nper / ((1 + rate) ** nper - 1)
            
            expression = f"PMT(PV={pv}, rate={rate}, n={nper})"
            self.display_result(expression, result)
    
    def complex_operations(self):
        """Handle complex number operations"""
        print(f"\n{Fore.YELLOW}Complex Number Operations:")
        print(f"{Fore.WHITE}Enter complex numbers as: a+bj")
        
        operation = input(f"{Fore.GREEN}Operation (+, -, *, /, **, polar, rect): ").strip().lower()
        
        if operation in ['+', '-', '*', '/', '**']:
            c1_str = input("First complex number (a+bj): ")
            c2_str = input("Second complex number (a+bj): ")
            
            try:
                c1 = complex(c1_str)
                c2 = complex(c2_str)
                
                if operation == '+':
                    result = c1 + c2
                elif operation == '-':
                    result = c1 - c2
                elif operation == '*':
                    result = c1 * c2
                elif operation == '/':
                    result = c1 / c2
                elif operation == '**':
                    result = c1 ** c2
                
                expression = f"({c1}) {operation} ({c2})"
                self.display_result(expression, result)
                
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
        
        elif operation == 'polar':
            real = self.get_number("Real part: ")
            imag = self.get_number("Imaginary part: ")
            
            magnitude = math.sqrt(real**2 + imag**2)
            phase = math.atan2(imag, real)
            
            print(f"{Fore.GREEN}Polar form: {magnitude:.6f} ∠ {phase:.6f} rad")
            if self.angle_mode == 'DEG':
                print(f"{Fore.GREEN}In degrees: {magnitude:.6f} ∠ {math.degrees(phase):.6f}°")
        
        elif operation == 'rect':
            magnitude = self.get_number("Magnitude: ")
            phase = self.get_number("Phase (radians): ")
            
            real = magnitude * math.cos(phase)
            imag = magnitude * math.sin(phase)
            
            print(f"{Fore.GREEN}Rectangular form: {real:.6f} + {imag:.6f}j")
    
    def statistics_operations(self):
        """Handle statistical operations"""
        print(f"\n{Fore.YELLOW}Statistical Operations:")
        print(f"{Fore.WHITE}Enter numbers separated by spaces")
        
        data_str = input(f"{Fore.GREEN}Enter data: ")
        
        try:
            data = [float(x) for x in data_str.split()]
            
            if not data:
                print(f"{Fore.RED}No data entered!")
                return
            
            print(f"\n{Fore.CYAN}Statistical Results:")
            print(f"{Fore.WHITE}Count: {len(data)}")
            print(f"{Fore.WHITE}Mean: {statistics.mean(data):.6f}")
            print(f"{Fore.WHITE}Median: {statistics.median(data):.6f}")
            print(f"{Fore.WHITE}Mode: {statistics.mode(data) if len(data) == len(set(data)) else 'No unique mode'}")
            print(f"{Fore.WHITE}Standard Deviation: {statistics.stdev(data):.6f}")
            print(f"{Fore.WHITE}Variance: {statistics.variance(data):.6f}")
            print(f"{Fore.WHITE}Min: {min(data):.6f}")
            print(f"{Fore.WHITE}Max: {max(data):.6f}")
            print(f"{Fore.WHITE}Range: {max(data) - min(data):.6f}")
            
        except Exception as e:
            print(f"{Fore.RED}Error: {e}")
    
    def memory_operations(self):
        """Handle memory operations"""
        print(f"\n{Fore.YELLOW}Memory Operations:")
        print(f"{Fore.WHITE}store : Store value in memory")
        print(f"{Fore.WHITE}recall : Recall value from memory") 
        print(f"{Fore.WHITE}clear : Clear memory")
        print(f"{Fore.WHITE}add : Add to memory")
        print(f"{Fore.WHITE}subtract : Subtract from memory")
        
        operation = input(f"{Fore.GREEN}Operation: ").strip().lower()
        
        if operation == 'store':
            value = self.get_number("Value to store: ")
            self.memory = value
            print(f"{Fore.GREEN}Value {value} stored in memory")
        
        elif operation == 'recall':
            print(f"{Fore.GREEN}Memory value: {self.memory}")
        
        elif operation == 'clear':
            self.memory = 0
            print(f"{Fore.GREEN}Memory cleared")
        
        elif operation == 'add':
            value = self.get_number("Value to add: ")
            self.memory += value
            print(f"{Fore.GREEN}Added {value} to memory. New value: {self.memory}")
        
        elif operation == 'subtract':
            value = self.get_number("Value to subtract: ")
            self.memory -= value
            print(f"{Fore.GREEN}Subtracted {value} from memory. New value: {self.memory}")
    
    def unit_conversions(self):
        """Handle unit conversions"""
        print(f"\n{Fore.YELLOW}Unit Conversions:")
        print(f"{Fore.WHITE}deg2rad : Degrees to Radians")
        print(f"{Fore.WHITE}rad2deg : Radians to Degrees")
        print(f"{Fore.WHITE}c2f : Celsius to Fahrenheit")
        print(f"{Fore.WHITE}f2c : Fahrenheit to Celsius")
        
        operation = input(f"{Fore.GREEN}Operation: ").strip().lower()
        
        if operation == 'deg2rad':
            deg = self.get_number("Degrees: ")
            rad = math.radians(deg)
            print(f"{Fore.GREEN}{deg}° = {rad:.6f} radians")
        
        elif operation == 'rad2deg':
            rad = self.get_number("Radians: ")
            deg = math.degrees(rad)
            print(f"{Fore.GREEN}{rad} radians = {deg:.6f}°")
        
        elif operation == 'c2f':
            celsius = self.get_number("Celsius: ")
            fahrenheit = celsius * 9/5 + 32
            print(f"{Fore.GREEN}{celsius}°C = {fahrenheit:.2f}°F")
        
        elif operation == 'f2c':
            fahrenheit = self.get_number("Fahrenheit: ")
            celsius = (fahrenheit - 32) * 5/9
            print(f"{Fore.GREEN}{fahrenheit}°F = {celsius:.2f}°C")
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print(f"{Fore.YELLOW}No history available")
            return
        
        print(f"\n{Fore.CYAN}{'Calculation History':^50}")
        print(f"{Fore.CYAN}{'-'*50}")
        
        for i, entry in enumerate(reversed(self.history), 1):
            print(f"{Fore.WHITE}{i:2d}. {entry['expression']} = {self.format_result(entry['result'])}")
    
    def settings_menu(self):
        """Display and modify calculator settings"""
        while True:
            print(f"\n{Fore.YELLOW}Calculator Settings:")
            print(f"{Fore.WHITE}1. Decimal places: {self.settings['decimal_places']}")
            print(f"{Fore.WHITE}2. Scientific notation: {'On' if self.settings['sci_notation'] else 'Off'}")
            print(f"{Fore.WHITE}3. Angle mode: {self.angle_mode}")
            print(f"{Fore.WHITE}4. History: {'Enabled' if self.settings['history_enabled'] else 'Disabled'}")
            print(f"{Fore.WHITE}5. Clear all history")
            print(f"{Fore.WHITE}6. Back to main menu")
            
            choice = input(f"{Fore.GREEN}Select option (1-6): ").strip()
            
            if choice == '1':
                try:
                    places = int(input("Decimal places (0-15): "))
                    if 0 <= places <= 15:
                        self.settings['decimal_places'] = places
                        print(f"{Fore.GREEN}Decimal places set to {places}")
                    else:
                        print(f"{Fore.RED}Please enter a value between 0 and 15")
                except ValueError:
                    print(f"{Fore.RED}Invalid number!")
            
            elif choice == '2':
                self.settings['sci_notation'] = not self.settings['sci_notation']
                status = "On" if self.settings['sci_notation'] else "Off"
                print(f"{Fore.GREEN}Scientific notation turned {status}")
            
            elif choice == '3':
                self.angle_mode = 'RAD' if self.angle_mode == 'DEG' else 'DEG'
                print(f"{Fore.GREEN}Angle mode set to {self.angle_mode}")
            
            elif choice == '4':
                self.settings['history_enabled'] = not self.settings['history_enabled']
                status = "Enabled" if self.settings['history_enabled'] else "Disabled"
                print(f"{Fore.GREEN}History {status}")
            
            elif choice == '5':
                self.history.clear()
                print(f"{Fore.GREEN}History cleared")
            
            elif choice == '6':
                break
    
    def display_result(self, expression, result):
        """Display result with animation and store in history"""
        # Animation effect
        print(f"\n{Fore.YELLOW}Calculating", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.3)
        
        print(f"\n{Fore.CYAN}{expression} = {Fore.GREEN}{self.format_result(result)}")
        
        # Store in history
        if self.settings['history_enabled']:
            self.history.append({
                'expression': expression,
                'result': result,
                'timestamp': datetime.now().isoformat()
            })
            self.save_history()
    
    def main_menu(self):
        """Display main menu and handle user input"""
        while True:
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"{Fore.CYAN}{'MAIN MENU':^60}")
            print(f"{Fore.CYAN}{'='*60}")
            print(f"{Fore.WHITE}1. Basic Operations")
            print(f"{Fore.WHITE}2. Scientific Operations")
            print(f"{Fore.WHITE}3. Financial Calculations")
            print(f"{Fore.WHITE}4. Complex Numbers")
            print(f"{Fore.WHITE}5. Statistics")
            print(f"{Fore.WHITE}6. Memory Operations")
            print(f"{Fore.WHITE}7. Unit Conversions")
            print(f"{Fore.WHITE}8. View History")
            print(f"{Fore.WHITE}9. Settings")
            print(f"{Fore.WHITE}0. Exit")
            print(f"{Fore.CYAN}{'='*60}")
            
            choice = input(f"{Fore.GREEN}Select option (0-9): ").strip()
            
            if choice == '1':
                self.basic_operations()
            elif choice == '2':
                self.scientific_operations()
            elif choice == '3':
                self.financial_operations()
            elif choice == '4':
                self.complex_operations()
            elif choice == '5':
                self.statistics_operations()
            elif choice == '6':
                self.memory_operations()
            elif choice == '7':
                self.unit_conversions()
            elif choice == '8':
                self.show_history()
            elif choice == '9':
                self.settings_menu()
            elif choice == '0':
                print(f"{Fore.BLUE}Thank you for using CSEC Calculator v2.0!")
                print(f"{Fore.BLUE}Goodbye!")
                break
            else:
                print(f"{Fore.RED}Invalid choice! Please select 0-9")

def main():
    calculator = CSECCalculator()
    calculator.welcome()
    
    # Animated welcome message
    calculator.animate_text(f"{Fore.GREEN}Initializing advanced calculator systems...")
    time.sleep(0.5)
    calculator.animate_text(f"{Fore.GREEN}Loading mathematical modules...")
    time.sleep(0.5)
    calculator.animate_text(f"{Fore.GREEN}Ready for complex computations!")
    time.sleep(0.5)
    
    calculator.main_menu()

if __name__ == "__main__":
    main()
