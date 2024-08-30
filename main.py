import time
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define some global variables
players = {}
tickets = {}

# Starting command handler
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in tickets:
        tickets[user_id] = 5  # Give new players 5 tickets
    update.message.reply_text("Welcome to the snowflake game! You have {} tickets.".format(tickets[user_id]))

# Check tickets
def check_tickets(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in tickets:
        tickets[user_id] = 5  # Set 5 tickets for new players
    update.message.reply_text("You have {} tickets.".format(tickets[user_id]))

# Start game function
def play(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if tickets[user_id] > 0:
        tickets[user_id] -= 1  # Deduct ticket to play
        players[user_id] = 0  # Reset the score for this player
        update.message.reply_text("Game starting! Tap the snowflakes to score points!")
        start_game(update, user_id)
    else:
        update.message.reply_text("You don't have enough tickets to play!")

# Simulate falling snowflakes
def start_game(update: Update, user_id):
    snowflakes = ["❄️", "☃️", "❅", "❆"]
    
    for i in range(5):  # Let the game run for 5 seconds
        snowflake = random.choice(snowflakes)
        update.message.reply_text("Tap the snowflake: {}".format(snowflake))
        time.sleep(1)  # Wait for 1 second before the next snowflake
    update.message.reply_text("Game over! You scored {} points!".format(players[user_id]))

# Tap the snowflake to get points
def tap(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id in players:
        players[user_id] += 1
        update.message.reply_text("Nice! Your current score is: {}".format(players[user_id]))

# Check points
def check_points(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id in players:
        update.message.reply_text("Your current score is: {}".format(players[user_id]))
    else:
        update.message.reply_text("You haven't started a game yet!")

def main() -> None:
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("checktickets", check_tickets))
    dispatcher.add_handler(CommandHandler("play", play))
    dispatcher.add_handler(CommandHandler("tap", tap))
    dispatcher.add_handler(CommandHandler("checkpoints", check_points))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
