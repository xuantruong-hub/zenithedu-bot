
import discord
from discord.ext import commands, tasks
import datetime
import pytz

# 🔧 CONFIG
DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
CHANNEL_ID = 123456789012345678
tz = pytz.timezone("Asia/Ho_Chi_Minh")
TARGET_DATE = tz.localize(datetime.datetime(2026, 6, 26, 7, 30, 0))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

message_to_edit = None

@bot.event
async def on_ready():
    print(f"✅ Bot ZenithEdu đã đăng nhập thành {bot.user}")
    countdown_loop.start()

@tasks.loop(seconds=1)
async def countdown_loop():
    global message_to_edit
    now = datetime.datetime.now(tz)
    delta = TARGET_DATE - now

    if delta.total_seconds() < 0:
        countdown_text = "🎉 Đã đến ngày thi! Chúc các sĩ tử ZenithEdu thành công!"
    else:
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_text = (
            f"🎯 **ZenithEdu - Countdown THPTQG 2026**\n\n"
            f"⏳ Còn **{days}** ngày **{hours}** giờ **{minutes}** phút **{seconds}** giây\n\n"
            "✨ Hãy tận dụng từng phút giây để chuẩn bị thật tốt cho kỳ thi sắp tới.\n"
            "🎓 Ôn tập chăm chỉ, luyện đề đều đặn, giữ cho tinh thần luôn vững vàng nhé!\n"
            "💖 ZenithEdu luôn đồng hành cùng bạn trên con đường chinh phục THPTQG 2026."
        )

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        if message_to_edit is None:
            message_to_edit = await channel.send(countdown_text)
        else:
            await message_to_edit.edit(content=countdown_text)

bot.run(DISCORD_TOKEN)
