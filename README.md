# supreme-bot
A free to use bot for supremenewyork.com that allows multiple-item checkout

## Requirements
- Python 3
- Google Chrome
- ChromeDriver

## Usage
1. Clone the project:
   ```
   $ git clone https://github.com/mDemianchuk/supreme-bot.git
   ```

2. Install dependencies:
    ```
    $ cd supreme-bot
    $ pip3 install -r requirements.txt   
    ```

3. Download [ChromDriver](https://chromedriver.chromium.org/downloads) for your version of Google Chrome, extract the executable, and place it in the root directory:

    ```
    supreme-bot/
    ├── bot.py
    ├── ...
    ├── chromedriver
    ```

4. Fill in the `settings.json`:

    ```  
    {
      "items": [                         
          {
              "name": "",                - full or partial item name (case-insensitive)
              "colorwayPosition": "",    - leave blank for any or use 1-base indexing
              "size": ""                 - must match sizes on supreme.com (Small, Medium, Large, etc.)
          }
      ],
      "billingInfo": {
          "fullName": "",
          "email": "",
          "phone": "",                   - digits only 
          "address": "",                 - street address only (city will be autocompleted by zip)
          "unit": "",                    - leave blank if not applicable
          "zip": "",
          "state": "",                   - use abbreviation
          "ccNumber": "",                - digits only 
          "expM": "",                    - must be two digit
          "expY": "",                    - must be four digit
          "cvv": ""
      }
    }
    ```
     \* All properties must be strings (enclosed in double quotation marks)

5. Run the bot:
   ```
   $ python3 main.py
   ```
   \* To avoid accidental charges, "Process payment" needs to be clicked **manually**
