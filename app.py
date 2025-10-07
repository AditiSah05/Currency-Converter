import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f5")
        
        # Variables
        self.amount_var = tk.StringVar(value="1000.00")
        self.from_currency = tk.StringVar(value="USD")
        self.to_currency = tk.StringVar(value="NPR")
        self.converted_var = tk.StringVar(value="0.00")
        
        # Currency country codes for flag images
        self.currency_countries = {
            "USD": "us",    # United States Dollar
            "EUR": "eu",    # Euro
            "GBP": "gb",    # British Pound
            "INR": "in",    # Indian Rupee
            "NPR": "np",    # Nepalese Rupee
            "JPY": "jp",    # Japanese Yen
            "CNY": "cn",    # Chinese Yuan
            "AUD": "au",    # Australian Dollar
            "CAD": "ca",    # Canadian Dollar
            "CHF": "ch",    # Swiss Franc
            "SGD": "sg",    # Singapore Dollar
            "HKD": "hk",    # Hong Kong Dollar
            "NZD": "nz",    # New Zealand Dollar
            "KRW": "kr",    # South Korean Won
            "MXN": "mx",    # Mexican Peso
            "BRL": "br",    # Brazilian Real
            "ZAR": "za",    # South African Rand
            "AED": "ae",    # UAE Dirham
            "SAR": "sa",    # Saudi Riyal
            "THB": "th",    # Thai Baht
            "MYR": "my",    # Malaysian Ringgit
            "IDR": "id",    # Indonesian Rupiah
            "PHP": "ph",    # Philippine Peso
            "VND": "vn",    # Vietnamese Dong
            "PKR": "pk",    # Pakistani Rupee
            "BDT": "bd",    # Bangladeshi Taka
            "LKR": "lk",    # Sri Lankan Rupee
            "SEK": "se",    # Swedish Krona
            "NOK": "no",    # Norwegian Krone
            "DKK": "dk",    # Danish Krone
            "PLN": "pl",    # Polish Zloty
            "TRY": "tr",    # Turkish Lira
            "RUB": "ru",    # Russian Ruble
            "TWD": "tw",    # Taiwan Dollar
        }
        
        self.flag_images = {}
        self.exchange_rates = {}
        
        self.load_flags()
        self.fetch_exchange_rates()
        
        self.create_widgets()
        self.calculate_conversion()
    
    def load_flags(self):
        """Load flag images from flagcdn.com"""
        for currency, country_code in self.currency_countries.items():
            try:
                # Using flagcdn.com for flag images
                url = f"https://flagcdn.com/48x36/{country_code}.png"
                response = requests.get(url, timeout=5)
                img_data = Image.open(BytesIO(response.content))
                img_data = img_data.resize((32, 24), Image.Resampling.LANCZOS)
                self.flag_images[currency] = ImageTk.PhotoImage(img_data)
            except:
                # Create a placeholder if flag loading fails
                placeholder = Image.new('RGB', (32, 24), color='#cccccc')
                self.flag_images[currency] = ImageTk.PhotoImage(placeholder)
    
    def fetch_exchange_rates(self):
        """Fetch real-time exchange rates from API"""
        try:
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)
            data = response.json()
            self.exchange_rates = data["rates"]
        except:
            # Fallback rates if API fails
            self.exchange_rates = {
                "USD": 1.0, "EUR": 0.92, "GBP": 0.79, "INR": 83.12,
                "NPR": 132.50, "JPY": 149.50, "CNY": 7.24, "AUD": 1.52,
                "CAD": 1.36, "CHF": 0.88, "SGD": 1.34, "HKD": 7.83,
                "NZD": 1.64, "KRW": 1342.50, "MXN": 17.15, "BRL": 4.97,
                "ZAR": 18.65, "AED": 3.67, "SAR": 3.75, "THB": 35.50,
                "MYR": 4.72, "IDR": 15650, "PHP": 56.80, "VND": 24500,
                "PKR": 278.50, "BDT": 110.25, "LKR": 325.80, "SEK": 10.87,
                "NOK": 10.93, "DKK": 6.86, "PLN": 4.03, "TRY": 32.15,
                "RUB": 92.50, "TWD": 32.20
            }
    
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#4a5a8a", height=120)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="Currency Converter", 
                              font=("Helvetica", 22, "bold"), 
                              bg="#4a5a8a", fg="white")
        title_label.pack(pady=15)
        
        subtitle_label = tk.Label(header_frame, 
                                 text="Check live rates, set rate alerts, receive\nnotifications and more.",
                                 font=("Helvetica", 10), 
                                 bg="#4a5a8a", fg="#d0d0e0")
        subtitle_label.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#f0f0f5")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Amount Section
        amount_label = tk.Label(main_frame, text="Amount", 
                               font=("Helvetica", 11), 
                               bg="#f0f0f5", fg="#666")
        amount_label.pack(anchor="w", pady=(0, 5))
        
        amount_frame = tk.Frame(main_frame, bg="white", relief=tk.FLAT, bd=1, highlightthickness=1, highlightbackground="#ddd")
        amount_frame.pack(fill=tk.X, pady=(0, 15))
        
        # From currency section
        from_frame = tk.Frame(amount_frame, bg="white")
        from_frame.pack(side=tk.LEFT, padx=10, pady=12)
        
        # Flag image
        self.from_flag_label = tk.Label(from_frame, image=self.flag_images[self.from_currency.get()],
                                       bg="white")
        self.from_flag_label.pack(side=tk.LEFT, padx=(0, 8))
        
        from_dropdown = ttk.Combobox(from_frame, textvariable=self.from_currency,
                                    values=list(self.currency_countries.keys()),
                                    state="readonly", width=6, font=("Helvetica", 12))
        from_dropdown.pack(side=tk.LEFT)
        from_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_from_flag())
        
        # Amount entry
        amount_entry = tk.Entry(amount_frame, textvariable=self.amount_var,
                               font=("Helvetica", 16), bg="white", 
                               relief=tk.FLAT, justify=tk.RIGHT, bd=0)
        amount_entry.pack(side=tk.RIGHT, padx=15, pady=12, fill=tk.X, expand=True)
        amount_entry.bind("<KeyRelease>", lambda e: self.calculate_conversion())
        
        # Swap button
        swap_btn = tk.Button(main_frame, text="⇅", font=("Helvetica", 20, "bold"),
                           bg="#3d4d7a", fg="white", width=3, height=1,
                           relief=tk.FLAT, cursor="hand2",
                           command=self.swap_currencies)
        swap_btn.pack(pady=10)
        
        # Converted Amount Section
        converted_label = tk.Label(main_frame, text="Converted Amount",
                                  font=("Helvetica", 11),
                                  bg="#f0f0f5", fg="#666")
        converted_label.pack(anchor="w", pady=(5, 5))
        
        converted_frame = tk.Frame(main_frame, bg="white", relief=tk.FLAT, bd=1, highlightthickness=1, highlightbackground="#ddd")
        converted_frame.pack(fill=tk.X, pady=(0, 20))
        
        # To currency section
        to_frame = tk.Frame(converted_frame, bg="white")
        to_frame.pack(side=tk.LEFT, padx=10, pady=12)
        
        # Flag image
        self.to_flag_label = tk.Label(to_frame, image=self.flag_images[self.to_currency.get()],
                                     bg="white")
        self.to_flag_label.pack(side=tk.LEFT, padx=(0, 8))
        
        to_dropdown = ttk.Combobox(to_frame, textvariable=self.to_currency,
                                  values=list(self.currency_countries.keys()),
                                  state="readonly", width=6, font=("Helvetica", 12))
        to_dropdown.pack(side=tk.LEFT)
        to_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_to_flag())
        
        # Converted amount display
        converted_display = tk.Label(converted_frame, textvariable=self.converted_var,
                                    font=("Helvetica", 16, "bold"), bg="white",
                                    fg="#333", anchor="e")
        converted_display.pack(side=tk.RIGHT, padx=15, pady=12, fill=tk.X, expand=True)
        
        # Keypad (numbers only, no alphabet letters)
        keypad_frame = tk.Frame(main_frame, bg="#e8e8f0")
        keypad_frame.pack(fill=tk.BOTH, expand=True)
        
        buttons = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['.', '0', '⌫']
        ]
        
        for i, row in enumerate(buttons):
            row_frame = tk.Frame(keypad_frame, bg="#e8e8f0")
            row_frame.pack(fill=tk.X, expand=True, pady=2)
            
            for j, btn_val in enumerate(row):
                btn = tk.Button(row_frame, text=btn_val,
                              font=("Helvetica", 16, "bold"),
                              bg="white", fg="#333",
                              relief=tk.FLAT, cursor="hand2",
                              command=lambda x=btn_val: self.keypad_press(x))
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
    
    def update_from_flag(self):
        """Update from currency flag"""
        currency = self.from_currency.get()
        self.from_flag_label.config(image=self.flag_images[currency])
        self.calculate_conversion()
    
    def update_to_flag(self):
        """Update to currency flag"""
        currency = self.to_currency.get()
        self.to_flag_label.config(image=self.flag_images[currency])
        self.calculate_conversion()
    
    def keypad_press(self, value):
        """Handle keypad button press"""
        current = self.amount_var.get()
        
        if value == '⌫':
            if len(current) > 0:
                self.amount_var.set(current[:-1])
        elif value == '.':
            if '.' not in current:
                if current == "":
                    self.amount_var.set("0.")
                else:
                    self.amount_var.set(current + '.')
        else:
            if current == "0.00" or current == "0":
                self.amount_var.set(value)
            else:
                self.amount_var.set(current + value)
        
        self.calculate_conversion()
    
    def swap_currencies(self):
        """Swap from and to currencies"""
        temp = self.from_currency.get()
        self.from_currency.set(self.to_currency.get())
        self.to_currency.set(temp)
        
        self.from_flag_label.config(image=self.flag_images[self.from_currency.get()])
        self.to_flag_label.config(image=self.flag_images[self.to_currency.get()])
        
        self.calculate_conversion()
    
    def calculate_conversion(self):
        """Calculate currency conversion"""
        try:
            amount = float(self.amount_var.get() or 0)
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            # Convert through USD as base
            amount_in_usd = amount / self.exchange_rates[from_curr]
            converted_amount = amount_in_usd * self.exchange_rates[to_curr]
            
            self.converted_var.set(f"{converted_amount:.2f}")
        except ValueError:
            self.converted_var.set("0.00")
        except Exception as e:
            print(f"Conversion error: {e}")
            self.converted_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()