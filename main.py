
from keep_alive import keep_alive
from bot import main
import asyncio

# Start the web server
keep_alive()

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
