Logging
========

This file is recommended to read and use. It contains a lot of useful information about logging in general and how to use it in your application.

What is logging?
--------------------

When your bot suffers an error, as is fairly common in programming, you need to know what went wrong and you need to ensure that your code doesn't stop or break because of it. This is where logging comes in.

Logging is the process of recording information about your application's execution. This information can be used to debug your application and to ensure that it is running smoothly.

Why should I use logging?
--------------------

Once, and if, you release your bot for the public to use, an error would be fatal to your bot. If your bot crashes, it will stop responding to commands and will be unable to do anything. This is a bad thing. 

Logging allows you to record information about your bot's execution and to debug it. This means that you can find out what went wrong and fix it. Logging also allows you to ensure that your bot is running smoothly and that there are no errors that you don't know about.

Example
--------------------

This is the recommended way to use logging in your application.

.. code-block:: python

    from nextguild import *
    import logging
    import datetime

    # Set up logging
    logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    # Log an error, this is the function you will be calling whenever an error occurs
    def log_exception(exc_type, exc_value, exc_traceback):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.exception(f"\n\n\n{timestamp}  -  An unhandled exception occurred", exc_info=(exc_type, exc_value, exc_traceback))
    print("An error occurred:", exc_value)

    # botinformation required for the bot to work
    bot = Client('TOKEN')
    events = Events(bot)

    # This is the proper way to handle an error inside of an event
    @events.on_message
    async def example(data):
    try:
        # Do something
    except Exception as e:
        log_exception(type(e), e, e.__traceback__)


It's that easy! Now you can handle errors in your application and ensure that your bot is running smoothly.

Happy programming!

