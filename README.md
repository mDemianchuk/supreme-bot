## Description
The __Supreme Bot__ is a solution to purchasing limited goods from Supreme New York. After a user provides the desired product(-s) details and supplies payment and shipping information, the bot runs automated scripts to add the product(-s) to the cart and complete the checkout process mocking user behavior.

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

3. Download [ChromeDriver](https://chromedriver.chromium.org/downloads) for your version of Google Chrome, extract the executable, and place it in the root directory:

    ```
    supreme-bot/
    ├── run.py
    ├── ...
    ├── chromedriver (or chromedriver.exe for Windows users)
    ```

4. Fill in `settings.json`:

    ```
    {
      "items": [
          {
              "name": "",                - full or partial item name (case-insensitive)
              "color": "",               - use 1-based index or leave blank for any color
              "size": ""                 - must match sizes on supreme.com (Small, Medium, Large, etc.)
          }
      ],
      "billingInfo": {
          "fullName": "",
          "email": "",
          "phone": "",                   - numerical characters only (no spaces)
          "address": "",                 - street address only (city will be autocompleted by zip)
          "unit": "",                    - leave blank if not applicable
          "zip": "",                     - 6-digit zip code
          "state": "",                   - state abbreviation
          "ccNumber": "",                - numerical characters only (no spaces)
          "expM": "",                    - 2-digit expiration month
          "expY": "",                    - 4-digit expiration year
          "cvv": ""                      - 3 or 4-digit cvv number
      }
    }
    ```
     \* All properties must be strings (enclosed in double quotation marks)

5. Run the bot:
   ```
   $ python3 run.py
   ```
   \* To avoid accidental charges, "Process payment" needs to be clicked **manually**
