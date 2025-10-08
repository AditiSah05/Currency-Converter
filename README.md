# 💱 Currency Converter (Tkinter Application)

A sleek, modern **Currency Converter** built with **Python and Tkinter**, providing real-time exchange rates with an interactive and user-friendly interface.  
The app supports over 30 global currencies with country flags, keypad input, and instant conversion.

---

## 🌍 Features:

- 🔁 **Real-Time Exchange Rates** fetched from [ExchangeRate API](https://www.exchangerate-api.com/)
- 🏳️ **Country Flags** displayed dynamically via [flagcdn.com](https://flagcdn.com)
- ⚡ **Instant Conversion** — updates automatically as you type
- 🔄 **Swap Currencies** with a single click
- 💡 **Offline Fallback Rates** (when API is unavailable)
- 🎨 **Modern UI/UX** designed for simplicity and readability

---

## 🧠 How It Works

1. The app fetches the latest exchange rates using the **ExchangeRate API**.  
2. Flag images for currencies are retrieved from **FlagCDN**.  
3. If the API fails, the app uses **predefined fallback rates**.  
4. Conversion formula used: converted_amount = (amount / rate[from_currency]) * rate[to_currency]
   
---

## 🧰 Technologies Used

- **Python 3**
- **Tkinter** — GUI Framework
- **Pillow (PIL)** — Image Handling
- **Requests** — API Integration
- **FlagCDN & ExchangeRate API** — External Data Sources

---

## 📦 Installation

### 1. Clone the Repository
`bash
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
2. Install Required Libraries
pip install requests pillow

3. Run the Application
python app.py

🖥️ User Interface Overview
Amount Entry: Enter the value to convert using the on-screen keypad.

Dropdowns: Select source and target currencies.

Flags: Display automatically for selected currencies.

Swap Button (⇅): Instantly swap between currencies.

Converted Amount: Displayed dynamically below.

<img width="497" height="848" alt="image" src="https://github.com/user-attachments/assets/5e7da180-7ac5-4741-aeb1-ef60bc951bdf" />
