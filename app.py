import discord
import csv
from datetime import datetime
from dotenv import load_dotenv

# Load the app token from .env file
load_dotenv()
token = os.getenv('TOKEN')

# Instantiate the discord client
client = discord.Client()

# Asynchronous fucntion that gets called once logged in (on_ready event)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Asynchronous function that gets called on every message
@client.event
async def on_message(message):
    # Checks if the message was sent by the bot itself
    if message.author == client.user:
        return

    # Otherwise, checks the starting commands and responds correspondingly
    if message.content.startswith('$help'):
        await message.channel.send('https://storage.googleapis.com/www.adityaone.com/usage1.png')
        await message.channel.send('https://storage.googleapis.com/www.adityaone.com/usage2.png')

    if message.content.startswith('$subject-list'):
        await message.channel.send('math1, math2, phy1, phy2, chem1, chem2, lang-lit1, lang-lit2, french1, french2, eco, psy, bm, tamil, hindi, tok, cas, cs, itgs, bio')

    if message.content.startswith('$send-chem1'):
        print('get chem1')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'chem1':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no chemistry homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Chemistry Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-chem2'):
        print('get chem2')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'chem2':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no chemistry homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Chemistry Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-phy1'):
        print('get phy1')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'phy1':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no physics homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Physics Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-phy2'):
        print('get phy2')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'phy2':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no physics homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Physics Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-math1'):
        print('get math1')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'math1':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no math homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Math Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-math2'):
        print('get math2')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'math2':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no math homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Math Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-french1'):
        print('get french1')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'french1':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no french homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**French Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-french2'):
        print('get french2')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'french2':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no french homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**French Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-lang-lit1'):
        print('get lang-lit1')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'lang-lit1':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no lang&lit homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Lang&Lit Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-lang-lit2'):
        print('get lang-lit2')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'lang-lit2':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no lang&lit homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Lang&Lit Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-eco'):
        print('get eco')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'eco':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no economics homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Economics Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-psy'):
        print('get psy')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'psy':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no psychology homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Psychology Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-tamil'):
        print('get tamil')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'tamil':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no tamil homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Tamil Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-tok'):
        print('get tok')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'tok':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no TOK homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**TOK Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-bio'):
        print('get bio')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'bio':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no biology homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Biology Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-bm'):
        print('get bm')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'bm':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no business management homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Business Management Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-hindi'):
        print('get hindi')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'hindi':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no hindi homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Hindi Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-cs'):
        print('get cs')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'cs':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no CS homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**CS Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-itgs'):
        print('get itgs')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'itgs':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no ITGS homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**ITGS Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-cas'):
        print('get cas')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'cas':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no CAS homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**CAS Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$send-tamil'):
        print('get tamil')
        homework_list = []
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['subject'] == 'tamil':
                    homework_list.append(row)
        if homework_list == []:
            await message.author.send('There is no tamil homework.')
        else:
            await message.channel.send('Details sent via DM')
            await message.author.send('**Tamil Homework:**')
            for item in homework_list:
                await message.author.send(f"{item['title']}, due on {item['due_date']}")

    if message.content.startswith('$clear-completed-hw'):
        print('delete hw')
        print(datetime.today().strftime('%d/%m/%y'))
        new_csv = []
        with open('homework.csv', mode='r') as csv_file:
            print()
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['due_date'] != datetime.today().strftime('%d/%m/%y'):
                    new_csv.append(row)
        print(new_csv)
        with open('homework.csv', mode='w') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            writer = csv.DictWriter(csv_file, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerows(new_csv)
        await message.channel.send('All homework due for today was deleted.')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! Nice to meet you.')
    
    if message.content.startswith('$send-all-hw'):
        print('get homework')
        with open('homework.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            homework_list = []
            for row in csv_reader:
                print(row)
                print(line_count)
                print(homework_list)
                line_count += 1
                homework_list.append(row);
            if line_count == 0:
                await message.author.send('No homework for you!')
            else:
                await message.channel.send('Homework sent via DM')
                for item in homework_list:
                    print(item)
                    await message.author.send(f"**{item['subject'].upper()}**: {item['title']}, due on: *{item['due_date']}*")
        
    if message.content.startswith('$add-chem1'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'chem1', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to chem1')

    if message.content.startswith('$add-chem2'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'chem2', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to chem2')

    if message.content.startswith('$add-phy1'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'phy1', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to phy1')

    if message.content.startswith('$add-phy2'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'phy2', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to phy2')

    if message.content.startswith('$add-math1'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'math1', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to math1')

    if message.content.startswith('$add-math2'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'math2', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to math2')

    if message.content.startswith('$add-french1'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'french1', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to french1')

    if message.content.startswith('$add-french2'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'french2', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to french2')

    if message.content.startswith('$add-lang-lit1'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'lang-lit1', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to lang-lit1')

    if message.content.startswith('$add-lang-lit2'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'lang-lit2', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to lang-lit2')

    if message.content.startswith('$add-eco'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'eco', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to eco')
    
    if message.content.startswith('$add-psy'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'psy', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to psy')

    if message.content.startswith('$add-tamil'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'tamil', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to tamil')

    if message.content.startswith('$add-tok'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'tok', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to tok')

    if message.content.startswith('$add-bio'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'bio', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to bio')

    if message.content.startswith('$add-bm'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'bm', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to bm')

    if message.content.startswith('$add-hindi'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'hindi', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to hindi')

    if message.content.startswith('$add-cs'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'cs', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to cs')

    if message.content.startswith('$add-itgs'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'itgs', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to itgs')

    if message.content.startswith('$add-cas'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'cas', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to cas')

    if message.content.startswith('$add-tamil'):
        print('add chem1')
        with open('homework.csv', mode='a') as csv_file:
            fieldNames = ['subject', 'title', 'due_date']
            homework_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

            homework_writer.writerow({ 'subject': 'tamil', 'title': message.content.split(';')[1], 'due_date': message.content.split(';')[2] })
            # csv_file.close()
        await message.channel.send('Homework added to tamil')

client.run(token)
