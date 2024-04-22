"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot, Backend

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

import warnings

from dotenv import load_dotenv
import os

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Load environment variables
load_dotenv()

def main():
    warnings.simplefilter('ignore', category=UserWarning)

    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    # Implement here your logic...
    app_path = os.getenv('CRM_PATH')
    bot.execute(app_path)

    app = bot.connect_to_app(Backend.UIA, path = app_path, title = "My CRM (Sample App)")

    # Fill text input fields
    first_field = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "textBoxPeopleFirstName")
    first_field.set_text("First")

    last_field = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "textBoxPeopleLastName")
    last_field.set_text("Last")

    # Tabs navigation
    company_tab = bot.find_app_element(from_parent_window = app.top_window(), control_type = "TabItem", title = "Company ")
    company_tab.select()

    other_tab = bot.find_app_element(from_parent_window = app.top_window(), control_type = "TabItem", title = "Other")
    other_tab.select()

    # Select dropdown
    state_dropdown = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "comboBoxPeopleAddressState")
    state_dropdown.select("CO")

    # Handle checkbox
    # is_active_checkbox = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "checkBox1")
    # if is_active_checkbox.get_toggle_state() == 0:
    #     print("The checkbox it's unchecked, let's check it!")
    #     is_active_checkbox.toggle()
    # else:
    #     print("Checkbox already checked!")

    save_btn = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "button1")
    save_btn.click()

    browse_btn = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "button2")
    browse_btn.click()


    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()