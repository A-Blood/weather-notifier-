# weather-notifier-
A weather notifier linked to my Gmail using yagmail. It sends a daily email at 6 AM, informing me whether rain is expected or not. This project is a simple weather notification script using API integration, JSON, and Python.

I decided to build it because, while developing my Python skills, I noticed that a lot of job postings now ask for experience with APIs and GitHub. I wanted to create something practical that could help me learn API integration properly and show a working project on my GitHub profile.

At the start, I installed Python through Visual Studio Code, not directly from the official Python website. I didn't realize at the time that this might cause issues later on — but it worked fine for getting started.

The first thing I did was find an API to work with. I chose OpenWeather's free API because it gives the current weather data, which was enough for a basic notification script. I set it up so that the script would run every morning at 6 AM and email me the weather. At first, it was simple: just pull the weather, format it into a message, and send it to my inbox.

While building it, I started thinking about how I could make it even more useful. I thought about turning it into a child clothing recommendation tool — something that could tell me whether to dress my kids in raincoats, sunscreen, or warm clothes depending on the weather. I also wanted the script to take their ages into account, automatically switching advice from "under 1" to "over 1" when my youngest had their birthday, and offering specific advice for toddlers and older kids.

I realized, though, that the free OpenWeather API only gives the current weather, not the forecast or UV index that I would need. I learned I would have to buy access to their One Call API to get that extra data. I also discovered Buienalarm — a free Dutch rain forecast service — has a openend access for private use. I thought about combining it to send more frequent rain warnings through the day. but the Buienalarm only provides up to date info every 2 hours and scheduling a new  email every 2 hours was too overwhelming for my first project 

But pretty quickly, I realized I was getting ahead of myself. I decided it would be smarter to focus on building the basic version first and making sure it worked well.

When I started testing, I ran into my first real problem. Because the script was set to only send an email at 6 AM if it was raining, I wasn’t receiving any emails to check if it actually worked. To fix this, I added a DEBUG_MODE option: if set to True, it would send the email immediately without waiting for the weather or the time.

Getting the email to send wasn’t straightforward either. Gmail refused to let the app sign in because it flagged it as an unsafe application. I didn’t want to mess around with the security settings on my main Gmail account, so I decided to create a brand-new dummy Gmail just for this project. I set up an App Password, linked it inside my .env file, and tested it again.

Because I care about security, I also set up a separate Mockconfig.env file alongside my real environment file. The mock environment was for safe testing without using real credentials — so if anything went wrong during development or testing, no personal or sensitive information would ever be exposed. I made sure that my .env files were included in my .gitignore, so they would never accidentally get pushed to GitHub either.

While working on this, I realized it would be smart to add some testing for the core functions too. I started with unittest because that's the built-in library, but after reading more about Python testing best practices, I decided to switch to pytest. I downloaded and installed pytest, and ran my tests that way instead. I found that pytest was easier to use because it had a simpler syntax, better output for test failures, and made it easier to add more tests later if I expanded the project. Setting up tests meant I could quickly confirm that the core parts of the script — like API calls and email formatting — were working correctly without always relying on live emails.

After fixing some environment syncing issues (mostly by saving, closing, and reopening VS Code), I finally received my first email with the current weather and temperature. It felt like a massive win.

Next, I wanted to push my project to GitHub. At first, I thought I'd have to manually copy the files over, but after researching a bit, I realized I could connect my local VS Code project to GitHub directly. I learned to install GitHub Desktop, properly initialize Git, and connect my repository.

There were a few problems along the way: my project was originally built inside the venv folder, which caused issues when trying to push. After figuring that out, I created a clean new project folder (Weather-), moved my scripts, reinitialized Git, and reconnected to GitHub properly.

After I finally got it up on GitHub, I decided to re-run the script just to be safe. This time, though, I ran into a new problem: a No pyvenv.cfg file error. Even just running python showed errors. It turned out that because I installed Python originally through Visual Studio, some pieces weren’t fully set up for managing virtual environments.

I decided to fully uninstall Python from Visual Studio.but decided to continue with Visual studios over the official website. After reinstalling, I recreated my virtual environment, reinstalled my packages, and reran the script — and it worked perfectly.

Through this project, I learned so much more than just how to call an API or send an email. I learned how to think about feature scaling, how to build safely with environment files, how to manage real-world errors, and how to properly upload and manage projects on GitHub. More importantly, I learned that real-world coding isn’t about getting things right the first time — it’s about pushing through confusion, fixing broken environments, and staying patient when everything feels like it's going wrong.

And in the end, I proved to myself that I could start something messy, fix it, finish it, and put it live.
